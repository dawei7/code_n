"""Project Euler 291: Panaitopol Primes

Find how many Panaitopol primes are less than 5 * 10^15.
A prime p is Panaitopol if p = (x^4 - y^4) / (x^3 + y^3) for positive integers x, y.
"""

from __future__ import annotations

import math


def solve(limit_p: int = 5 * 10**15) -> str:
    """Calculates the number of Panaitopol primes less than limit_p.

    Algebraic reduction of p = (x^4 - y^4) / (x^3 + y^3):
      x^4 - y^4 = (x - y)(x + y)(x^2 + y^2)
      x^3 + y^3 = (x + y)(x^2 - xy + y^2)
      p = (x - y)(x^2 + y^2) / (x^2 - xy + y^2)
    For p to be prime and integers x > y > 0:
      x - y = 1 and x = n + 1, y = n
      p = n^2 + (n + 1)^2 = 2n^2 + 2n + 1

    We sieve primes of the form 2n^2 + 2n + 1 < limit_p:
      All prime divisors q of 2n^2 + 2n + 1 satisfy (2n+1)^2 = -1 (mod q),
      so q = 1 (mod 4).
      For each prime q = 1 (mod 4) with q <= sqrt(limit_p), we compute the modular square root
      r^2 = -1 (mod q) and cross out the two arithmetic progressions of composite terms.
    """
    n_max = int(math.isqrt((limit_p - 1) // 2))
    q_max = int(math.isqrt(limit_p)) + 100

    # Sieve primes <= q_max
    is_p = bytearray(b"\x01") * (q_max + 1)
    is_p[0] = is_p[1] = 0
    for i in range(2, math.isqrt(q_max) + 1):
        if is_p[i]:
            is_p[i * i :: i] = b"\x00" * len(is_p[i * i :: i])

    primes_1mod4 = [i for i in range(5, q_max + 1, 4) if is_p[i]]

    # Polynomial sieve array of size n_max + 1:
    poly_sieve = bytearray(b"\x01") * (n_max + 1)
    poly_sieve[0] = 0  # n >= 1

    test_bases = (2, 3, 5, 6, 7, 10, 11, 13, 17, 19)

    for q in primes_1mod4:
        exp = (q - 1) >> 2
        for g in test_bases:
            r = pow(g, exp, q)
            if (r * r + 1) % q == 0:
                break
        else:
            g = 21
            while True:
                r = pow(g, exp, q)
                if (r * r + 1) % q == 0:
                    break
                g += 1

        inv2 = (q + 1) >> 1
        n1 = ((r - 1) * inv2) % q
        n2 = ((q - r - 1) * inv2) % q

        # If 2n^2 + 2n + 1 == q, n represents the prime itself, so start crossing at n + q
        start1 = n1 if (2 * n1 * n1 + 2 * n1 + 1) > q else n1 + q
        if start1 <= n_max:
            poly_sieve[start1::q] = b"\x00" * len(poly_sieve[start1::q])

        start2 = n2 if (2 * n2 * n2 + 2 * n2 + 1) > q else n2 + q
        if start2 <= n_max:
            poly_sieve[start2::q] = b"\x00" * len(poly_sieve[start2::q])

    total_panaitopol_primes = sum(poly_sieve)
    return str(total_panaitopol_primes)


if __name__ == "__main__":
    print(solve())
