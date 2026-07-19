"""Optimal app-local solution for LeetCode 1558."""


def solve(nums: list[int]) -> int:
    """Count forced individual increments and shared doubling stages."""
    increments = sum(value.bit_count() for value in nums)
    doubles = max(0, max(nums).bit_length() - 1)
    return increments + doubles
