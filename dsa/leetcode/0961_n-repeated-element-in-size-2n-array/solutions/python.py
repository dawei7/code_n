"""Optimal app-local solution for LeetCode 961."""


def solve(nums):
    seen = set()
    for value in nums:
        if value in seen:
            return value
        seen.add(value)
    raise ValueError("input does not contain the promised repeated value")
