import pandas as pd


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index="month", columns="city", values="temperature")


def solve(weather: pd.DataFrame) -> pd.DataFrame:
    return pivotTable(weather).reset_index()
