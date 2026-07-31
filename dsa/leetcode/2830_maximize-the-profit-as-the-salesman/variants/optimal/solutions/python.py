"""App-local reference solution for LeetCode 2830."""

from bisect import bisect_left
from typing import List


def solve(n: int, offers: List[List[int]]) -> int:
    """Return the maximum gold from pairwise disjoint inclusive offers."""
    offer_count = len(offers)
    if n > offer_count * (offer_count.bit_length() + 1):
        ordered = sorted(offers, key=lambda offer: offer[1])
        ends = []
        prefix_best = [0]

        for start, end, gold in ordered:
            compatible_count = bisect_left(ends, start)
            candidate = prefix_best[compatible_count] + gold
            ends.append(end)
            prefix_best.append(max(prefix_best[-1], candidate))

        return prefix_best[-1]

    offers_by_end = [[] for _ in range(n)]
    for start, end, gold in offers:
        offers_by_end[end].append((start, gold))

    best = [0] * (n + 1)
    for end in range(n):
        best[end + 1] = best[end]
        for start, gold in offers_by_end[end]:
            best[end + 1] = max(best[end + 1], best[start] + gold)

    return best[n]
