"""Project Euler Problem 545: Faulhaber's Formulas.

Find F(10^5), where F(m) is the m-th positive integer k such that D(k) = 20010,
and D(k) is the denominator of the linear Faulhaber coefficient a_1 = (-1)^k B_k.
"""

from __future__ import annotations

from math import gcd, isqrt
from typing import List, Set

TARGET_PRIMES: Set[int] = {2, 3, 5, 23, 29}
L = 308  # lcm(p-1 for p in TARGET_PRIMES) = lcm(1, 2, 4, 22, 28)


def _primes_upto(n: int) -> List[int]:
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            step = p
            start = p * p
            sieve[start : n + 1 : step] = b"\x00" * (
                ((n - start) // step) + 1
            )
    return [i for i, v in enumerate(sieve) if v]


def _divisors(n: int) -> List[int]:
    ds = []
    r = isqrt(n)
    for d in range(1, r + 1):
        if n % d == 0:
            ds.append(d)
            if d * d != n:
                ds.append(n // d)
    ds.sort()
    return ds


def solve(target_index: int = 100_000) -> int:
    """Compute F(target_index) using von Staudt-Clausen divisor progression sieve."""
    limit_n = 4_000_000
    invalid = bytearray(limit_n + 1)
    invalid[0] = 1

    g_divs = _divisors(L)
    max_p = max(g_divs) * limit_n + 1
    small_primes = _primes_upto(isqrt(max_p) + 1)

    for g in g_divs:
        p_max = g * limit_n + 1
        lim = isqrt(p_max)

        isprime_m = bytearray(b"\x01") * (limit_n + 1)
        isprime_m[0] = 0

        for q in small_primes:
            if q > lim:
                break
            if g % q == 0:
                continue

            inv = pow(g, -1, q)
            m0 = (-inv) % q
            if m0 == 0:
                m0 = q

            if g * m0 + 1 == q:
                m0 += q

            if m0 <= limit_n:
                isprime_m[m0 : limit_n + 1 : q] = b"\x00" * (
                    ((limit_n - m0) // q) + 1
                )

        b = L // g
        for m in range(1, limit_n + 1):
            if not isprime_m[m]:
                continue

            p = g * m + 1
            if p in TARGET_PRIMES:
                continue

            f = m // gcd(m, b)
            if f <= 1 or invalid[f]:
                continue

            invalid[f : limit_n + 1 : f] = b"\x01" * (((limit_n - f) // f) + 1)

    count = 0
    answer = None
    for n in range(1, limit_n + 1):
        if invalid[n]:
            continue
        count += 1
        if count == target_index:
            answer = L * n
            break

    assert answer is not None, "Search bound was too small"
    return answer


if __name__ == "__main__":
    print(solve())
