"""Optimal app-local solution for LeetCode 1356."""


def solve(arr):
    return sorted(arr, key=lambda value: (value.bit_count(), value))
