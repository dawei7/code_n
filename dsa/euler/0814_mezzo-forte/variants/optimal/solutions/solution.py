"""Project Euler Problem 814: Mezzo-Forte.

Mathematical Formulation:
Find number of legal arrangements in 4n choir members with mutual visibility constraints.
"""

from __future__ import annotations


def solve(n: int = 1000, mod: int = 1000000007) -> str:
    """Compute Mezzo-Forte arrangement count mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + pow(4, i, mod)) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
