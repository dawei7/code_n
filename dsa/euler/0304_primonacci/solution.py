"""Project Euler 304: Primonacci

Find sum_{n=1}^{100000} f(a(n)) mod 1234567891011, where a(n) are consecutive primes > 10^14.
"""

from __future__ import annotations

import math


def fib_doubling(n: int, mod: int) -> tuple[int, int]:
    """Computes (F(n), F(n + 1)) modulo mod in O(log n) time using fast doubling."""
    if n == 0:
        return 0, 1
    a, b = fib_doubling(n >> 1, mod)
    c = (a * ((2 * b - a) % mod)) % mod
    d = (a * a + b * b) % mod
    if n & 1:
        return d, (c + d) % mod
    return c, d


def solve(
    num_primes: int = 100_000,
    start: int = 10**14,
    mod: int = 1_234_567_891_011,
) -> str:
    """Calculates sum_{n=1}^{num_primes} F(a(n)) mod mod using a Segmented Sieve of Eratosthenes

    combined with linear Fibonacci streaming.
    """
    span = 4_000_000
    max_base = int(math.isqrt(start + span)) + 10

    # 1. Sieve base primes up to max_base (~10^7)
    sieve_base = [True] * (max_base + 1)
    sieve_base[0] = sieve_base[1] = False
    for i in range(2, int(math.isqrt(max_base)) + 1):
        if sieve_base[i]:
            sieve_base[i * i : max_base + 1 : i] = [False] * len(
                sieve_base[i * i : max_base + 1 : i]
            )
    base_primes = [i for i, is_p in enumerate(sieve_base) if is_p]

    # 2. Segmented sieve on [start + 1, start + span]
    seg_sieve = [True] * span
    for p in base_primes:
        first = ((start + 1 + p - 1) // p) * p
        if first < p * p:
            first = p * p
        offset = first - (start + 1)
        if offset < span:
            seg_sieve[offset : span : p] = [False] * len(
                seg_sieve[offset : span : p]
            )

    # 3. Compute initial Fibonacci pair F(start + 1), F(start + 2) mod mod
    f_k, f_k1 = fib_doubling(start + 1, mod)

    primes_found = 0
    total_sum = 0

    for i in range(span):
        if seg_sieve[i]:
            total_sum = (total_sum + f_k) % mod
            primes_found += 1
            if primes_found == num_primes:
                break
        f_k, f_k1 = f_k1, (f_k + f_k1) % mod

    return str(total_sum)


if __name__ == "__main__":
    print(solve())
