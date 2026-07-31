import pandas as pd


def solve(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals["weight"] > 100].sort_values(by="weight", ascending=False)[["name"]]
