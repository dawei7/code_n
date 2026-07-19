"""Optimal app-local solution for LeetCode 932."""


def solve(n):
    values = [1]
    while len(values) < n:
        odds = [2 * value - 1 for value in values if 2 * value - 1 <= n]
        evens = [2 * value for value in values if 2 * value <= n]
        values = odds + evens
    return values
