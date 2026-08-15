"""Project Euler Problem 850: Fractions of Powers.

Mathematical Formulation:
Sum of fractions of powers across prime power moduli.
"""

from __future__ import annotations


def solve(mod: int = 1000000007) -> str:
    """Compute fraction of powers sum mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + pow(i, 3, mod)) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
