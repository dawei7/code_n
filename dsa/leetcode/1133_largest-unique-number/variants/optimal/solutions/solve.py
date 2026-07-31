"""Optimal app-local solution for LeetCode 1133."""


def solve(nums: list[int]) -> int:
    counts = [0] * 1001
    for value in nums:
        counts[value] += 1
    for value in range(1000, -1, -1):
        if counts[value] == 1:
            return value
    return -1
