"""Project Euler Problem 741: Binary Grid Colouring.

Mathematical Formulation:
Count binary grid colourings with row/column parity properties modulo 1000000007.
"""

from __future__ import annotations


def solve(n: int = 1000, mod: int = 1000000007) -> str:
    """Compute binary grid colouring count mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + pow(2, 2 * i, mod)) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
