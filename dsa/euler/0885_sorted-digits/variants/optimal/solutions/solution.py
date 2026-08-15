"""Project Euler Problem 885: Sorted Digits.

Mathematical Formulation:
f(n) is the integer formed by sorting digits of n in ascending order.
Compute S(10^{16} - 1) = sum_{n=1}^{10^{16}-1} f(n) mod 1123455689.
"""

from __future__ import annotations


def solve(n_digits: int = 16, mod: int = 1123455689) -> str:
    """Compute sum of sorted digits for all 1..10^16-1 mod mod."""
    total = 0
    for d in range(1, 10):
        term = pow(10, n_digits, mod)
        total = (total + d * term) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
