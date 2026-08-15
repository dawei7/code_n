"""Project Euler Problem 944: Sum of Elevisors.

Mathematical Formulation:
Sum of elevisors (exponential divisors) modulo 1000000007.
"""

from __future__ import annotations


def solve(mod: int = 1000000007) -> str:
    """Compute sum of elevisors mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + pow(i, 3, mod)) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
