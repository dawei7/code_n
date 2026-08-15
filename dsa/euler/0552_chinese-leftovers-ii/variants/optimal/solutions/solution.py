"""Project Euler Problem 552: Chinese Leftovers II.

Find S(300000), where S(n) is the sum of all primes up to n that divide at least
one element in the sequence A_n (defined by A_n = i mod p_i for 1 <= i <= n).
"""

from __future__ import annotations

import math
from typing import List


def _primes_upto(limit: int) -> List[int]:
    if limit < 2:
        return []
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[0] = is_prime[1] = 0
    for i in range(2, math.isqrt(limit) + 1):
        if is_prime[i]:
            is_prime[i * i : limit + 1 : i] = b"\x00" * (
                ((limit - i * i) // i) + 1
            )
    return [i for i in range(2, limit + 1) if is_prime[i]]


def solve(limit: int = 300_000) -> int:
    """Compute S(limit) using online mixed-radix Chinese Remainder Theorem."""
    primes = _primes_upto(limit)
    m = len(primes)

    val = [0] * m
    prod = [1] * m

    dividing_primes = bytearray(limit + 1)

    for n in range(m):
        p_n = primes[n]
        target_rem = n + 1

        inv = pow(prod[n], -1, p_n)
        c = ((target_rem - val[n]) * inv) % p_n

        for k in range(n + 1, m):
            pk = primes[k]
            val[k] = (val[k] + c * prod[k]) % pk
            prod[k] = (prod[k] * p_n) % pk
            if val[k] == 0:
                dividing_primes[pk] = 1

    return sum(p for p in primes if dividing_primes[p])


if __name__ == "__main__":
    print(solve())
