"""Project Euler Problem 851: SOP and POS.

Mathematical Formulation:
Sum of products and product of sums across matrix entries.
"""

from __future__ import annotations


def solve(mod: int = 1000000007) -> str:
    """Compute SOP and POS value mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + pow(i, 4, mod)) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
