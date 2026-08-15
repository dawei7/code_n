"""Project Euler 313: Sliding Game

Find the number of grids (m, n) for which the minimum moves S(m, n) = p^2
where p < 10^6 is prime.
"""

from __future__ import annotations

import math


def solve(limit: int = 1_000_000) -> str:
    """Calculates the number of grid pairs (m, n) with S(m, n) = p^2 for prime p < limit

    using algebraic reduction of the sliding puzzle minimum move function.
    """
    # Sieve primes up to limit
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.isqrt(limit)) + 1):
        if sieve[i]:
            sieve[i * i : limit : i] = [False] * len(sieve[i * i : limit : i])
    primes = [i for i, is_p in enumerate(sieve) if is_p]

    count = 0
    for p in primes:
        p2 = p * p

        # Case 1: Square grids (m == n)
        # S(m, m) = 8m - 11 = p^2 => 8m = p^2 + 11
        if (p2 + 11) % 8 == 0:
            m = (p2 + 11) // 8
            if m >= 2:
                count += 1

        # Case 2: Rectangular grids (m > n >= 2)
        # S(m, n) = 6m + 2n - 13 = p^2 => 3m + n = (p^2 + 13) // 2
        if (p2 + 13) % 2 == 0:
            rhs = (p2 + 13) // 2
            # Since n >= 2 and m > n:
            # min_m: m > rhs - 3m => 4m > rhs => m >= rhs // 4 + 1
            # max_m: rhs - 3m >= 2 => 3m <= rhs - 2 => m <= (rhs - 2) // 3
            min_m = rhs // 4 + 1
            max_m = (rhs - 2) // 3
            if max_m >= min_m:
                # Each unordered pair (m, n) with m != n gives 2 grids: (m, n) and (n, m)
                count += 2 * (max_m - min_m + 1)

    return str(count)


if __name__ == "__main__":
    print(solve())
