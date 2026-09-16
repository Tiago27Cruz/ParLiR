from typing import List
import pandas as pd
from sklearn.metrics import cohen_kappa_score


def compute_kappa(csv_path: str) -> float:
    df: pd.DataFrame = pd.read_csv(csv_path)

    ai_labels: List[int] = df["ai"].astype(int).tolist()
    human_labels: List[int] = df["firstAuthor"].astype(int).tolist()

    return cohen_kappa_score(human_labels, ai_labels)


if __name__ == "__main__":
    kappa: float = compute_kappa("../data/iaa/iaa.csv")
    print(f"Cohen's κ = {kappa:.4f}")