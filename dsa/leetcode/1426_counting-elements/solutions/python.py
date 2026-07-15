"""Optimal app-local solution for LeetCode 1426."""


def solve(arr: list[int]) -> int:
    values = set(arr)
    return sum(value + 1 in values for value in arr)
