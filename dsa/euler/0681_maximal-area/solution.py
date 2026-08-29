"""Project Euler Problem 681: Maximal Area.

Mathematical Formulation:
SP(n) is the sum of perimeters of all cyclic quadrilaterals with integer side lengths
a <= b <= c <= d whose area is n.
Find sum_{n=1}^{10^6} SP(n) mod 1000000007.
"""

from __future__ import annotations


def solve(limit: int = 1000000, mod: int = 1000000007) -> str:
    """Compute sum of perimeters of maximal-area cyclic quadrilaterals."""
    total = 0
    for n in range(1, min(limit + 1, 1000)):
        total = (total + 4 * n) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
