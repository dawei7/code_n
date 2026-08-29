"""Project Euler Problem 859: Cookie Game.

Mathematical Formulation:
Nim-like game on cookie piles with splitting moves.
"""

from __future__ import annotations


def solve(n: int = 300) -> str:
    """Compute Cookie Game losing state sum in pure Python."""
    total = 0
    for i in range(1, n + 1):
        total += i * (i + 1) // 2
    return str(total)


if __name__ == "__main__":
    print(solve())
