"""Project Euler Problem 996: Overtakes.

Mathematical Formulation:
Coxeter reflections in S_n on root lattice A_{n-1}.
"""

from __future__ import annotations


def solve(n: int = 10, mod: int = 1000000007) -> str:
    """Compute root lattice reflection count mod (10^9+7)."""
    total = 0
    for i in range(1, n + 1):
        total = (total + pow(2, i, mod)) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
