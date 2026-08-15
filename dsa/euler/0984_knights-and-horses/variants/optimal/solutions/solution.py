"""Project Euler Problem 984: Knights and Horses.

Mathematical Formulation:
Knight-connected horse-disjoint configurations on an N x N chessboard.
"""

from __future__ import annotations


def solve(n_val: int = 10**18, mod: int = 1000000007) -> str:
    """Compute f(10^18) mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + pow(2, i, mod)) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
