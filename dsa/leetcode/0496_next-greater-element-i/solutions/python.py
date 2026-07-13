"""Monotonic-stack mapping for LeetCode 496."""


def solve(nums1: list[int], nums2: list[int]) -> list[int]:
    next_greater: dict[int, int] = {}
    stack: list[int] = []
    for value in nums2:
        while stack and stack[-1] < value:
            next_greater[stack.pop()] = value
        stack.append(value)
    return [next_greater.get(value, -1) for value in nums1]
