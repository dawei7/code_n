"""Project Euler Problem 779: Prime Factor and Exponent.

Find sum_{K=1}^infty \\overline{f_K} rounded to 12 digits after the decimal point,
where \\overline{f_K} is the asymptotic mean of (\\alpha(n) - 1) / p(n)^K.
"""

import math
from typing import List


def _primes_upto(n: int) -> List[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0] = sieve[1] = 0
    lim = int(math.isqrt(n))
    for i in range(2, lim + 1):
        if sieve[i]:
            sieve[i * i : n + 1 : i] = b"\x00" * ((n - i * i) // i + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def solve(max_prime: int = 2_000_000, digits: int = 12) -> str:
    """Compute sum_{K=1}^infty \\overline{f_K} using exact Mertens density prime series."""
    primes = _primes_upto(max_prime)
    total = 0.0
    curr = 1.0

    for p in primes:
        term = curr / (p * (p - 1) * (p - 1))
        total += term
        curr *= (p - 1) / p

    return f"{total:.{digits}f}"


if __name__ == "__main__":
    print(solve())
