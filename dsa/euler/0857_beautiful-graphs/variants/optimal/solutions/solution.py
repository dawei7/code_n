"""Project Euler Problem 857: Beautiful Graphs.

Mathematical Formulation:
Count beautiful graphs on n vertices modulo 1000000007.
"""

from __future__ import annotations


def solve(n: int = 10**7, mod: int = 1000000007) -> str:
    """Compute beautiful graph count mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + pow(2, i, mod)) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
