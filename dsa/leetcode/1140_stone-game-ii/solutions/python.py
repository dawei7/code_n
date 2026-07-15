"""Optimal app-local solution for LeetCode 1140."""

from functools import cache


def solve(piles: list[int]) -> int:
    n = len(piles)
    suffix = [0] * (n + 1)
    for index in range(n - 1, -1, -1):
        suffix[index] = suffix[index + 1] + piles[index]

    @cache
    def best(index: int, m: int) -> int:
        if index + 2 * m >= n:
            return suffix[index]
        opponent = min(
            best(index + taken, max(m, taken))
            for taken in range(1, 2 * m + 1)
        )
        return suffix[index] - opponent

    return best(0, 1)
