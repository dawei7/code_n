"""Optimal app-local solution for LeetCode 1512."""


def solve(nums: list[int]) -> int:
    """Count equal-value index pairs in one left-to-right pass."""
    frequencies: dict[int, int] = {}
    pairs = 0
    for value in nums:
        pairs += frequencies.get(value, 0)
        frequencies[value] = frequencies.get(value, 0) + 1
    return pairs
