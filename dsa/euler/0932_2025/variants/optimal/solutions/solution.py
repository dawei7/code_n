"""Project Euler Problem 932: 2025.

Mathematical formulation:
A positive integer N = a * 10^k + b is a 2025-number if N = (a + b)^2, where b has exactly k digits.
T(n) is the sum of all 2025-numbers with n digits or less.
Given:
  T(4) = 5131  (from numbers 81, 2025, 3025)

Diophantine Reduction & Chinese Remainder Theorem:
Let x = a + b. Then:
  x^2 = a * 10^k + b = a * 10^k + (x - a) = a(10^k - 1) + x.
Rearranging gives:
  x(x - 1) = a(10^k - 1).
Since gcd(x, x - 1) = 1, each coprime factorization 10^k - 1 = d_1 * d_2 yields a unique
base solution x_0 in [0, 10^k - 1) via the Chinese Remainder Theorem:
  x == 0 (mod d_1),  x == 1 (mod d_2).

All valid solutions are x = x_0 + j(10^k - 1) <= 10^{n/2} = 10^8.
Checking the exact digit length condition 10^{k-1} <= b < 10^k identifies all 2025-numbers.

Evaluates T(16) = 72673459417881349 in under 4s in 100% pure Python.
"""

from __future__ import annotations

import math


def solve(max_digits: int = 16) -> int:
    """Compute T(n) for 2025-numbers with at most max_digits."""
    max_x = int(math.isqrt(10**max_digits - 1))
    found: set[int] = set()

    for k in range(1, max_digits):
        m_mod = 10**k - 1

        # Factor m_mod into prime powers
        temp = m_mod
        prime_powers = []
        p = 2
        while p * p <= temp:
            if temp % p == 0:
                pp = 1
                while temp % p == 0:
                    pp *= p
                    temp //= p
                prime_powers.append(pp)
            p += 1
        if temp > 1:
            prime_powers.append(temp)

        num_pp = len(prime_powers)
        for mask in range(1 << num_pp):
            d1 = 1
            d2 = 1
            for bit in range(num_pp):
                if (mask >> bit) & 1:
                    d1 *= prime_powers[bit]
                else:
                    d2 *= prime_powers[bit]

            inv = pow(d1, -1, d2) if d2 > 1 else 0
            x0 = (d1 * inv) % m_mod

            j = 0
            while True:
                x = x0 + j * m_mod
                j += 1
                if x > max_x:
                    break
                if x <= 0:
                    continue

                a = (x * (x - 1)) // m_mod
                b = x - a
                if a <= 0 or b <= 0:
                    continue

                # Exact digit length condition for b
                if 10 ** (k - 1) <= b < 10**k:
                    val = x * x
                    if val < 10**max_digits:
                        found.add(val)

    return sum(found)


if __name__ == "__main__":
    print(solve())
