from ranx import Qrels, Run, evaluate
from pathlib import Path
from gmap import gmap
from collections import defaultdict

BASE_DIR: Path = Path(__file__).resolve().parent.parent
QRELS_PATH = BASE_DIR / "data" / "qrels" / "qrels_test.trec"
RUNS_DIR = BASE_DIR / "data" / "runs"

metadata_ins: set[int] = {1,2,10,12,13,15,16,17,18,21,22,23,24,28,29}
qrels: Qrels = Qrels.from_file(str(QRELS_PATH))

metadata_qrels_dict: dict = {qid: rels for qid, rels in qrels.qrels.items()if int(qid.split("-")[0]) in metadata_ins}
metadata_qrels: Qrels = Qrels.from_dict(metadata_qrels_dict)

lexical_qrels_dict: dict = {qid: rels for qid, rels in qrels.qrels.items() if not int(qid.split("-")[0]) in metadata_ins}
lexical_qrels: Qrels = Qrels.from_dict(lexical_qrels_dict)


runs = {
    "BM25": Run.from_file(str(RUNS_DIR / "bm25.run"), kind="trec"),
    "QL": Run.from_file(str(RUNS_DIR / "ql.run"), kind="trec"),
    "TFIDF": Run.from_file(str(RUNS_DIR / "tfidf.run"), kind="trec"),
}

metrics = [
    "ndcg@5",
    "ndcg@10",
    "ndcg@100",
    "map@5",
    "map@10",
    "map@100",
    "precision@5",
    "precision@10",
    "precision@100",
    "recall@5",
    "recall@10",
    "recall@100",
    "r-precision",
    "mrr@10"
]

less_metrics = [
    "precision@10",
    "recall@10",
    "ndcg@10"
]

for name, run in runs.items():
    scores = evaluate(qrels, run, metrics)
    print(f"\n{name}")

    if not isinstance(scores, dict): continue
    for metric, value in scores.items():
        print(f"  {metric}: {value:.3f}")
    for k in [5, 10, 100]:
        print(f"  gmap@{k}: {gmap(qrels, run, k):.3f}")

    if name== "BM25":
        metadata_run_dict: dict = {qid: rels for qid, rels in run.run.items() if int(qid.split("-")[0]) in metadata_ins}
        metadata_run = Run.from_dict(metadata_run_dict)
        lexical_run_dict: dict = {qid: rels for qid, rels in run.run.items() if not int(qid.split("-")[0]) in metadata_ins}
        lexical_run = Run.from_dict(lexical_run_dict)

        metadata_scores = evaluate(metadata_qrels, metadata_run, less_metrics)
        if not isinstance(metadata_scores, dict): continue
        print(f"\n{name} -- METADATA ONLY")
        for metric, value in metadata_scores.items():
            print(f"  {metric}: {value:.3f}")

        lexical_scores = evaluate(lexical_qrels, lexical_run, less_metrics)
        if not isinstance(lexical_scores, dict): continue
        print(f"\n{name} -- LEXICAL ONLY")
        for metric, value in lexical_scores.items():
            print(f"  {metric}: {value:.3f}")

# Vector 5 iteration process

metric_scores: dict[str, list[float]] = defaultdict(list)
gmap_scores: dict[int, list[float]] = defaultdict(list)

print("\nVector:")

for iteration in range(5):
    run_path: Path = RUNS_DIR / f"vector_{iteration}.run"

    run: Run = Run.from_file(str(run_path), kind="trec")

    scores = evaluate(qrels, run, metrics)

    if isinstance(scores, dict):
        for metric, value in scores.items():
            metric_scores[metric].append(value)

    for k in [5, 10, 100]:
        gmap_scores[k].append(gmap(qrels, run, k))

for metric in metrics:
    avg: float = sum(metric_scores[metric]) / len(metric_scores[metric])
    print(f"  {metric}: {avg:.3f}")

for k in [5, 10, 100]:
    avg_gmap: float = sum(gmap_scores[k]) / len(gmap_scores[k])
    print(f"  gmap@{k}: {avg_gmap:.3f}")