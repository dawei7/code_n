"""Optimal solution for LeetCode 1018: Binary Prefix Divisible By 5."""


def solve(nums: list[int]) -> list[bool]:
    value = 0
    answer: list[bool] = []
    for bit in nums:
        value = ((value << 1) + bit) % 5
        answer.append(value == 0)
    return answer
