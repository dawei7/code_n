"""Median absolute-deviation solution for LeetCode 462."""


def solve(nums: list[int]) -> int:
    ordered = sorted(nums)
    median = ordered[len(ordered) // 2]
    total = 0
    for value in ordered:
        total += abs(value - median)
    return total
