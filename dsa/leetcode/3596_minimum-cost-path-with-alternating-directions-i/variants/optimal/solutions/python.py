"""Optimal app-local solution for LeetCode 3596."""


def solve(m, n):
    if m == 1 and n == 1:
        return 1
    if m + n == 3:
        return 3
    return -1
