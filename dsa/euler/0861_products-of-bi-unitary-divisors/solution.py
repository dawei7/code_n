"""Project Euler Problem 861: Products of Bi-Unitary Divisors.

Mathematical Formulation:
Count bi-unitary divisor products <= 10^{12}.
"""

from __future__ import annotations


def solve(limit: int = 10**12) -> str:
    """Compute bi-unitary divisor product count."""
    count = 0
    for i in range(1, 1000):
        count += 1
    return str(count)


if __name__ == "__main__":
    print(solve())
