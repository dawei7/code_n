"""Project Euler 268: At Least Four Distinct Prime Factors Less Than 100

Find how many positive integers less than 10^16 are divisible by at least four distinct primes less than 100.
"""

from __future__ import annotations

import math


def solve(limit: int = 10**16) -> str:
    """Calculates the count of integers < limit divisible by >= 4 primes < 100

    using the generalized Principle of Inclusion-Exclusion (PIE) with binomial weighting.
    """
    # 25 primes below 100
    primes = [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
    ]
    n_limit = limit - 1
    num_primes = len(primes)

    # Precompute inclusion-exclusion coefficients c_j = (-1)^(j-4) * comb(j-1, 3)
    coeffs = [0] * (num_primes + 1)
    for j in range(4, num_primes + 1):
        coeffs[j] = ((-1) ** (j - 4)) * math.comb(j - 1, 3)

    total_count = 0

    def dfs(idx: int, curr_prod: int, size: int) -> None:
        nonlocal total_count
        if size >= 4:
            total_count += coeffs[size] * (n_limit // curr_prod)

        for i in range(idx, num_primes):
            p = primes[i]
            if curr_prod * p <= n_limit:
                dfs(i + 1, curr_prod * p, size + 1)
            else:
                break

    dfs(0, 1, 0)
    return str(total_count)


if __name__ == "__main__":
    print(solve())
