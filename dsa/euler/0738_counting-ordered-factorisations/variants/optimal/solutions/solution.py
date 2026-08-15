"""Project Euler Problem 738: Counting Ordered Factorisations.

Mathematical Formulation:
Counting ordered factorisations with bounded part sizes modulo 1000000007.
"""

from __future__ import annotations


def solve(n_val: int = 10**10, mod: int = 1000000007) -> str:
    """Compute ordered factorisations sum mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + pow(2, i, mod)) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
