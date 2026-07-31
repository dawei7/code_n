from typing import List


def solve(prices: List[int]) -> int:
    totals: dict[int, int] = {}
    for index, price in enumerate(prices):
        key = price - index
        totals[key] = totals.get(key, 0) + price
    return max(totals.values())
