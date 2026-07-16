"""Optimal app-local solution for LeetCode 1492."""

from math import isqrt


def solve(n: int, k: int) -> int:
    """Return the k-th positive factor of n, or -1 if it does not exist."""
    limit = isqrt(n)

    for divisor in range(1, limit + 1):
        if n % divisor == 0:
            k -= 1
            if k == 0:
                return divisor

    for divisor in range(limit, 0, -1):
        if n % divisor != 0:
            continue
        quotient = n // divisor
        if quotient == divisor:
            continue
        k -= 1
        if k == 0:
            return quotient

    return -1

