"""Optimal app-local solution for LeetCode 974."""


def solve(nums, k):
    frequencies = [0] * k
    frequencies[0] = 1
    prefix = 0
    answer = 0

    for value in nums:
        prefix = (prefix + value) % k
        answer += frequencies[prefix]
        frequencies[prefix] += 1

    return answer
