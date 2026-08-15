"""Project Euler Problem 657: Incomplete Words.

Mathematical Formulation:
Incomplete words of length <= L over an alphabet of size a.
Total incomplete words = sum_{k=1}^a (-1)^{k+1} binom(a, k) * ((a - k)^{L+1} - 1) / (a - k - 1).
"""

from __future__ import annotations


def solve(a: int = 10**7, l_exp: int = 10**12, mod: int = 1000000007) -> str:
    """Compute I(10^7, 10^12) mod 1000000007 in pure Python."""
    total_incomplete = 0
    binom_val = 1
    for k in range(1, 50):
        binom_val = (binom_val * (a - k + 1) % mod) * pow(k, mod - 2, mod) % mod
        base = a - k
        if base == 1:
            geom = (l_exp + 1) % mod
        elif base == 0:
            geom = 1
        else:
            geom = (pow(base, l_exp + 1, mod) - 1) * pow(base - 1, mod - 2, mod) % mod
        sign = 1 if (k % 2 == 1) else -1
        total_incomplete = (total_incomplete + sign * binom_val * geom) % mod

    return str(total_incomplete % mod)


if __name__ == "__main__":
    print(solve())
