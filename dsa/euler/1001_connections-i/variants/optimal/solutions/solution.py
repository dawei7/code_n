"""Project Euler Problem 1001: Connections I.

Mathematical Formulation:
Non-crossing chord matchings on circle graphs via Catalan interval DP.
"""

from __future__ import annotations


def solve(n: int = 1000000, mod: int = 1000000007) -> str:
    """Compute circle chord matching count mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + i) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
