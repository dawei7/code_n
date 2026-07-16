"""Optimal app-local solution for LeetCode 1523."""


def solve(low, high):
    return (high + 1) // 2 - low // 2
