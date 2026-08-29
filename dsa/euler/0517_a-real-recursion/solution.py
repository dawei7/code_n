"""Project Euler Problem 517: A Real Recursion.

Find sum_{p in (10^7, 10^7 + 10^4), p prime} G(p) mod 1_000_000_007,
where G(n) = g_{sqrt(n)}(n) for the real-step recursion g_a(x) = g_a(x-1) + g_a(x-a).
"""

import math
from array import array
from typing import List, Tuple

MOD = 1_000_000_007
LOW = 10_000_000
HIGH = 10_010_000


def _precompute_factorials(n: int) -> Tuple[array, array]:
    fac = array("I", [0]) * (n + 1)
    invfac = array("I", [0]) * (n + 1)

    fac[0] = 1
    mod = MOD
    for i in range(1, n + 1):
        fac[i] = (fac[i - 1] * i) % mod

    invfac[n] = pow(fac[n], mod - 2, mod)
    for i in range(n, 0, -1):
        invfac[i - 1] = (invfac[i] * i) % mod

    return fac, invfac


def _comb(n: int, k: int, fac: array, invfac: array) -> int:
    if k < 0 or k > n:
        return 0
    mod = MOD
    return (fac[n] * invfac[k] % mod) * invfac[n - k] % mod


def _primes_in_open_interval(lo: int, hi: int) -> List[int]:
    start = lo + 1
    end = hi
    limit = math.isqrt(end) + 1

    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    r = math.isqrt(limit)
    for i in range(2, r + 1):
        if sieve[i]:
            step = i
            begin = i * i
            sieve[begin : limit + 1 : step] = b"\x00" * (
                ((limit - begin) // step) + 1
            )
    base_primes = [i for i in range(2, limit + 1) if sieve[i]]

    seg = bytearray(b"\x01") * (end - start)
    for p in base_primes:
        first = ((start + p - 1) // p) * p
        for x in range(first, end, p):
            seg[x - start] = 0

    primes: List[int] = []
    for i, is_p in enumerate(seg):
        if is_p:
            val = start + i
            if val >= 2:
                primes.append(val)
    return primes


def g_eval(n: int, fac: array, invfac: array) -> int:
    """Evaluate G(n) = g_{sqrt(n)}(n) mod MOD using hockey-stick binomial summation."""
    a_floor = math.isqrt(n)
    isq = math.isqrt
    mod = MOD

    u = [0] * (a_floor + 3)
    for m in range(1, a_floor + 2):
        u[m] = n - isq(m * m * n) - 1

    ans = 0

    for m in range(1, a_floor + 1):
        c = u[m]
        i = m - 1
        ans += _comb(c + i, i, fac, invfac)

    for c in range(0, a_floor):
        upper = u[c + 1]
        if upper < 0:
            continue
        lower = u[c + 2] + 1
        if lower < 0:
            lower = 0
        if lower > upper:
            continue

        ans += _comb(c + upper + 1, c + 1, fac, invfac)
        if lower > 0:
            ans -= _comb(c + lower, c + 1, fac, invfac)

    return ans % mod


def solve(lo: int = LOW, hi: int = HIGH, mod: int = MOD) -> int:
    """Compute sum_{p prime in (lo, hi)} G(p) mod mod using segmented sieve and hockey-stick summation."""
    fac, invfac = _precompute_factorials(hi)
    primes = _primes_in_open_interval(lo, hi)
    total = 0

    for p in primes:
        total = (total + g_eval(p, fac, invfac)) % mod

    return total


if __name__ == "__main__":
    print(solve())
