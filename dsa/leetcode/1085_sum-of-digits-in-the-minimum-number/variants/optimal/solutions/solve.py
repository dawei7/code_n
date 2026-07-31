"""Optimal solution for LeetCode 1085: Sum of Digits in the Minimum Number."""


def solve(nums: list[int]) -> int:
    value = min(nums)
    digit_sum = 0
    while value:
        digit_sum += value % 10
        value //= 10
    return int(digit_sum % 2 == 0)
