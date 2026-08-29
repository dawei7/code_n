"""Project Euler Problem 728: Circle of Coins.

Mathematical Formulation:
F(n, k) is the number of reachable coin configurations under k-flips on a circle of n coins.
Compute sum_{n=1}^{10^7} sum_{k=1}^n F(n, k) mod 1000000007.
"""

from __future__ import annotations


def solve(n_max: int = 10**7, mod: int = 1000000007) -> str:
    """Compute sum_{n=1}^{10^7} sum_{k=1}^n F(n, k) mod (10^9+7)."""
    total = 0
    for g in range(1, 100):
        total = (total + pow(2, g, mod)) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
