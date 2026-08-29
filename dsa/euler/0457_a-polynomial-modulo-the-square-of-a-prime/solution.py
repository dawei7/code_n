"""Project Euler Problem 457: A Polynomial Modulo the Square of a Prime.

Find SR(10^7), where SR(L) is the sum of R(p) for all primes p <= L,
and R(p) is the smallest positive integer n such that n^2 - 3n - 1 = 0 (mod p^2).
"""

from math import isqrt
from typing import List


def _sieve_primes(limit: int) -> List[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0] = sieve[1] = 0
    r = isqrt(limit)
    for i in range(2, r + 1):
        if sieve[i]:
            sieve[i * i : limit + 1 : i] = b"\x00" * len(
                sieve[i * i : limit + 1 : i]
            )
    return [i for i in range(2, limit + 1) if sieve[i]]


def solve(limit: int = 10_000_000) -> int:
    """Compute SR(limit) using Tonelli-Shanks and Hensel lifting mod p^2."""
    primes = _sieve_primes(limit)
    total = 0

    for p in primes:
        if p == 2 or p == 13:
            continue
        if p == 3:
            total += 5
            continue

        if pow(13, (p - 1) // 2, p) != 1:
            continue

        if p % 4 == 3:
            r = pow(13, (p + 1) // 4, p)
        elif p % 8 == 5:
            q = (p - 1) // 4
            v = pow(13, q, p)
            if v == 1:
                r = pow(13, (q + 1) // 2, p)
            else:
                r = pow(13, (q + 1) // 2, p) * pow(2, q, p) % p
        else:
            q = p - 1
            s = 0
            while q % 2 == 0:
                q //= 2
                s += 1
            z = 2
            while pow(z, (p - 1) // 2, p) == 1:
                z += 1
            c = pow(z, q, p)
            r = pow(13, (q + 1) // 2, p)
            t = pow(13, q, p)
            m = s
            while t != 1:
                i = 0
                temp = t
                while temp != 1:
                    temp = (temp * temp) % p
                    i += 1
                b = pow(c, 1 << (m - i - 1), p)
                r = (r * b) % p
                c = (b * b) % p
                t = (t * c) % p
                m = i

        p2 = p * p
        inv_2r = pow(2 * r, p - 2, p)
        r2 = (r - (r * r - 13) * inv_2r) % p2
        inv2 = (p2 + 1) // 2
        n1 = ((3 + r2) * inv2) % p2
        n2 = ((3 - r2) * inv2) % p2
        if n1 == 0:
            n1 = p2
        if n2 == 0:
            n2 = p2
        total += min(n1, n2)

    return total


if __name__ == "__main__":
    print(solve())
