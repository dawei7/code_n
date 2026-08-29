"""Project Euler Problem 656: Palindromic Sequences.

Find the last 15 digits of sum_{beta in T} H_100(sqrt(beta)), where T is the set of positive
non-square integers <= 1000 and H_g(alpha) is the sum of the first g palindromic prefix lengths of S_alpha.
"""

import math
from typing import List, Tuple

_MOD = 10**15


def _sqrt_continued_fraction_period(n: int) -> Tuple[int, List[int]]:
    a0 = math.isqrt(n)
    if a0 * a0 == n:
        raise ValueError("n must be non-square")

    m = 0
    d = 1
    a = a0
    period: List[int] = []
    while True:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        period.append(a)
        if a == 2 * a0:
            break
    return a0, period


def _h_mod_from_period(period: List[int], g: int, mod: int = _MOD) -> int:
    q_m1, q0 = 0, 1
    k = 1
    i = 0
    count = 0
    s = 0
    while count < g:
        a = period[i]
        i += 1
        if i == len(period):
            i = 0

        if k % 2 == 1:
            remaining = g - count
            tmax = min(a, remaining)
            s = (s + tmax * q_m1 + q0 * (tmax * (tmax + 1) // 2)) % mod
            count += tmax

        q1 = (a * q0 + q_m1) % mod
        q_m1, q0 = q0, q1
        k += 1
    return s % mod


def solve(limit_beta: int = 1000, g_terms: int = 100) -> str:
    """Compute the sum of H_g(sqrt(beta)) mod 10^15 over all non-square beta <= limit_beta using continued fraction semiconvergents."""
    squares = {i * i for i in range(1, math.isqrt(limit_beta) + 1)}
    total = 0

    for beta in range(2, limit_beta + 1):
        if beta in squares:
            continue
        _, period = _sqrt_continued_fraction_period(beta)
        total = (total + _h_mod_from_period(period, g_terms, _MOD)) % _MOD

    return f"{total:015d}"


if __name__ == "__main__":
    print(solve())
