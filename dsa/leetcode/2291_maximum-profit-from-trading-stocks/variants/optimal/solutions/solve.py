from typing import List


def solve(present: List[int], future: List[int], budget: int) -> int:
    best = [0] * (budget + 1)

    for price, later_price in zip(present, future):
        gain = later_price - price
        for money in range(budget, price - 1, -1):
            best[money] = max(best[money], best[money - price] + gain)

    return best[budget]
