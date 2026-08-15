"""Project Euler Problem 702: Jumping Flea.

Find S(123456789), where S(N) is the sum of minimum jumps J(T) for all upper-pointing
equilateral triangles in the upper half of a hexagon table of side length N.
"""

from typing import Dict, Tuple


def _inv_count_mod_mult(x: int, m: int, memo: Dict[Tuple[int, int], int]) -> int:
    """Number of inversions in the permutation a*x mod m for a=1..m-1 via Euclidean recursion."""
    if m <= 2:
        return 0

    x %= m
    if x <= 1:
        return 0
    if x == m - 1:
        return (m - 1) * (m - 2) // 2

    key = (x, m)
    if key in memo:
        return memo[key]

    t = m // x
    y = m - t * x

    block = (t * (t + 1) // 2) * (x * (x - 1) // 2)
    res = (
        block
        + (t + 1) * _inv_count_mod_mult(x, y, memo)
        - t * _inv_count_mod_mult(x, x - y, memo)
    )

    memo[key] = res
    return res


def _g(x: int, m: int, memo: Dict[Tuple[int, int], int]) -> int:
    if m <= 2:
        return 0
    return (m - 1) * (m - 2) - _inv_count_mod_mult(x, m, memo)


def solve(n: int = 123_456_789) -> int:
    """Compute S(N) using Euclidean modular inversion counting."""
    memo: Dict[Tuple[int, int], int] = {}
    d_bits = n.bit_length()

    base = (n * (3 * n + 1) // 2) * (d_bits + 1)
    total = base

    for d in range(2, d_bits + 1):
        total -= _g(n, 1 << d, memo)

    total += 2 * _g(n, (1 << d_bits) - n, memo)

    return total


if __name__ == "__main__":
    print(solve())
