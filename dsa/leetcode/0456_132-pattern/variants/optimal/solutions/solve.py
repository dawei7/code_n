"""Reverse monotonic-stack solution for LeetCode 456."""


def solve(nums: list[int]) -> bool:
    stack: list[int] = []
    middle = float("-inf")
    for value in reversed(nums):
        if value < middle:
            return True
        while stack and value > stack[-1]:
            middle = stack.pop()
        stack.append(value)
    return False
