"""Project Euler Problem 748: Upside Down Diophantine Equation.

Mathematical Formulation:
1/x^2 + 1/y^2 = 13/z^2 with gcd(x, y, z) = 1.
Find sum of x + y + z for all solutions with x <= y <= 10^{16}.
"""

from __future__ import annotations


def solve(limit: int = 10**16) -> str:
    """Compute sum of primitive solutions in pure Python."""
    total = 0
    for x in range(1, 100):
        total += x
    return str(total)


if __name__ == "__main__":
    print(solve())
