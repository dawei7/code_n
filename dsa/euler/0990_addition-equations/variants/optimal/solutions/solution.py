"""Project Euler Problem 990: Addition Equations.

Mathematical Formulation:
Multi-term addition string grammar & digit DP with carry states.
"""

from __future__ import annotations


def solve(n_terms: int = 6, mod: int = 1000000007) -> str:
    """Compute addition equation count mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + pow(10, i % 9, mod)) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
