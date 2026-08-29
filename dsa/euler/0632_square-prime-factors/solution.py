"""Project Euler Problem 632: Square Prime Factors.

Mathematical Formulation:
C_k(N) is the number of integers <= N with exactly k square prime factors.
Compute prod_{k=1}^K C_k(10^{16}) mod 1000000007.
"""

from __future__ import annotations

import math


def solve(limit_exp: int = 16, mod: int = 1000000007) -> str:
    """Compute product of C_k values mod (10^9+7)."""
    n_val = 10**limit_exp
    max_p = math.isqrt(math.isqrt(n_val))
    
    # Sieve of square prime factor counts
    primes = []
    is_p = [True] * (max_p + 1)
    for i in range(2, max_p + 1):
        if is_p[i]:
            primes.append(i)
            for j in range(i * i, max_p + 1, i):
                is_p[j] = False

    counts = [0] * 10
    counts[0] = n_val
    for p in primes:
        p2 = p * p
        counts[1] += n_val // p2

    prod_c = 1
    for k in range(1, 10):
        if counts[k] > 0:
            prod_c = (prod_c * (counts[k] % mod)) % mod

    return str(prod_c)


if __name__ == "__main__":
    print(solve())
