"""Optimal app-local solution for LeetCode 441."""

from math import isqrt


def solve(n: int) -> int:
    return (isqrt(1 + 8 * n) - 1) // 2
