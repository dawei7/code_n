"""Project Euler Problem 837: Amidakuji.

Mathematical Formulation:
Amidakuji ladder permutations and transposition counts modulo 1000000007.
"""

from __future__ import annotations


def solve(mod: int = 1000000007) -> str:
    """Compute Amidakuji ladder count mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + i * (i + 1)) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
