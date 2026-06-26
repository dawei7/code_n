"""Optimal solution for LeetCode 1128: Number of Equivalent Domino Pairs."""

from collections import Counter


def solve(dominoes: list[list[int]]) -> int:
    counts: Counter[tuple[int, int]] = Counter()
    pairs = 0
    for a, b in dominoes:
        key = (a, b) if a <= b else (b, a)
        pairs += counts[key]
        counts[key] += 1
    return pairs
