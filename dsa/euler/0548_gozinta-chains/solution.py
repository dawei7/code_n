"""Project Euler Problem 548: Gozinta Chains.

Find the sum of all n <= 10^16 for which g(n) = n, where g(n) is the number of gozinta chains for n.
"""

from __future__ import annotations

import math
from typing import Dict, Iterator, List, Optional, Tuple

LIMIT = 10**16
MAX_EXP_SUM = LIMIT.bit_length()


def _primes_upto(n: int) -> List[int]:
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            step = p
            start = p * p
            sieve[start : n + 1 : step] = b"\x00" * (
                ((n - start) // step) + 1
            )
    return [i for i in range(n + 1) if sieve[i]]


SMALL_PRIMES = _primes_upto(100000)
FIRST_PRIMES = SMALL_PRIMES[:60]
_MR_BASES_64 = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)


def _is_probable_prime(n: int) -> bool:
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small:
        if n == p:
            return True
        if n % p == 0:
            return False

    d = n - 1
    s = 0
    while (d & 1) == 0:
        s += 1
        d >>= 1

    for a in _MR_BASES_64:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


_rng_state = 0x9E3779B97F4A7C15


def _rand64() -> int:
    global _rng_state
    x = _rng_state & ((1 << 64) - 1)
    x ^= (x >> 12) & ((1 << 64) - 1)
    x ^= (x << 25) & ((1 << 64) - 1)
    x ^= (x >> 27) & ((1 << 64) - 1)
    _rng_state = x
    return (x * 2685821657736338717) & ((1 << 64) - 1)


def _pollard_rho(n: int) -> int:
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    while True:
        c = (_rand64() % (n - 1)) + 1
        x = _rand64() % n
        y = x

        def f(v: int) -> int:
            return (v * v + c) % n

        d = 1
        while d == 1:
            x = f(x)
            y = f(f(y))
            d = math.gcd(abs(x - y), n)
        if d != n:
            return d


def _factorize(n: int, out: Dict[int, int]) -> None:
    if n == 1:
        return
    if _is_probable_prime(n):
        out[n] = out.get(n, 0) + 1
        return

    for p in SMALL_PRIMES[:2000]:
        if p * p > n:
            break
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out[p] = out.get(p, 0) + e
            _factorize(n, out)
            return

    if n == 1:
        return
    if _is_probable_prime(n):
        out[n] = out.get(n, 0) + 1
        return

    d = _pollard_rho(n)
    _factorize(d, out)
    _factorize(n // d, out)


def _prime_signature(n: int) -> Tuple[int, ...]:
    if n == 1:
        return ()
    fac: Dict[int, int] = {}
    _factorize(n, fac)
    return tuple(sorted(fac.values(), reverse=True))


_MAX_N = 2 * MAX_EXP_SUM + 2
_COMB = [[0] * (_MAX_N + 1) for _ in range(_MAX_N + 1)]
for _n in range(_MAX_N + 1):
    _COMB[_n][0] = 1
    for _k in range(1, _n + 1):
        _COMB[_n][_k] = (
            _COMB[_n - 1][_k - 1] + _COMB[_n - 1][_k] if _k < _n else 1
        )

_BINOM = [[0] * (MAX_EXP_SUM + 1) for _ in range(MAX_EXP_SUM + 1)]
for _n in range(MAX_EXP_SUM + 1):
    for _k in range(_n + 1):
        _BINOM[_n][_k] = _COMB[_n][_k]


def _gozinta_from_signature(
    sig: Tuple[int, ...], limit: Optional[int] = None
) -> int:
    s = sum(sig)
    if s == 0:
        return 1

    p_table = [0] * (s + 1)
    for t in range(1, s + 1):
        prod = 1
        tt = t - 1
        for a in sig:
            prod *= _COMB[a + t - 1][tt]
        p_table[t] = prod

    total = 0
    for m in range(1, s + 1):
        a_m = 0
        for t in range(1, m + 1):
            term = _BINOM[m][t] * p_table[t]
            if (m - t) & 1:
                a_m -= term
            else:
                a_m += term
        total += a_m
        if limit is not None and total > limit:
            return limit + 1
    return total


def _generate_signatures(
    max_sum: int, limit: int
) -> Iterator[Tuple[int, ...]]:
    sig: List[int] = []

    def rec(
        pos: int, prev_e: int, sum_used: int, prod: int
    ) -> Iterator[Tuple[int, ...]]:
        if sig:
            yield tuple(sig)
        if sum_used == max_sum or pos >= len(FIRST_PRIMES):
            return

        p = FIRST_PRIMES[pos]
        max_e = min(prev_e, max_sum - sum_used)

        power = p
        for e in range(1, max_e + 1):
            new_prod = prod * power
            if new_prod > limit:
                break
            sig.append(e)
            yield from rec(pos + 1, e, sum_used + e, new_prod)
            sig.pop()
            power *= p

    yield from rec(0, max_sum, 0, 1)


def solve(limit: int = LIMIT) -> int:
    """Find the sum of all n <= limit for which g(n) = n by signature enumeration."""
    solutions = [1]

    for sig in _generate_signatures(MAX_EXP_SUM, limit):
        g = _gozinta_from_signature(sig, limit=limit)
        if g > limit:
            continue
        if _prime_signature(g) == sig:
            solutions.append(g)

    return sum(sorted(set(solutions)))


if __name__ == "__main__":
    print(solve())
