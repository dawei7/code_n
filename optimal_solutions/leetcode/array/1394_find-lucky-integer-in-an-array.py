"""Optimal solution for LeetCode 1394: Find Lucky Integer in an Array."""

from collections import Counter


def solve(arr: list[int]) -> int:
    counts = Counter(arr)
    return max((value for value, count in counts.items() if value == count), default=-1)
