"""App-local reference solution for LeetCode 2826."""

from typing import List


def solve(nums: List[int]) -> int:
    """Return the minimum deletions needed for a non-decreasing subsequence."""
    longest = [0, 0, 0]

    for value in nums:
        index = value - 1
        longest[index] = 1 + max(longest[: index + 1])

    return len(nums) - max(longest)
