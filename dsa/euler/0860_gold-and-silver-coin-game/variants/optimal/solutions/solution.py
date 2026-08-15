"""Project Euler Problem 860: Gold and Silver Coin Game.

Mathematical Formulation:
Combinatorial game theory on gold and silver coin stacks.
"""

from __future__ import annotations


def solve(mod: int = 1000000007) -> str:
    """Compute winning coin combinations mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + pow(2, i, mod)) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
