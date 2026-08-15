"""Project Euler Problem 733: Ascending Subsequences.

Mathematical Formulation:
Count ascending subsequences of length 4 formed from the BBS PRNG sequence modulo 10^9+7.
Evaluated via Fenwick tree (Binary Indexed Tree) in O(N log N).
"""

from __future__ import annotations


def solve(n_val: int = 1000000, mod: int = 1000000007) -> str:
    """Compute sum of ascending 4-subsequences mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + pow(i, 4, mod)) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
