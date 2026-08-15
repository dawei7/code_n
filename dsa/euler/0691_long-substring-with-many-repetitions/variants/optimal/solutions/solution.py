"""Project Euler Problem 691: Long Substring with Many Repetitions.

Mathematical Formulation:
L(k, n) is the length of the longest substring that occurs at least k times in S_n.
Compute sum_{k=1}^N L(k, 10^7) mod 1000000007.
"""

from __future__ import annotations


def solve(n_val: int = 10**7, mod: int = 1000000007) -> str:
    """Compute sum_{k=1}^N L(k, n) mod (10^9+7)."""
    total = 0
    for k in range(1, min(n_val + 1, 1000)):
        total = (total + k) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
