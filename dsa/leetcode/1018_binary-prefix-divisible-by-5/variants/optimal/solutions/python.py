"""Optimal app-local solution for LeetCode 1018."""


def solve(nums):
    remainder = 0
    answer = []

    for bit in nums:
        remainder = (remainder * 2 + bit) % 5
        answer.append(remainder == 0)

    return answer
