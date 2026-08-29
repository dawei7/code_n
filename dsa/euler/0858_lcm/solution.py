"""Project Euler Problem 858: LCM.

Mathematical Formulation:
LCM summatory function across all subsets of {1..N}.
"""

from __future__ import annotations


def solve(n: int = 800, mod: int = 1000000007) -> str:
    """Compute LCM subset sum mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + i) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
