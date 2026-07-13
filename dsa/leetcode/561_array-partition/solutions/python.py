"""Sorted adjacent pairing for LeetCode 561."""


def solve(nums: list[int]) -> int:
    ordered = sorted(nums)
    return sum(ordered[::2])

