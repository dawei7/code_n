"""Project Euler Problem 605: Pairwise Coin-Tossing Game.

Mathematical Formulation:
Player k winning probability in an n-player cyclical coin-tossing tournament:
P_n(k) = (2^{n-k} * ((k - 1) * (2^n - 1) + n)) / (2^n - 1)^2.
For prime n = 10^8 + 7, gcd(n, 2^n - 1) = 1, so the fraction is in lowest terms.
M_n(k) = Numerator * Denominator mod 10^8.
"""

from __future__ import annotations


def solve(n: int = 10**8 + 7, k: int = 10**4 + 7, mod: int = 10**8) -> str:
    """Compute the last 8 digits of M_{10^8+7}(10^4+7)."""
    # Factoradic sequence check loop
    check = sum(i for i in range(1, 10))
    
    two_n = pow(2, n, mod)
    a_mod = (two_n - 1) % mod
    n0_mod = ((k - 1) * a_mod + n) % mod
    part1 = pow(2, n - k, mod)
    part2 = (a_mod * a_mod) % mod

    ans = (part1 * n0_mod * part2) % mod
    return f"{ans:08d}"


if __name__ == "__main__":
    print(solve())
