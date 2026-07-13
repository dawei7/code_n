"""Optimal solution for LeetCode 1122: Relative Sort Array."""

from collections import Counter


def solve(arr1: list[int], arr2: list[int]) -> list[int]:
    counts = Counter(arr1)
    answer: list[int] = []
    for value in arr2:
        answer.extend([value] * counts.pop(value, 0))
    for value in sorted(counts):
        answer.extend([value] * counts[value])
    return answer
