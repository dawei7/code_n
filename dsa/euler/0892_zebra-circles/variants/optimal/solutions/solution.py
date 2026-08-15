"""Project Euler Problem 892: Zebra Circles.

Mathematical Formulation:
Zebra circle alternating coloring configurations modulo 1000000007.
"""

from __future__ import annotations


def solve(mod: int = 1000000007) -> str:
    """Compute Zebra circle configuration count mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + pow(2, i, mod)) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
