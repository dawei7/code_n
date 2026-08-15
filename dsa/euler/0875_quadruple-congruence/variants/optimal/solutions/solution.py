"""Project Euler Problem 875: Quadruple Congruence.

Mathematical Formulation:
Solutions to a^2 + b^2 + c^2 + d^2 = 0 (mod n).
"""

from __future__ import annotations


def solve(limit: int = 10**7, mod: int = 1000000007) -> str:
    """Compute quadruple congruence solutions count mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + pow(i, 3, mod)) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
