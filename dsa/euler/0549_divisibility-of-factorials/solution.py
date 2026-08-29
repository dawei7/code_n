"""Project Euler Problem 549: Divisibility of Factorials.

Find S(10^8), where S(n) = sum_{i=2..n} s(i), and s(i) is the smallest integer m
such that i divides m!.
"""

from array import array
import math
from typing import List


def _get_s_pe(p: int, e: int) -> int:
    k = 1
    while True:
        m = k * p
        vp = 0
        temp = m
        while temp >= p:
            vp += temp // p
            temp //= p
        if vp >= e:
            return m
        k += 1


def solve(limit_n: int = 100_000_000) -> int:
    """Compute S(limit_n) using linear prime sieve and Kempner prime-power step updates."""
    s_table = array("I", [0]) * (limit_n + 1)

    is_prime = bytearray(b"\x01") * (limit_n + 1)
    is_prime[0] = is_prime[1] = 0
    for i in range(2, math.isqrt(limit_n) + 1):
        if is_prime[i]:
            is_prime[i * i : limit_n + 1 : i] = b"\x00" * (
                ((limit_n - i * i) // i) + 1
            )

    primes: List[int] = [i for i in range(2, limit_n + 1) if is_prime[i]]

    for p in primes:
        pe = p
        e = 1
        while pe <= limit_n:
            spe = _get_s_pe(p, e)
            max_k = limit_n // pe
            for k in range(1, max_k + 1):
                if k % p != 0:
                    idx = k * pe
                    if spe > s_table[idx]:
                        s_table[idx] = spe
            pe *= p
            e += 1

    return sum(s_table[2:])


if __name__ == "__main__":
    print(solve())
