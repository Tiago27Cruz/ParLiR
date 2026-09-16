from __future__ import annotations
from transformers import pipeline
from rdflib import Graph, RDFS, Namespace
import random
import xml.etree.ElementTree as ET
from typing import Dict, List, Set, TypedDict
import torch
import re

POLIS_INI = Namespace("http://purl.org/polis/ar/initiatives#")
BIBO = Namespace("http://purl.org/ontology/bibo/")
QRELS_PATH: str = "../data/qrels/qrels_test.trec"
TOPICS_PATH: str = "../data/queries/topics.xml"


def get_initiatives() -> dict:

    g = Graph()
    g.parse("data/corpus/legislature_xvi.ttl")

    q = """
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX dct: <http://purl.org/dc/terms/>
    PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX polis-ini: <http://purl.org/polis/ar/initiatives#>
    PREFIX polis-core: <http://purl.org/polis/ar/core#>
    PREFIX bibo: <http://purl.org/ontology/bibo/>
    PREFIX schema: <https://schema.org/>

    SELECT DISTINCT ?initiative ?content ?typeLabel 
    (GROUP_CONCAT(DISTINCT COALESCE(?propName, ""); separator=", ") AS ?proponents)
    (GROUP_CONCAT(DISTINCT COALESCE(?authName, ""); separator=", ") AS ?authors)
    WHERE {
        ?initiative a ?type .
        ?type rdfs:subClassOf* polis-ini:Initiative .

        ?type rdfs:label ?typeLabel .

        OPTIONAL {{
                ?initiative polis-ini:hasProponent ?pg .
					?pg polis-core:isOfParty ?party .
				?party foaf:name ?propName .
            }}
        
        OPTIONAL {{
                ?initiative polis-ini:hasAuthor ?parliamentarian .
                ?parliamentarian foaf:name ?authName .
            }}

        ?initiative polis-ini:hasContent ?doc .
        ?doc bibo:content ?content .
    }
    GROUP BY ?initiative ?content ?typeLabel
    """

    initiative_contents = {}
    for row in g.query(
        q,
        initNs={
            "rdfs": RDFS,
            "polis-ini": POLIS_INI,
            "bibo": BIBO,
        }
    ):
        initiative_contents[str(row.initiative)] = {
            'text': str(row.content),
            'type': str(row.typeLabel),
            'proponents': str(row.proponents),
            'authors': str(row.authors)
        }

    return initiative_contents

def get_ia_labels(pairs: list[Pair]):
    
    pipe = pipeline("text-generation", model="Qwen/Qwen3-8B", device_map="auto")

    prompt_default = """
        You are a relevance assessor for a parliamentary information retrieval system.
Given a query and a document, judge whether the document is relevant to the query's
information need.

Answer with exactly one character: 1 if the document is relevant or 0 if it is not.
Do not explain.
Do not think aloud.
Do not output <think>.
    """

    for pair in pairs:
        print("Query: ", pair['title'])
        prompt = f"""
            {prompt_default}

            Query: {pair['title']}
            Information Need: {pair['desc']}
            Relevance criteria: {pair['narr']}

            Document Text: {pair['doc_text']}
            Document Type: {pair['doc_type']}
            Document Proponents: {pair['doc_proponents']}
            Document Authors: {pair['doc_authors']}

Answer with exactly one character: 1 if the document is relevant or 0 if it is not.
Do not explain.
Do not think aloud.
Do not output <think>.
        """

        message=[
            {"role":"user", "content":prompt}
        ]

        result: list[dict] = pipe(
            message,
            max_new_tokens=5,
            do_sample=False
        )

        response: str = result[0]["generated_text"][-1]["content"]
        response = re.sub(
            r"<think>.*?</think>",
            "",
            response,
            flags=re.DOTALL
        ).strip()
        print(f"{pair['doc_id']} -- AI: {response} | Tiago {pair['relevance']}")
        with open("out/iaa.csv", '+a') as f:
            f.write(f"{pair['doc_id']},{response},{pair['relevance']}\n")

class QueryInfo(TypedDict):
    title: str
    desc: str
    narr: str


class Pair(TypedDict):
    query_id: str
    query_type: str
    relevance: int
    doc_id: str
    doc_text:str
    doc_type:str
    doc_proponents:str
    doc_authors:str
    title: str
    desc: str
    narr: str

def load_topics(path: str) -> Dict[str, QueryInfo]:
    tree = ET.parse(path)
    root = tree.getroot()

    topics: Dict[str, QueryInfo] = {}

    for topic in root.findall(".//top"):
        qid: str = str(topic.find("num").text.strip())
        title: str = (topic.find("title").text or "").strip()
        desc: str = (topic.find("desc").text or "").strip()
        narr: str = (topic.find("narr").text or "").strip()
        topics[qid] = {
            "title": title,
            "desc": desc,
            "narr": narr
        }

    return topics

def load_qrels(path: str) -> Dict[str, Set[str]]:
    relevant_docs: Dict[str, Set[str]] = {}

    with open(path, encoding="utf-8") as f:
        for line in f:
            query_id_str, _, doc_id, rel_str = line.split()
            rel: int = int(rel_str)

            if rel != 1: continue

            relevant_docs.setdefault(query_id_str, set()).add(doc_id)

    return relevant_docs



def sample_pairs(topics: Dict[str, QueryInfo],relevant_docs: Dict[str, Set[str]],initiatives) -> List[Pair]:
    metadata_ins: Set[int] = {1,2,10,12,13,15,16,17,18,21,22,23,24,28,29}
    rng = random.Random(42)
    all_docs: Set[str] = initiatives.keys()

    lexical_queries: List[str] = [q
        for q in relevant_docs.keys()
        if int(q.split('-')[0]) not in metadata_ins
    ]

    metadata_queries: List[str] = [
        q
        for q in relevant_docs.keys()
        if int(q.split('-')[0]) in metadata_ins
    ]

    selected_lexical_rel: List[str] = rng.sample(lexical_queries,  6)

    remaining_lexical: List[str] = [ q for q in lexical_queries if q not in selected_lexical_rel]

    selected_lexical_nonrel: List[str] = rng.sample(  remaining_lexical,6 )

    selected_metadata_rel: List[str] = rng.sample( metadata_queries,6)

    remaining_metadata: List[str] = [q for q in metadata_queries if q not in selected_metadata_rel  ]

    selected_metadata_nonrel: List[str] = rng.sample(remaining_metadata, 6)

    pairs: List[Pair] = []

    #
    # lexical + relevant
    #
    for qid in selected_lexical_rel:

        doc_id: str = rng.choice(
            list(relevant_docs[qid])
        )

        pairs.append({
            "query_id": qid,
            "query_type": "lexical",
            "relevance": 1,
            "doc_id": doc_id,
            "doc_text": initiatives[doc_id]['text'],
            "doc_type": initiatives[doc_id]['type'],
            "doc_proponents": initiatives[doc_id]['proponents'],
            "doc_authors": initiatives[doc_id]['authors'],
            "title": topics[qid]["title"],
            "desc": topics[qid]["desc"],
            "narr": topics[qid]["narr"]
        })

    #
    # lexical + non relevant
    #
    for qid in selected_lexical_nonrel:

        non_relevant_pool: List[str] = list(
            all_docs - relevant_docs[qid]
        )

        doc_id: str = rng.choice(
            non_relevant_pool
        )

        pairs.append({
            "query_id": qid,
            "query_type": "lexical",
            "relevance": 0,
            "doc_id": doc_id,
            "doc_text": initiatives[doc_id]['text'],
            "doc_type": initiatives[doc_id]['type'],
            "doc_proponents": initiatives[doc_id]['proponents'],
            "doc_authors": initiatives[doc_id]['authors'],
            "title": topics[qid]["title"],
            "desc": topics[qid]["desc"],
            "narr": topics[qid]["narr"]
        })

    #
    # metadata + relevant
    #
    for qid in selected_metadata_rel:

        doc_id: str = rng.choice(
            list(relevant_docs[qid])
        )

        pairs.append({
            "query_id": qid,
            "query_type": "metadata",
            "relevance": 1,
            "doc_id": doc_id,
            "doc_text": initiatives[doc_id]['text'],
            "doc_type": initiatives[doc_id]['type'],
            "doc_proponents": initiatives[doc_id]['proponents'],
            "doc_authors": initiatives[doc_id]['authors'],
            "title": topics[qid]["title"],
            "desc": topics[qid]["desc"],
            "narr": topics[qid]["narr"]
        })

    #
    # metadata + non relevant
    #
    for qid in selected_metadata_nonrel:

        non_relevant_pool: List[str] = list(
            all_docs - relevant_docs[qid]
        )

        doc_id: str = rng.choice(
            non_relevant_pool
        )

        pairs.append({
            "query_id": qid,
            "query_type": "metadata",
            "relevance": 0,
            "doc_id": doc_id,
            "doc_text": initiatives[doc_id]['text'],
            "doc_type": initiatives[doc_id]['type'],
            "doc_proponents": initiatives[doc_id]['proponents'],
            "doc_authors": initiatives[doc_id]['authors'],
            "title": topics[qid]["title"],
            "desc": topics[qid]["desc"],
            "narr": topics[qid]["narr"]
        })

    return pairs


if __name__ == "__main__":
    print(torch.cuda.is_available())
    topics = load_topics(TOPICS_PATH)
    relevant_docs = load_qrels(QRELS_PATH)

    pairs = sample_pairs(topics,relevant_docs,get_initiatives())
    get_ia_labels(pairs)