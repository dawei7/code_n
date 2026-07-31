"""Optimal app-local solution for LeetCode 891."""


def solve(nums):
    modulus = 1_000_000_007
    ordered = sorted(nums)
    answer = 0
    power = 1

    for index, value in enumerate(ordered):
        answer += (value - ordered[-1 - index]) * power
        power = power * 2 % modulus

    return answer % modulus
