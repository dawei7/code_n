"""Project Euler Problem 403: Lattice Points Enclosed by Parabola and Line.

Find S(10^12) mod 10^8, where S(N) is the sum of lattice points L(a, b) over |a|, |b| <= N
such that the domain area is rational.
"""

from math import isqrt

MOD = 100_000_000


def _g(n: int) -> int:
    return (n * n * n + 5 * n + 6) // 6


def _g_sum(n: int) -> int:
    if n < 0:
        return 0
    n2 = n * n
    n3 = n2 * n
    n4 = n2 * n2
    return (n4 + 2 * n3 + 11 * n2 + 34 * n + 24) // 24


def _h_sum(n: int) -> int:
    if n < 0:
        return 0
    s1 = n * (n + 1) // 2
    s2 = n * (n + 1) * (2 * n + 1) // 6
    s3 = s1 * s1
    s4 = n * (n + 1) * (2 * n + 1) * (3 * n * n + 3 * n - 1) // 30
    return (s4 + 2 * s3 + 11 * s2 + 34 * s1 + 24 * (n + 1)) // 24


def _sum_g_interval(l: int, r: int) -> int:
    if l > r:
        return 0
    return _h_sum(r) - _h_sum(l - 1)


def solve(n_val: int = 10**12) -> int:
    """Compute S(n_val) mod 10^8 using hyperbola grouping and degree-4 Faulhaber prefix polynomials."""
    s = isqrt(n_val)
    total = 0

    # p = 0
    total += 2 * _g_sum(n_val) - 1

    if n_val >= 1:
        f1 = _g_sum(n_val + 1) + _g_sum(n_val - 2) - 1
        total += 2 * f1

    if n_val >= 2:
        fn = _g(n_val) + _g(n_val + 1)
        total += 2 * fn

    # Small |p|
    hi = min(s, n_val - 1)
    if hi >= 2:
        small_sum = 0
        for p in range(2, hi + 1):
            m = n_val // p
            small_sum += _g_sum(m + p) + _g_sum(m - p) - 1
        total += 2 * small_sum

    # Large |p| grouped by m = floor(n_val / p)
    large_sum = 0
    for m in range(1, s + 1):
        l = n_val // (m + 1) + 1
        r = n_val // m
        if r <= s:
            continue
        if l <= s:
            l = s + 1
        if l > r:
            continue
        if r == n_val and n_val >= l:
            if l <= n_val - 1:
                large_sum += _sum_g_interval(
                    l + m, n_val - 1 + m
                ) - _sum_g_interval(l - m - 1, n_val - 1 - m - 1)
        else:
            large_sum += _sum_g_interval(l + m, r + m) - _sum_g_interval(
                l - m - 1, r - m - 1
            )
    total += 2 * large_sum

    diag = 2 * min(n_val // 2, isqrt(n_val)) + 1
    ans = (total + diag) // 2
    return ans % MOD


if __name__ == "__main__":
    print(solve())
