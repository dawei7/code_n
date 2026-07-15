"""Optimal app-local solution for LeetCode 1331."""


def solve(arr):
    ranks = {value: rank for rank, value in enumerate(sorted(set(arr)), start=1)}
    return [ranks[value] for value in arr]
