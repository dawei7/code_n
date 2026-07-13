"""Optimal app-local solution for LeetCode 442."""


def solve(nums: list[int]) -> list[int]:
    duplicates: list[int] = []
    for number in nums:
        value = abs(number)
        marker = value - 1
        if nums[marker] < 0:
            duplicates.append(value)
        else:
            nums[marker] = -nums[marker]
    return duplicates
