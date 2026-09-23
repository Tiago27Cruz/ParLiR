# ParLiR - A Test Collection for Information Retrieval over Portuguese Parliamentary Initiatives

[![DOI](https://zenodo.org/badge/1357651635.svg)](https://doi.org/10.5281/zenodo.22915661)

Submitted to ECIR2027

## Dataset

The parliamentary initiatives and associated metadata provided in ``data/corpus/legislature_xvi.ttl`` were collected from the official [Portuguese Parliament's open data section](https://www.parlamento.pt/Cidadania/Paginas/DadosAbertos.aspx).

The dataset is distributed in accordance with the terms established by the Portuguese Parliament. Users are requested to acknowledge the original [source](https://www.parlamento.pt/Cidadania/Paginas/DadosAbertos.aspx) when reusing the data.

All dataset resources are located under the ``data/`` directory.

### Directory Structure

- **corpus/**: Contains the document collection used throughout the experiments. The file ``legislature_xvi.ttl`` stores the knowledge graph representing parliamentary initiatives from the XVI Legislature. The file ``initiatives.ttl`` contains the initiative module of the POLIS ontology and is used by ``iaa.py`` to retrieve all subclasses of ``Initiative`` through SPARQL queries.

- **iaa/**: Contains the inter-annotator agreement data. The file ``iaa.csv`` stores the relevance assessments used to measure agreement between human and LLM annotators.

- **qrels/**: Contains the relevance judgments in multiple formats, including ``.trec``, ``.parquet``, and ``.json``. This directory also includes the train/test partitions used in the experiments (``qrels_complete``, ``qrels_test``, and ``qrels_train``).

- **queries/**: Contains ``topics.xml``, which defines all information needs in TREC format. Each topic includes a unique identifier, title, description (information need), and narrative (relevance criteria).

- **runs/**: Contains the baseline retrieval runs in TREC ``.run`` format (BM25, Query Likelihood, TF-IDF, and Vector Search). Since the vector retrieval baseline relies on Faiss HNSW, which introduces non-deterministic behavior, five independent runs are provided to support the computation of averaged effectiveness metrics.

## Reproducing the Experiments

All source code required to reproduce the dataset generation and evaluation procedures is available under the ``scripts/`` directory.

First, install the project dependencies:
```
uv sync
```

Scripts can then be executed using:
```
uv run ./scripts/<script_name>.py
```

### Script Overview

- **qrels.py**: Generates the relevance judgments and exports them to the supported formats. This script also performs the train/test partitioning procedure used in the evaluation.

- **iaa.py**: Generates a stratified sample of query–initiative pairs and prompts a locally hosted Qwen3-8B model to assess relevance. The model receives a structured prompt containing initiative metadata, initiative text, the topic description, and the narrative relevance criteria.

- **evaluation.py**: Computes all retrieval effectiveness metrics reported in the paper using the ``ranx`` evaluation framework.

- **cohen.py**: Computes Cohen's κ coefficient using the annotations stored in ``data/iaa/iaa.csv``.

- **distribution.ipynb**: Produces the collection distribution visualisation presented in the paper.