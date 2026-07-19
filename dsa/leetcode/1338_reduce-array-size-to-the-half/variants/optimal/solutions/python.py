"""Optimal app-local solution for LeetCode 1338."""

from collections import Counter


def solve(arr):
    target = len(arr) // 2
    removed = 0

    for selected, frequency in enumerate(
        sorted(Counter(arr).values(), reverse=True), start=1
    ):
        removed += frequency
        if removed >= target:
            return selected

    raise AssertionError("A non-empty legal array must reach its removal target")
