import pandas as pd


def solve(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(
        index="month", columns="city", values="temperature"
    ).reset_index()
