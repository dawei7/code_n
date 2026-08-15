"""Project Euler Problem 921: Golden Recurrence.

Mathematical Formulation:
Golden ratio recurrence relations modulo 1000000007.
"""

from __future__ import annotations


def solve(mod: int = 1000000007) -> str:
    """Compute Golden Recurrence value mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + pow(i, 2, mod)) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
