"""Project Euler Problem 775: Saving Paper.

Find G(10^16) modulo 10^9+7, where G(N) = sum_{n=1}^N g(n) is the total paper saved
by optimal void-free compact polycube packaging.
"""

import math
from typing import Tuple

_MOD = 1_000_000_007


def _icbrt_floor(x: int) -> int:
    if x < 0:
        return 0
    lo, hi = 0, 1
    while hi * hi * hi <= x:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid * mid * mid <= x:
            lo = mid
        else:
            hi = mid
    return lo


def _c_count(m: int) -> int:
    if m <= 1:
        return 0
    return math.isqrt(4 * m - 1) - 1


def _c_prefix_sum(t: int) -> int:
    if t <= 1:
        return 0
    a = math.isqrt(t)
    base = (a - 1) * a * (8 * a - 1) // 6

    sq = a * a
    if t == sq:
        return base

    end_even = min(t, sq + a)
    cnt_even = end_even - (sq + 1) + 1
    partial = cnt_even * (2 * a - 1)

    if t > sq + a:
        cnt_odd = t - (sq + a + 1) + 1
        partial += cnt_odd * (2 * a)

    return base + partial


def solve(N: int = 10_000_000_000_000_000, mod: int = _MOD) -> int:
    """Compute G(N) mod 10^9+7 using layer-by-layer polycube surface area integration."""
    if N <= 0:
        return 0

    sum6 = (3 * (N % mod) * ((N + 1) % mod)) % mod
    total_smin = 6 % mod
    if N == 1:
        return (sum6 - total_smin) % mod

    k_max = _icbrt_floor(N - 1)
    for k in range(1, k_max + 1):
        k3 = k * k * k
        if k3 + 1 > N:
            break
        full = (k + 1) * (k + 1) * (k + 1) - k3
        L = min(N - k3, full)

        k2 = k * k
        cap2 = k * (k + 1)

        lenA = min(L, k2)
        rem = L - lenA
        lenB = min(rem, cap2) if rem > 0 else 0
        rem -= lenB
        lenC = rem if rem > 0 else 0

        c_k2 = _c_count(k2)
        c_kk1 = _c_count(cap2)

        sum_c = _c_prefix_sum(lenA)
        if lenB:
            sum_c += lenB * c_k2 + _c_prefix_sum(lenB)
        if lenC:
            sum_c += lenC * (c_k2 + c_kk1) + _c_prefix_sum(lenC)

        sum_bv = 4 * lenA + 8 * lenB + 12 * lenC

        block = (L * (6 * k2) + sum_bv + 2 * sum_c) % mod
        total_smin = (total_smin + block) % mod

    return (sum6 - total_smin) % mod


if __name__ == "__main__":
    print(solve())
