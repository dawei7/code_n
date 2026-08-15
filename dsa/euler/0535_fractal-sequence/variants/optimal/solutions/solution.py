"""Project Euler Problem 535: Fractal Sequence.

Find the last 9 digits of T(10^18), where T(n) is the sum of the first n terms
of the fractal sequence S.
"""

from __future__ import annotations

import math
from typing import Dict

MOD = 10**9


def _sum_1_to_m(m: int) -> int:
    if m <= 0:
        return 0
    return m * (m + 1) // 2


def _sum_floor_sqrt_1_to_m(m: int) -> int:
    if m <= 0:
        return 0
    t = math.isqrt(m)
    full = t - 1
    if full <= 0:
        return t * (m - t * t + 1)

    s1 = full * (full + 1) // 2
    s2 = full * (full + 1) * (2 * full + 1) // 6
    total = 2 * s2 + s1
    total += t * (m - t * t + 1)
    return total


def solve(n: int = 10**18, mod: int = MOD) -> str:
    """Compute the last 9 digits of T(n) via recursive self-embedding fractal DP."""
    memo_phi: Dict[int, int] = {0: 0, 1: 0}
    memo_g: Dict[int, int] = {0: 0}
    memo_t: Dict[int, int] = {0: 0}

    def phi(k: int) -> int:
        if k in memo_phi:
            return memo_phi[k]
        if k <= 1:
            memo_phi[k] = 0
            return 0

        lo, hi = 0, k
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if mid + g(mid) <= k:
                lo = mid
            else:
                hi = mid

        memo_phi[k] = lo
        return lo

    def g(k: int) -> int:
        if k in memo_g:
            return memo_g[k]
        r = phi(k)
        m = k - r
        val = g(r) + _sum_floor_sqrt_1_to_m(m)
        memo_g[k] = val
        return val

    def t_sum(k: int) -> int:
        if k in memo_t:
            return memo_t[k]
        r = phi(k)
        m = k - r
        val = t_sum(r) + _sum_1_to_m(m)
        memo_t[k] = val
        return val

    # Iterative pre-population or evaluation
    steps = []
    curr = n
    while curr > 1:
        steps.append(curr)
        curr = phi(curr)

    for val in reversed(steps):
        t_sum(val)

    ans = t_sum(n) % mod
    return f"{ans:09d}"


if __name__ == "__main__":
    print(solve())
