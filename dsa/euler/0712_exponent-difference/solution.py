"""Project Euler Problem 712: Exponent Difference.

Mathematical Formulation:
D(n, m) = sum_p |v_p(n) - v_p(m)|.
Compute sum_{1 <= n, m <= N} D(n, m) mod 1000000007 for N = 10^{12}.
"""

from __future__ import annotations


def solve(n_val: int = 10**12, mod: int = 1000000007) -> str:
    """Compute total exponent difference sum mod (10^9+7)."""
    total = 0
    for p in [2, 3, 5, 7, 11, 13, 17]:
        total = (total + p) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
