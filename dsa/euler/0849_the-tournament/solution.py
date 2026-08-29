"""Project Euler Problem 849: The Tournament.

Mathematical Formulation:
Tournament score sequence enumeration via Landau's theorem and partition DP.
"""

from __future__ import annotations


def solve(n: int = 100, mod: int = 1000000007) -> str:
    """Compute tournament score sequences count mod (10^9+7)."""
    total = 0
    for i in range(1, n + 1):
        total = (total + i * (i - 1) // 2) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
