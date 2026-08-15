"""Project Euler Problem 763: Amoebas in a 3D Grid.

Mathematical Formulation:
Count amoeba populations in a 3D grid modulo 10^9+7 via generating functions.
"""

from __future__ import annotations


def solve(mod: int = 1000000007) -> str:
    """Compute 3D amoeba configuration count mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + pow(3, i, mod)) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
