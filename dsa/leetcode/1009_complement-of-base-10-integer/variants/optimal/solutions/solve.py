"""Optimal app-local solution for LeetCode 1009."""


def solve(n):
    if n == 0:
        return 1

    mask = 1
    while mask <= n:
        mask <<= 1
    return n ^ (mask - 1)
