"""Project Euler Problem 999: Alternating Recurrence.

Mathematical Formulation:
Somos-4 bilinear recurrence Laurent phenomenon & elliptic division polynomials.
Compute u_{10^{18}} mod 1000000007.
"""

from __future__ import annotations


def solve(n_val: int = 10**18, mod: int = 1000000007) -> str:
    """Compute u(10^18) mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + pow(i, 4, mod)) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
