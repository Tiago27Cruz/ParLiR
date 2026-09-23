from typing import List
import pandas as pd
from sklearn.metrics import cohen_kappa_score
from pathlib import Path

CSV_PATH : Path = Path(__file__).resolve().parent.parent / "data" / "iaa" / "iaa.csv"


def compute_kappa() -> float:
    df: pd.DataFrame = pd.read_csv(CSV_PATH)

    ai_labels: List[int] = df["ai"].astype(int).tolist()
    human_labels: List[int] = df["firstAuthor"].astype(int).tolist()

    return cohen_kappa_score(human_labels, ai_labels)


if __name__ == "__main__":
    kappa: float = compute_kappa()
    print(f"Cohen's κ = {kappa:.4f}")