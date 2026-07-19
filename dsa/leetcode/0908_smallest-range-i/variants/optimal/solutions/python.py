"""Optimal app-local solution for LeetCode 908."""


def solve(nums, k):
    return max(0, max(nums) - min(nums) - 2 * k)
