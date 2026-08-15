"""Project Euler Problem 492: Exploding Sequence.

Find B(10^9, 10^7, 10^15), where B(x, y, n) = sum_{p in P, x <= p <= x+y} (a_n mod p)
and a_1 = 1, a_{n+1} = 6 a_n^2 + 10 a_n + 3.
"""

from math import isqrt
from typing import List


def _primes_in_range(x_start: int, y_range: int) -> List[int]:
    limit = x_start + y_range
    sieve_limit = isqrt(limit)

    is_p = [True] * (sieve_limit + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, isqrt(sieve_limit) + 1):
        if is_p[i]:
            for j in range(i * i, sieve_limit + 1, i):
                is_p[j] = False
    small_primes = [i for i, v in enumerate(is_p) if v]

    seg = bytearray(b"\x01") * (y_range + 1)
    for p in small_primes:
        start = (x_start + p - 1) // p * p
        if start < p * p:
            start = p * p
        off = start - x_start
        seg[off::p] = b"\x00" * ((y_range - off) // p + 1)

    return [x_start + i for i, v in enumerate(seg) if v and (x_start + i) > 1]


def solve(
    x_start: int = 10**9, y_range: int = 10**7, n: int = 10**15
) -> int:
    """Compute B(x, y, n) using Chebyshev/quadratic extension ring exponentiation."""
    primes = _primes_in_range(x_start, y_range)
    total = 0
    pow_fn = pow

    for p in primes:
        leg = pow_fn(13, (p - 1) // 2, p)
        leg_val = -1 if leg == p - 1 else 1
        mod_group = p - leg_val
        exp_e = pow_fn(2, n - 1, mod_group)

        inv2 = (p + 1) // 2
        u_a = (11 * inv2) % p
        u_b = (3 * inv2) % p

        res_a, res_b = 1, 0
        base_a, base_b = u_a, u_b

        e = exp_e
        while e > 0:
            if e & 1:
                res_a, res_b = (
                    res_a * base_a + 13 * res_b * base_b
                ) % p, (res_a * base_b + res_b * base_a) % p
            base_a, base_b = (
                base_a * base_a + 13 * base_b * base_b
            ) % p, (2 * base_a * base_b) % p
            e >>= 1

        x_n = (2 * res_a) % p
        a_n = ((x_n - 5) * pow_fn(6, p - 2, p)) % p
        total += a_n

    return total


if __name__ == "__main__":
    print(solve())
