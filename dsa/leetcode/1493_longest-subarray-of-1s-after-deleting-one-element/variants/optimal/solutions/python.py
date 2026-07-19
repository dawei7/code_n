"""Optimal app-local solution for LeetCode 1493."""


def solve(nums: list[int]) -> int:
    """Return the longest all-ones run after exactly one deletion."""
    left = 0
    zeros = 0
    best = 0

    for right, value in enumerate(nums):
        if value == 0:
            zeros += 1

        while zeros > 1:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        best = max(best, right - left)

    return best
