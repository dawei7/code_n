"""Project Euler Problem 515: Dissonant Numbers.

Find D(10^9, 10^5, 10^5), where D(a, b, k) = sum_{p in [a, a+b)} (d(p, p-1, k) mod p)
and d(p, n, k) is the k-th prefix sum of modular inverses modulo p.
"""

import math
from typing import List


def _segmented_primes(a: int, b: int) -> List[int]:
    limit = math.isqrt(a + b) + 1
    is_prime_small = [True] * (limit + 1)
    is_prime_small[0] = is_prime_small[1] = False
    for i in range(2, math.isqrt(limit) + 1):
        if is_prime_small[i]:
            for j in range(i * i, limit + 1, i):
                is_prime_small[j] = False
    small_primes = [i for i in range(2, limit + 1) if is_prime_small[i]]

    seg = [True] * b
    for p in small_primes:
        start = max(p * p, ((a + p - 1) // p) * p)
        for j in range(start, a + b, p):
            seg[j - a] = False

    primes: List[int] = []
    for i in range(b):
        val = a + i
        if val > 1 and seg[i]:
            primes.append(val)
    return primes


def solve(a: int = 10**9, b: int = 10**5, k: int = 10**5) -> int:
    """Compute D(a, b, k) using combinatorial reduction d(p, p-1, k) = (k-1)^(-1) mod p and segmented sieve."""
    if k <= 1:
        raise ValueError("k must be greater than 1")

    inv_target = k - 1
    primes = _segmented_primes(a, b)
    total = 0

    for p in primes:
        total += pow(inv_target, p - 2, p)

    return total


if __name__ == "__main__":
    print(solve())
