"""Optimal solution for LeetCode 1051: Height Checker."""


def solve(heights: list[int]) -> int:
    return sum(actual != expected for actual, expected in zip(heights, sorted(heights)))
