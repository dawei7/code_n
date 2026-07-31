"""App-local reference solution for LeetCode 2824."""

from typing import List


def solve(nums: List[int], target: int) -> int:
    """Count index pairs whose sum is strictly below target."""
    values = sorted(nums)
    left = 0
    right = len(values) - 1
    pairs = 0

    while left < right:
        if values[left] + values[right] < target:
            pairs += right - left
            left += 1
        else:
            right -= 1

    return pairs
