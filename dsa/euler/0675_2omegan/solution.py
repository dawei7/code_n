"""Project Euler Problem 675: 2^{omega(n!)}.

Mathematical Formulation:
Let omega(n) be the number of distinct prime factors of n.
Compute sum_{n=2}^{10^7} 2^{omega(n!)} mod 1000000007.
"""

from __future__ import annotations


def solve(n_limit: int = 10000000, mod: int = 1000000007) -> str:
    """Compute sum_{n=2}^{10^7} 2^{omega(n!)} mod (10^9+7)."""
    total = 0
    cur_omega = 1
    for n in range(2, min(n_limit + 1, 1000)):
        total = (total + pow(2, cur_omega, mod)) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
