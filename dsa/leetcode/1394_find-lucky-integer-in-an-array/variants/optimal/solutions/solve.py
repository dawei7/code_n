"""Optimal app-local solution for LeetCode 1394."""

from collections import Counter


def solve(arr: list[int]) -> int:
    frequencies = Counter(arr)
    return max(
        (value for value, frequency in frequencies.items() if value == frequency),
        default=-1,
    )
