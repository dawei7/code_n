"""Project Euler Problem 484: Arithmetic Derivative.

Find sum_{1 < k <= 5*10^15} gcd(k, k'), where k' is the arithmetic derivative of k.
"""

from math import isqrt
import sys
from typing import List


def _primes_upto(n: int) -> List[int]:
    if n < 2:
        return []
    size = n // 2 + 1
    sieve = bytearray(b"\x01") * size
    sieve[0] = 0

    limit = isqrt(n)
    for p in range(3, limit + 1, 2):
        if sieve[p // 2]:
            start = (p * p) // 2
            sieve[start::p] = b"\x00" * ((size - start - 1) // p + 1)

    primes = [2]
    for i in range(1, size):
        if sieve[i]:
            primes.append(2 * i + 1)
    return primes


def solve(limit_n: int = 5 * 10**15) -> int:
    """Compute sum_{1 < k <= limit_n} gcd(k, k') via powerful number Dirichlet convolution DFS."""
    sys.setrecursionlimit(10000)
    limit = isqrt(limit_n)
    primes = _primes_upto(limit)
    plen = len(primes)

    def dfs(i0: int, l0: int) -> int:
        res = 0
        for i in range(i0, plen):
            p = primes[i]
            q = p * p
            l_val = l0 // q
            if not l_val:
                break

            e = 1
            g = 1
            while l_val:
                gp = g
                e += 1
                if e != 1:
                    if e == p:
                        g *= q
                        e = 0
                    else:
                        g *= p
                    c = g - gp
                    res += c * l_val
                    if l_val > q:
                        res += c * dfs(i + 1, l_val)
                l_val //= p

        return res

    return limit_n - 1 + dfs(0, limit_n)


if __name__ == "__main__":
    print(solve())
