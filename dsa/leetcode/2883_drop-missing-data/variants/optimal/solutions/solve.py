import pandas as pd


def solve(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=["name"])
