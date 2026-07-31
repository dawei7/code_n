import pandas as pd


def solve(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=["email"], keep="first")
