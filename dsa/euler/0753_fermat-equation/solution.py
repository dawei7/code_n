"""Project Euler Problem 753: Fermat Equation.

Find the sum of F(p) over all primes p < 6000000, where F(p) is the number of integer
solutions to a^3 + b^3 = c^3 (mod p) for 1 <= a, b, c < p.
"""

from array import array
import math


def _sieve_primes_upto(n: int) -> tuple[bytearray, list[int]]:
    if n < 2:
        return bytearray(b"\x00"), []

    size = (n // 2) + 1
    sieve_odd = bytearray(b"\x01") * size
    sieve_odd[0] = 0

    r = math.isqrt(n)
    for i in range(1, (r // 2) + 1):
        if sieve_odd[i]:
            p = 2 * i + 1
            start = (p * p) // 2
            sieve_odd[start::p] = b"\x00" * (((size - 1 - start) // p) + 1)

    primes = [2]
    primes.extend(2 * i + 1 for i in range(1, size) if sieve_odd[i])
    if primes and primes[-1] > n:
        primes.pop()
    return sieve_odd, primes


def _build_u_map(limit_inclusive: int, sieve_odd: bytearray) -> array:
    n = limit_inclusive
    n4 = 4 * n
    vmax = math.isqrt(n4 // 27)
    u_by_p = array("H", [0]) * (n + 1)

    for v in range(1, vmax + 1):
        base = 27 * v * v
        umax = math.isqrt(n4 - base)
        u = v & 1
        while u <= umax:
            p = (u * u + base) >> 2
            if p <= n and (p % 3 == 1):
                if p != 2 and (p & 1) and sieve_odd[p >> 1]:
                    if u_by_p[p] == 0:
                        u_by_p[p] = u
            u += 2
    return u_by_p


def solve(limit_exclusive: int = 6_000_000) -> int:
    """Compute sum_{p < limit} F(p) using CM elliptic curve trace 4p = u^2 + 27v^2."""
    if limit_exclusive <= 2:
        return 0

    max_p = limit_exclusive - 1
    sieve_odd, primes = _sieve_primes_upto(max_p)
    u_by_p = _build_u_map(max_p, sieve_odd)

    total = 0
    for p in primes:
        if p == 2:
            continue
        elif p == 3:
            total += 2
        elif p % 3 == 2:
            total += (p - 1) * (p - 2)
        else:
            u = u_by_p[p]
            ap = u if (u % 3) == 2 else -u
            total += (p - 1) * (p - ap - 8)

    return total


if __name__ == "__main__":
    print(solve())
