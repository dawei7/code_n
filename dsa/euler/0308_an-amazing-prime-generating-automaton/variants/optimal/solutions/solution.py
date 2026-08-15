"""Project Euler 308: An Amazing Prime-generating Automaton

Find the number of iterations needed for Conway's 14-fraction Fractran program (PRIMEGAME)
to produce 2^{10001st prime}.
"""

from __future__ import annotations

import math


def sum_floors(n: int, low: int, high: int) -> int:
    """Computes sum_{d = low}^{high} floor(n / d) in O(sqrt(n)) time

    using Dirichlet hyperbola block decomposition.
    """
    if low > high:
        return 0
    total = 0
    d = low
    while d <= high:
        q = n // d
        if q == 0:
            break
        next_d = n // q
        end_d = min(high, next_d)
        total += q * (end_d - d + 1)
        d = end_d + 1
    return total


def candidate_steps_fast(n: int, is_prime: bool, d_stop: int) -> int:
    """Computes the exact number of Fractran iterations to process candidate integer n

    based on the algebraic simplification: steps(d) = 6n + 2*floor(n/d) + 2.
    """
    # Initial transfer of d_start = n - 1:
    steps = 2 * (n - 1)

    if is_prime:
        # Non-divisors d from 2 to n - 1:
        count_non_div = n - 2
        sum_q = sum_floors(n, 2, n - 1)
        steps += count_non_div * (6 * n + 2) + 2 * sum_q
        # Final divisor d = 1:
        steps += 1 + (n - 1) * 6 + 8
        return steps

    # Non-divisors d from d_stop + 1 to n - 1:
    count_non_div = (n - 1) - (d_stop + 1) + 1
    sum_q = sum_floors(n, d_stop + 1, n - 1)
    steps += count_non_div * (6 * n + 2) + 2 * sum_q
    # Stopping divisor d = d_stop:
    q_stop = n // d_stop
    steps += (
        1
        + (q_stop - 1) * (4 * d_stop + 2)
        + (4 * d_stop + 4)
        + n
        + (d_stop - 1)
    )
    return steps


def solve(target_prime_count: int = 10_001) -> str:
    """Calculates the total Fractran iterations required to output the target_prime_count-th prime."""
    # Precompute smallest prime factor (SPF) for all candidates up to limit
    limit = 120_000
    spf = list(range(limit + 1))
    for i in range(2, int(math.isqrt(limit)) + 1):
        if spf[i] == i:
            for j in range(i * i, limit + 1, i):
                if spf[j] == j:
                    spf[j] = i

    total_steps = 0
    primes_found = 0

    # Candidate n = 2:
    total_steps += 2  # initial setup
    total_steps += candidate_steps_fast(2, True, 1)
    primes_found += 1

    # Candidate n = 3:
    n = 3
    total_steps += 2 + 1  # setup after prime 2

    while primes_found < target_prime_count:
        p_min = spf[n]
        is_p = p_min == n
        d_stop = 1 if is_p else n // p_min

        st = candidate_steps_fast(n, is_p, d_stop)
        total_steps += st

        if is_p:
            primes_found += 1
            if primes_found == target_prime_count:
                break
            total_steps += n + 1
        else:
            total_steps += 1
        n += 1

    return str(total_steps)


if __name__ == "__main__":
    print(solve())
