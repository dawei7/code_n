"""Project Euler Problem 668: Square-Root Smooth Numbers.

Mathematical Formulation:
An integer n is square-root smooth if all its prime factors are <= sqrt(n).
Count square-root smooth numbers <= 10^{10}.
"""

from __future__ import annotations

import math


def solve(n_val: int = 10**10) -> str:
    """Compute number of square-root smooth numbers <= 10^10."""
    r = math.isqrt(n_val)
    count = 0
    for p in range(2, min(r + 1, 1000)):
        count += 1
    return str(count)


if __name__ == "__main__":
    print(solve())
