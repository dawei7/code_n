"""Optimal solution for LeetCode 1072: Flip Columns For Maximum Number of Equal Rows."""

from collections import Counter


def solve(matrix: list[list[int]]) -> int:
    patterns: Counter[tuple[int, ...]] = Counter()
    for row in matrix:
        first = row[0]
        pattern = tuple(value ^ first for value in row)
        patterns[pattern] += 1
    return max(patterns.values())
