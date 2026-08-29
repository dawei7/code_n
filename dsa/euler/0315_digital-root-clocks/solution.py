"""Project Euler 315: Digital Root Clocks

Find the difference in total transition transitions between Sam's clock and Max's clock
for all prime numbers between 10^7 and 2*10^7.
"""

from __future__ import annotations

import math

# 7-segment bitmasks for digits 0-9:
# Segments: a:1, b:2, c:4, d:8, e:16, f:32, g:64
DIGITS: list[int] = [63, 6, 91, 79, 102, 109, 125, 39, 127, 111]


def common_segments(u: int, v: int) -> int:
    """Calculates the number of overlapping lit segments between two right-aligned numbers."""
    common = 0
    while u > 0 and v > 0:
        du = u % 10
        dv = v % 10
        common += (DIGITS[du] & DIGITS[dv]).bit_count()
        u //= 10
        v //= 10
    return common


def digit_sum(n: int) -> int:
    """Calculates the sum of digits of n."""
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


def solve(lower_bound: int = 10_000_000, upper_bound: int = 20_000_000) -> str:
    """Calculates the transition savings of Max's clock over Sam's clock for all primes in [lower_bound, upper_bound]

    using the bitwise overlap theorem: Savings(u -> v) = 2 * popcount(u & v).
    """
    # Sieve primes up to upper_bound
    sieve = [True] * (upper_bound + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.isqrt(upper_bound)) + 1):
        if sieve[i]:
            sieve[i * i : upper_bound + 1 : i] = [False] * len(
                sieve[i * i : upper_bound + 1 : i]
            )

    total_savings = 0

    # For each prime, compute the digital root sequence and accumulate bitwise intersection savings
    for p in range(lower_bound, upper_bound + 1):
        if sieve[p]:
            curr = p
            while curr >= 10:
                nxt = digit_sum(curr)
                total_savings += 2 * common_segments(curr, nxt)
                curr = nxt

    return str(total_savings)


if __name__ == "__main__":
    print(solve())
