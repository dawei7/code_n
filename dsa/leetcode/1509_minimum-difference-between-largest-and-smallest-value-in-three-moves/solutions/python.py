"""Optimal app-local solution for LeetCode 1509."""

from heapq import nlargest, nsmallest


def solve(nums: list[int]) -> int:
    """Return the minimum range after changing at most three occurrences."""
    if len(nums) <= 4:
        return 0
    smallest = nsmallest(4, nums)
    largest = sorted(nlargest(4, nums))
    return min(high - low for low, high in zip(smallest, largest))
