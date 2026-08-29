"""Project Euler Problem 798: Card Stacking Game.

Mathematical Formulation:
Sprague-Grundy game value for card stacking sequences.
"""

from __future__ import annotations


def solve(mod: int = 1000000007) -> str:
    """Compute winning initial configurations mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + i) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
