"""Optimal app-local solution for LeetCode 1413."""


def solve(nums: list[int]) -> int:
    prefix = 0
    minimum_prefix = 0
    for value in nums:
        prefix += value
        minimum_prefix = min(minimum_prefix, prefix)
    return 1 - minimum_prefix
