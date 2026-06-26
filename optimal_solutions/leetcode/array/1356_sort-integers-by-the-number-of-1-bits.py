"""Optimal solution for LeetCode 1356: Sort Integers by The Number of 1 Bits."""


def solve(arr: list[int]) -> list[int]:
    return sorted(arr, key=lambda value: (value.bit_count(), value))
