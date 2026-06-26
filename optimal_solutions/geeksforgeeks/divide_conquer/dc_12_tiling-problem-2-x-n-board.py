"""Optimal solution for dc_12: Tiling Problem (2 x N board).

Given a 2 x n board and tiles of size 2 x 1, count
"""


def solve(n):
    """Count the tilings of a 2 x n board with 2 x 1 dominoes.

    T(n) = T(n-1) + T(n-2), T(0) = 1, T(1) = 1 (Fibonacci).
    """
    if n <= 1:
        return 1
    a, b = 1, 1   # T(0), T(1)
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
