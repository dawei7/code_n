"""Optimal app-local solution for LeetCode 1150."""

from bisect import bisect_left


def solve(nums: list[int], target: int) -> bool:
    first = bisect_left(nums, target)
    majority_offset = first + len(nums) // 2
    return majority_offset < len(nums) and nums[majority_offset] == target
