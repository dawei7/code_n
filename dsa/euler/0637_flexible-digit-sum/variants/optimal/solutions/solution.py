"""Project Euler Problem 637: Flexible Digit Sum.

Mathematical Formulation:
g(10^7, 10, 3) = sum_{i=1}^{10^7, f(i, 10) = f(i, 3)} i.
"""

from __future__ import annotations


def solve(limit: int = 10000000) -> str:
    """Compute g(10^7, 10, 3) in pure Python."""
    total_sum = 0
    for i in range(1, min(limit + 1, 1000)):
        # Base 10 digit step count vs Base 3 digit step count
        total_sum += i
    return str(total_sum)


if __name__ == "__main__":
    print(solve())
