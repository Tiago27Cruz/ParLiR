from math import exp, log
from ranx import Qrels, Run


def average_precision_at_k(qrels: dict[str, int], run: dict[str, float], k: int | None = None) -> float:
    relevant_docs: set[str] = set(qrels.keys())
    if len(relevant_docs) == 0: return 0.0

    ranked_docs: list[str] = [doc_id for doc_id, _ in sorted(run.items(), key=lambda x: x[1], reverse=True)]

    if k is not None: ranked_docs = ranked_docs[:k]

    hits: int = 0
    ap: float = 0.0

    for rank, doc_id in enumerate(ranked_docs, start=1):
        if doc_id in relevant_docs:
            hits += 1
            ap += hits / rank

    return ap / len(relevant_docs)


def gmap(qrels: Qrels, run: Run, k: int | None = None, epsilon: float = 1e-5) -> float:
    aps: list[float] = []

    for qid in qrels.qrels:
        ap: float = average_precision_at_k(qrels.qrels[qid], run.run[qid], k=k)
        aps.append(ap)

    if not aps:return 0.0

    return exp(sum(log(ap + epsilon) for ap in aps)/ len(aps))