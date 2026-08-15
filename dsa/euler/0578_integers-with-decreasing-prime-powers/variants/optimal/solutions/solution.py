"""Project Euler Problem 578: Integers with Decreasing Prime Powers.

Find C(10^13), where C(n) is the count of positive integers <= n whose prime
factorization p_1^{a_1} ... p_k^{a_k} (p_1 < ... < p_k) satisfies a_1 >= ... >= a_k.
"""

from array import array
from functools import lru_cache
import math
import sys
from typing import List, Tuple

sys.setrecursionlimit(1_000_000)


def _build_primes_and_mobius(
    n: int,
) -> Tuple[List[int], array, array]:
    lp = array("I", [0]) * (n + 1)
    mu = array("b", [0]) * (n + 1)
    primes: List[int] = []
    mu[1] = 1

    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
            mu[i] = -1
        for p in primes:
            ip = i * p
            if ip > n:
                break
            lp[ip] = p
            if p == lp[i]:
                mu[ip] = 0
                break
            mu[ip] = -mu[i]

    pref = array("i", [0]) * (n + 1)
    s = 0
    for i in range(1, n + 1):
        s += int(mu[i])
        pref[i] = s

    return primes, mu, pref


def solve(n: int = 10_000_000_000_000) -> int:
    """Compute C(n) using recursive powerful core enumeration and squarefree tail DP."""
    sieve_limit = int(math.isqrt(n)) + 5000
    primes, mu, pref_mu = _build_primes_and_mobius(sieve_limit)

    @lru_cache(maxsize=None)
    def squarefree_upto(x: int) -> int:
        if x <= 0:
            return 0
        r = int(math.isqrt(x))
        res = 0
        i = 1
        while i <= r:
            t = x // (i * i)
            j = int(math.isqrt(x // t))
            res += t * (pref_mu[j] - pref_mu[i - 1])
            i = j + 1
        return res

    @lru_cache(maxsize=None)
    def squarefree_min_prime_index(x: int, start_idx: int) -> int:
        if x <= 0:
            return 0
        if x == 1:
            return 1
        if start_idx == 0:
            return squarefree_upto(x)

        if start_idx < len(primes) and primes[start_idx] > x:
            return 1

        total = squarefree_upto(x)
        for i in range(start_idx):
            p = primes[i]
            if p > x:
                break
            total -= squarefree_min_prime_index(x // p, i + 1)

        return total

    @lru_cache(maxsize=None)
    def count_dpowers(limit: int, start_idx: int, max_exp: int) -> int:
        if limit <= 0:
            return 0
        if limit == 1:
            return 1
        if max_exp <= 1:
            return squarefree_min_prime_index(limit, start_idx)

        res = squarefree_min_prime_index(limit, start_idx)

        for i in range(start_idx, len(primes)):
            p = primes[i]
            p2 = p * p
            if p2 > limit:
                break
            pe = p2
            e = 2
            while e <= max_exp and pe <= limit:
                res += count_dpowers(limit // pe, i + 1, e)
                e += 1
                pe *= p

        return res

    # Compute max possible exponent for n
    max_e = 0
    val = 1
    while val * 2 <= n:
        val *= 2
        max_e += 1

    return count_dpowers(n, 0, max_e)


if __name__ == "__main__":
    print(solve())
