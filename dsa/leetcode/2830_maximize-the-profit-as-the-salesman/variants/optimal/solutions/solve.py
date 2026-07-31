"""App-local reference solution for LeetCode 2830."""

from typing import List


def solve(n: int, offers: List[List[int]]) -> int:
    """Return the maximum gold from pairwise disjoint inclusive offers."""
    offers_by_end = [[] for _ in range(n)]
    for start, end, gold in offers:
        offers_by_end[end].append((start, gold))

    best = [0] * (n + 1)
    for end in range(n):
        best[end + 1] = best[end]
        for start, gold in offers_by_end[end]:
            best[end + 1] = max(best[end + 1], best[start] + gold)

    return best[n]
