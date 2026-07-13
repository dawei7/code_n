"""Optimal solution for LeetCode 1365: How Many Numbers Are Smaller Than the Current Number."""


def solve(nums: list[int]) -> list[int]:
    counts = [0] * 102
    for value in nums:
        counts[value + 1] += 1
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
    return [counts[value] for value in nums]
