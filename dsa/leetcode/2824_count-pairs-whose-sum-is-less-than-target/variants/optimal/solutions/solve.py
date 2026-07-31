"""App-local reference solution for LeetCode 2824."""

from typing import List


def solve(nums: List[int], target: int) -> int:
    """Count index pairs whose sum is strictly below target."""
    nums.sort()
    left = 0
    right = len(nums) - 1
    pairs = 0

    while left < right:
        if nums[left] + nums[right] < target:
            pairs += right - left
            left += 1
        else:
            right -= 1

    return pairs
