"""Project Euler Problem 542: Geometric Progression with Maximum Sum.

Find T(10^17), where T(n) = sum_{k=4..n} (-1)^k S(k), and S(k) is the maximal sum
of >= 3 distinct positive integers forming a geometric progression with max element <= k.
"""

from typing import Dict


def _iroot(n: int, k: int) -> int:
    if k <= 1:
        return n
    x = int(n ** (1.0 / k))
    if x < 1:
        x = 1
    while pow(x + 1, k) <= n:
        x += 1
    while pow(x, k) > n:
        x -= 1
    return x


def _s_func(k: int) -> int:
    if k < 4:
        return 0

    best = 0
    t_max = k.bit_length() - 1

    for t in range(t_max, 1, -1):
        p_max = _iroot(k, t)
        if p_max < 2:
            continue

        ub = min(t + 1, p_max) * k
        if ub <= best:
            if p_max >= t + 1:
                break
            continue

        for p in range(2, p_max + 1):
            d = pow(p, t)
            b = k // d
            if b == 0:
                break
            c = pow(p, t + 1) - pow(p - 1, t + 1)
            val = b * c
            if val > best:
                best = val

    return best


def _alt_sum_constant(a: int, b: int) -> int:
    if a > b:
        return 0
    length = b - a + 1
    if length % 2 == 0:
        return 0
    return 1 if (a % 2 == 0) else -1


def solve(limit_n: int = 10**17) -> int:
    """Compute T(limit_n) using piecewise constant leapfrogging with exponential and binary search."""
    if limit_n < 4:
        return 0

    cache: Dict[int, int] = {}

    def s_cached(x: int) -> int:
        v = cache.get(x)
        if v is None:
            v = _s_func(x)
            cache[x] = v
        return v

    total = 0
    k = 4

    while k <= limit_n:
        v = s_cached(k)

        step = 1
        hi = min(limit_n, k + step)
        v_hi = s_cached(hi)
        while v_hi == v and hi != limit_n:
            step *= 2
            hi = min(limit_n, k + step)
            v_hi = s_cached(hi)

        if hi == limit_n and v_hi == v:
            total += v * _alt_sum_constant(k, limit_n)
            break

        lo = k + 1
        r = hi
        while lo < r:
            mid = (lo + r) // 2
            if s_cached(mid) == v:
                lo = mid + 1
            else:
                r = mid
        change = lo

        total += v * _alt_sum_constant(k, change - 1)
        k = change

    return total


if __name__ == "__main__":
    print(solve())
