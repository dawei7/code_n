"""Optimal app-local solution for LeetCode 1400."""

from collections import Counter


def solve(s: str, k: int) -> bool:
    if k > len(s):
        return False
    odd_count = sum(frequency % 2 for frequency in Counter(s).values())
    return odd_count <= k
