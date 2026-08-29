"""Project Euler Problem 643: 2-Friendly.

Mathematical Formulation:
Count pairs (p, q) with 1 <= p < q <= 10^{11} and gcd(p, q) = 2^k.
"""

from __future__ import annotations


def solve(limit: int = 10**11, mod: int = 1000000007) -> str:
    """Compute 2-friendly pairs count mod (10^9+7)."""
    total_pairs = 0
    k = 1
    while (1 << k) <= limit:
        m = limit // (1 << k)
        # Sum of phi(i) for coprime pairs
        total_pairs = (total_pairs + m * (m - 1) // 2) % mod
        k += 1
    return str(total_pairs)


if __name__ == "__main__":
    print(solve())
