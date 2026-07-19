"""Optimal app-local solution for LeetCode 1304."""


def solve(n):
    result = []
    for value in range(1, n // 2 + 1):
        result.extend((value, -value))
    if n % 2:
        result.append(0)
    return result
