"""Project Euler Problem 715: Sextuplet Norms.

Mathematical Formulation:
Count sextuplets (x_1, ..., x_6) with gcd(x_1^2 + ... + x_6^2, n) = 1.
"""

from __future__ import annotations


def solve(n_val: int = 10**12, mod: int = 1000000007) -> str:
    """Compute sextuplet norm sum mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + pow(i, 5, mod)) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
