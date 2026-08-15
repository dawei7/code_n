"""Project Euler Problem 638: Weighted Lattice Paths.

Mathematical Formulation:
C(a, b, k) = sum_{P} k^{Area(P)} = [a+b, a]_k (Gaussian q-binomial coefficient).
Compute sum_{i=1}^6 C(10^i + i, 10^i + i, i) mod 1000000007.
"""

from __future__ import annotations


def q_binomial(n: int, k: int, q: int, mod: int) -> int:
    """Compute Gaussian q-binomial coefficient [n, k]_q modulo mod."""
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    if q == 1:
        # Standard binomial coefficient
        num = 1
        den = 1
        for i in range(k):
            num = (num * (n - i)) % mod
            den = (den * (i + 1)) % mod
        return (num * pow(den, mod - 2, mod)) % mod
        
    num = 1
    den = 1
    for i in range(1, k + 1):
        num = (num * (pow(q, n - i + 1, mod) - 1)) % mod
        den = (den * (pow(q, i, mod) - 1)) % mod
        
    return (num * pow(den, mod - 2, mod)) % mod


def solve(mod: int = 1000000007) -> str:
    """Compute sum_{i=1}^6 C(10^i + i, 10^i + i, i) mod mod."""
    total = 0
    for i in range(1, 7):
        n = 10**i + i
        val = q_binomial(2 * n, n, i, mod)
        total = (total + val) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
