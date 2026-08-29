"""Project Euler Problem 603: Substring Sums of Prime Concatenations.

Find S(C(10^6, 10^12)) mod 1000000007, where S(s) is the sum of all contiguous
substrings formed from the digit string s, and C(n, k) concatenates k copies of the first n primes.
"""

import math
from typing import List

_MOD = 1000000007


def _sieve_primes(n: int) -> List[int]:
    if n < 6:
        limit = 15
    else:
        limit = int(n * (math.log(n) + math.log(math.log(n))) + 10)
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(math.isqrt(limit)) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (
                ((limit - p * p) // p) + 1
            )
    primes = [i for i in range(2, limit + 1) if sieve[i]]
    return primes[:n]


def _geom_sum(r: int, k: int, mod: int) -> int:
    if r == 1:
        return k % mod
    return (pow(r, k, mod) - 1) * pow(r - 1, mod - 2, mod) % mod


def _geom_sum_b(r: int, k: int, mod: int) -> int:
    if r == 1:
        return ((k - 1) * k // 2) % mod
    num = ((k - 1) * pow(r, k + 1, mod) - k * pow(r, k, mod) + r) % mod
    den = pow(r - 1, 2, mod)
    return num * pow(den, mod - 2, mod) % mod


def solve(n: int = 1_000_000, k: int = 1_000_000_000_000) -> int:
    """Compute S(C(n, k)) modulo 1000000007 using digit-contribution linearity and geometric progressions."""
    primes = _sieve_primes(n)
    digits: List[int] = []
    for p in primes:
        for ch in str(p):
            digits.append(int(ch))

    l_p = len(digits)
    a_sum = 0
    b_sum = 0
    c_sum = 0
    d_sum = 0
    pow10 = 10

    for m in range(l_p, 0, -1):
        d = digits[m - 1]
        a_sum = (a_sum + d * pow10) % _MOD
        b_sum = (b_sum + d * m % _MOD * pow10) % _MOD
        c_sum = (c_sum + d) % _MOD
        d_sum = (d_sum + d * m) % _MOD
        pow10 = (pow10 * 10) % _MOD

    r = pow(10, l_p, _MOD)
    g0 = _geom_sum(r, k, _MOD)
    g1 = ((k - 1) * g0 - _geom_sum_b(r, k, _MOD)) % _MOD

    k0 = k % _MOD
    k1 = (k * (k - 1) // 2) % _MOD

    t1 = (l_p * a_sum % _MOD * g1) % _MOD
    t2 = (b_sum * g0) % _MOD
    t3 = (l_p * c_sum % _MOD * k1) % _MOD
    t4 = (d_sum * k0) % _MOD

    total = (t1 + t2 - t3 - t4) % _MOD
    inv9 = pow(9, _MOD - 2, _MOD)
    return (total * inv9) % _MOD


if __name__ == "__main__":
    print(solve())
