"""Project Euler Problem 452: Long Products.

Find F(10^9, 10^9) mod 1234567891, where F(m, n) is the number of n-tuples
of positive integers whose product does not exceed m.
"""

from functools import lru_cache
from math import isqrt
from typing import Dict, List, Tuple

MOD = 1_234_567_891
SIEVE_MAX = 1_000_000


def _sieve(n: int) -> Tuple[List[int], List[int]]:
    is_p = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        is_p[0] = 0
    if n >= 1:
        is_p[1] = 0
    r = isqrt(n)
    for i in range(2, r + 1):
        if is_p[i]:
            step = i
            start = i * i
            is_p[start : n + 1 : step] = b"\x00" * (
                ((n - start) // step) + 1
            )
    primes = [i for i in range(2, n + 1) if is_p[i]]
    pi = [0] * (n + 1)
    c = 0
    for i in range(n + 1):
        if is_p[i]:
            c += 1
        pi[i] = c
    return primes, pi


PRIMES, PI_SMALL = _sieve(SIEVE_MAX)


def _iroot(n: int, k: int) -> int:
    if n < 2:
        return n
    lo, hi = 1, 1
    while hi**k <= n:
        hi *= 2
    lo = hi // 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**k <= n:
            lo = mid
        else:
            hi = mid
    return lo


@lru_cache(maxsize=None)
def _phi(x: int, a: int) -> int:
    if a == 0:
        return x
    if a == 1:
        return x - x // 2
    if a == 2:
        return x - x // 2 - x // 3 + x // 6
    return _phi(x, a - 1) - _phi(x // PRIMES[a - 1], a - 1)


@lru_cache(maxsize=None)
def _prime_pi(n: int) -> int:
    if n < SIEVE_MAX:
        return PI_SMALL[n]
    a = _prime_pi(_iroot(n, 4))
    b = _prime_pi(isqrt(n))
    c = _prime_pi(_iroot(n, 3))
    res = _phi(n, a) + ((b + a - 2) * (b - a + 1)) // 2
    for i in range(a, b):
        p = PRIMES[i]
        w = n // p
        res -= _prime_pi(w)
        if i < c:
            lim = _prime_pi(isqrt(w))
            for j in range(i, lim):
                res -= _prime_pi(w // PRIMES[j]) - j
    return res


def _weights_for_n(n: int) -> List[int]:
    max_e = n.bit_length() - 1
    w = [1] * (max_e + 1)
    cur = 1
    for e in range(1, max_e + 1):
        cur = (cur * ((n + e - 1) % MOD)) % MOD
        cur = (cur * pow(e, MOD - 2, MOD)) % MOD
        w[e] = cur
    return w


def solve(n: int = 1_000_000_000) -> int:
    """Compute F(n, n) mod MOD using prime power recursion and Lehmer prime counting."""
    w = _weights_for_n(n)
    w1 = w[1]
    max_e = len(w) - 1

    s_cache: Dict[Tuple[int, int], int] = {}

    def s_func(limit: int, idx: int) -> int:
        if limit < 2:
            return 1
        if idx >= len(PRIMES) or PRIMES[idx] > limit:
            return 1

        state = (limit, idx)
        if state in s_cache:
            return s_cache[state]

        p0 = PRIMES[idx]
        if p0 * p0 > limit:
            cnt = _prime_pi(limit) - _prime_pi(p0 - 1)
            res = (1 + (cnt % MOD) * w1) % MOD
            s_cache[state] = res
            return res

        res = 1
        root = isqrt(limit)
        cnt_large = _prime_pi(limit) - _prime_pi(root)
        res = (res + (cnt_large % MOD) * w1) % MOD

        i = idx
        while i < len(PRIMES):
            p = PRIMES[i]
            if p > root:
                break
            pe = p
            e = 1
            while pe <= limit:
                res = (res + w[e] * s_func(limit // pe, i + 1)) % MOD
                e += 1
                if e > max_e:
                    break
                pe *= p
            i += 1

        s_cache[state] = res
        return res

    return s_func(n, 0)


if __name__ == "__main__":
    print(solve())
