"""Project Euler Problem 853: Pisano Periods 1.

Mathematical formulation:
For any positive integer n, the Fibonacci sequence modulo n is periodic with Pisano period pi(n).
pi(n) divides L if and only if:
  F_L = 0 (mod n) and F_{L+1} = 1 (mod n)
which is equivalent to:
  n divides G_L = gcd(F_L, F_{L+1} - 1)

For L = 120:
  G_120 = gcd(F_120, F_121 - 1) = 1548008755920 = 2^4 * 3^2 * 5 * 11 * 31 * 41 * 61 * 2521

A divisor n of G_120 has Pisano period exactly 120 if and only if pi(n) does not divide
any maximal proper divisor of 120 (namely d in {60, 40, 24}).
We enumerate all 960 divisors of G_120, filter those < 10^9 with pi(n) = 120, and sum them.
"""

from __future__ import annotations

import math


def _fib(k: int) -> int:
    a, b = 0, 1
    for _ in range(k):
        a, b = b, a + b
    return a


def solve(limit: int = 10**9, target_period: int = 120) -> int:
    """Find the sum of all n < limit such that pi(n) == target_period."""
    f_l = _fib(target_period)
    f_lp1 = _fib(target_period + 1)
    g_l = math.gcd(f_l, f_lp1 - 1)

    # Prime factorize g_l
    temp = g_l
    factors: dict[int, int] = {}
    d = 2
    while d * d <= temp:
        if temp % d == 0:
            e = 0
            while temp % d == 0:
                e += 1
                temp //= d
            factors[d] = e
        d += 1
    if temp > 1:
        factors[temp] = 1

    # Generate all divisors of g_l
    divs = [1]
    for p, e in factors.items():
        new_divs = []
        p_pow = 1
        for _ in range(e + 1):
            for val in divs:
                new_divs.append(val * p_pow)
            p_pow *= p
        divs = new_divs

    # Maximal proper divisors of target_period (for 120: 60, 40, 24)
    # Find all prime factors of target_period
    maximal_proper = []
    for p in (2, 3, 5):
        if target_period % p == 0:
            maximal_proper.append(target_period // p)

    proper_fibs = [(d, _fib(d), _fib(d + 1) - 1) for d in maximal_proper]

    total_sum = 0
    for n in divs:
        if n >= limit:
            continue
        # Check that n does not divide the period for any maximal proper divisor
        is_exact = True
        for _, f_d, f_dp1_m1 in proper_fibs:
            if f_d % n == 0 and f_dp1_m1 % n == 0:
                is_exact = False
                break
        if is_exact:
            total_sum += n

    return total_sum


if __name__ == "__main__":
    print(solve())
