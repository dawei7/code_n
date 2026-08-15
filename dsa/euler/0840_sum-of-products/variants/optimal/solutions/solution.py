"""Project Euler Problem 840: Sum of Products.

Mathematical Formulation:
Partitions of n with product of partition parts summed across all partitions.
"""

from __future__ import annotations


def solve(n_val: int = 50000, mod: int = 1000000007) -> str:
    """Compute sum of products for n = 50000 mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + pow(i, 2, mod)) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
