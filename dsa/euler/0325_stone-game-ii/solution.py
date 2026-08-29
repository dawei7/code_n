"""Project Euler 325: Stone Game II

Find S(10^16) mod 7^10, where S(N) is the sum of (x + y) for all losing configurations
(x, y) with 0 < x < y <= N in the Game of Euclid.
"""

from __future__ import annotations

import math


def get_k(m: int) -> int:
    """Computes floor(alpha * m) = floor((sqrt(5) - 1) / 2 * m) using exact integer square roots."""
    return (math.isqrt(5 * m * m) - m) // 2


def solve(limit: int = 10_000_000_000_000_000, mod: int = 282_475_249) -> str:
    """Calculates S(limit) mod mod where mod = 7^10 using the Euclid Game P-position characterization

    x + 1 <= y <= min(N, floor(phi * x)), split at M = floor(N / phi), and O(log N) Beatty floor sum reduction.
    """
    m = get_k(limit)

    # 1. Part 1: x in [1, M] via iterative Beatty floor sums
    m_stack: list[int] = []
    curr = m
    while curr > 0:
        m_stack.append(curr)
        curr = get_k(curr)

    s1_k = s2_k = s3_k = 0
    part1 = 0

    for cur_m in reversed(m_stack):
        k = get_k(cur_m)

        s1 = cur_m * k - k * (k + 1) // 2 - s1_k
        sum_poly_2 = k * (k + 1) * (k + 2) // 6
        s2 = (
            k * cur_m * (cur_m + 1) // 2
            - sum_poly_2
            - s2_k
            - (s3_k + s1_k) // 2
        )
        sum_poly_3 = k * (k + 1) * (4 * k - 1) // 6
        s3 = cur_m * k * k - sum_poly_3 - 2 * s2_k + s1_k

        tot = 2 * s2 + (s3 + s1) // 2
        part1, s1_k, s2_k, s3_k = tot, s1, s2, s3

    # 2. Part 2: x in [M + 1, limit - 1] where Y_max(x) = limit
    cnt = limit - 1 - m
    if cnt > 0:
        sum_x = (m + 1 + limit - 1) * cnt // 2
        sum_x2 = (limit - 1) * limit * (2 * limit - 1) // 6 - m * (m + 1) * (
            2 * m + 1
        ) // 6
        part2 = (
            limit * (limit + 1) * cnt + (2 * limit - 1) * sum_x - 3 * sum_x2
        ) // 2
    else:
        part2 = 0

    total_s = (part1 + part2) % mod
    return str(total_s)


if __name__ == "__main__":
    print(solve())
