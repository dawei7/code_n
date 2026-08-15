"""Project Euler Problem 453: Lattice Quadrilaterals.

Find Q(12345, 6789) mod 135707531, where Q(m, n) is the number of simple
quadrilaterals with vertices on the (m+1) x (n+1) lattice grid.
"""

from functools import lru_cache
from math import comb, isqrt

MOD = 135_707_531


def _sum_pows(t: int, k: int) -> int:
    if t <= 0:
        return 0
    if k == 0:
        return t
    if k == 1:
        return t * (t + 1) // 2
    if k == 2:
        return t * (t + 1) * (2 * t + 1) // 6
    if k == 3:
        return (t * t * (t + 1) * (t + 1)) // 4
    if k == 4:
        return t * (t + 1) * (2 * t + 1) * (3 * t * t + 3 * t - 1) // 30
    raise ValueError("k must be in [0..4]")


def solve(m: int = 12345, n: int = 6789, mod: int = MOD) -> int:
    """Compute Q(m, n) mod mod using 2D lattice moments and Pick's theorem decomposition."""
    p_total = (m + 1) * (n + 1)

    @lru_cache(maxsize=None)
    def g_func(u: int, v: int, a: int, b: int) -> int:
        if u <= 0 or v <= 0:
            return 0
        q = isqrt(u)
        upper = min(v, u // q)
        res = _sum_pows(u, a) * _sum_pows(v, b)

        for k in range(2, upper + 1):
            res -= g_func(u // k, v // k, a, b) * (k ** (a + b))

        for k in range(1, q):
            x = v // (u // (k + 1) + 1)
            y = v // (u // k)

            if x == y:
                res -= g_func(k, x, a, b) * (
                    _sum_pows(u // k, a + b)
                    - _sum_pows(u // (k + 1), a + b)
                )
            else:
                lo = max(u // (k + 1), v // (x + 1))
                hi = min(u // k, v // x)
                if hi > lo:
                    res -= g_func(k, x, a, b) * (
                        _sum_pows(hi, a + b) - _sum_pows(lo, a + b)
                    )

                if y:
                    lo2 = max(u // (k + 1), v // (y + 1))
                    hi2 = min(u // k, v // y)
                    if hi2 > lo2:
                        res -= g_func(k, y, a, b) * (
                            _sum_pows(hi2, a + b)
                            - _sum_pows(lo2, a + b)
                        )

        return res

    def h_func(a: int, b: int, c: int) -> int:
        if c == 0:
            return _sum_pows(m, a) * _sum_pows(n, b)

        q = isqrt(m)
        upper = min(n, m // q)
        res = 0

        for k in range(1, upper + 1):
            res += g_func(m // k, n // k, a, b) * (k ** (a + b + c))

        for k in range(1, q):
            x = n // (m // (k + 1) + 1)
            y = n // (m // k)

            if x == y:
                res += g_func(k, x, a, b) * (
                    _sum_pows(m // k, a + b + c)
                    - _sum_pows(m // (k + 1), a + b + c)
                )
            else:
                lo = max(m // (k + 1), n // (x + 1))
                hi = min(m // k, n // x)
                if hi > lo:
                    res += g_func(k, x, a, b) * (
                        _sum_pows(hi, a + b + c)
                        - _sum_pows(lo, a + b + c)
                    )

                if y:
                    lo2 = max(m // (k + 1), n // (y + 1))
                    hi2 = min(m // k, n // y)
                    if hi2 > lo2:
                        res += g_func(k, y, a, b) * (
                            _sum_pows(hi2, a + b + c)
                            - _sum_pows(lo2, a + b + c)
                        )

        return res

    def f_func(a: int, b: int, c: int) -> int:
        res = h_func(a, b, c)
        if a == 0:
            res += _sum_pows(n, b + c)
        if b == 0:
            res += _sum_pows(m, a + c)
        if a + b + c == 0:
            res += 1
        return res

    need = [
        (0, 0, 1),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 1),
        (0, 0, 2),
        (0, 1, 2),
        (1, 0, 2),
        (1, 1, 2),
        (0, 0, 0),
        (0, 1, 0),
        (1, 0, 0),
        (1, 1, 0),
        (3, 3, 0),
        (3, 2, 0),
        (2, 3, 0),
        (2, 2, 0),
        (3, 1, 0),
        (2, 1, 0),
        (3, 0, 0),
        (2, 0, 0),
        (1, 3, 0),
        (1, 2, 0),
        (0, 3, 0),
        (0, 2, 0),
    ]
    vals = {t: f_func(*t) for t in need}

    s001 = vals[(0, 0, 1)]
    s011 = vals[(0, 1, 1)]
    s101 = vals[(1, 0, 1)]
    s111 = vals[(1, 1, 1)]
    s002 = vals[(0, 0, 2)]
    s012 = vals[(0, 1, 2)]
    s102 = vals[(1, 0, 2)]
    s112 = vals[(1, 1, 2)]

    s000 = vals[(0, 0, 0)]
    s010 = vals[(0, 1, 0)]
    s100 = vals[(1, 0, 0)]
    s110 = vals[(1, 1, 0)]

    s330 = vals[(3, 3, 0)]
    s320 = vals[(3, 2, 0)]
    s230 = vals[(2, 3, 0)]
    s220 = vals[(2, 2, 0)]
    s310 = vals[(3, 1, 0)]
    s210 = vals[(2, 1, 0)]
    s300 = vals[(3, 0, 0)]
    s200 = vals[(2, 0, 0)]
    s130 = vals[(1, 3, 0)]
    s120 = vals[(1, 2, 0)]
    s030 = vals[(0, 3, 0)]
    s020 = vals[(0, 2, 0)]

    s_val = (
        (s012 - 11 * s230 - s210 - s030) * (m + 1)
        + (s102 - 11 * s320 - s300 - s120) * (n + 1)
        - (s112 - 11 * s330 - s310 - s130)
        - (s002 - 11 * s220 - s200 - s020) * (m + 1) * (n + 1)
    )

    c3 = (
        2
        * (
            (s010 - s011) * (m + 1)
            + (s100 - s101) * (n + 1)
            - (s000 - s001) * (m + 1) * (n + 1)
            - (s110 - s111)
        )
        + s020
        - (n + 2) * s010
        + (n + 1) * s000
        + s200
        - (m + 2) * s100
        + (m + 1) * s000
    )

    c4 = (
        (s000 * 4 - s001 * 6 + s002 * 2) * (m + 1) * (n + 1)
        + (s110 * 4 - s111 * 6 + s112 * 2)
        - (s100 * 4 - s101 * 6 + s102 * 2) * (n + 1)
        - (s010 * 4 - s011 * 6 + s012 * 2) * (m + 1)
        + s030
        - (n + 4) * s020
        + (3 * n + 5) * s010
        - 2 * (n + 1) * s000
        + s300
        - (m + 4) * s200
        + (3 * m + 5) * s100
        - 2 * (m + 1) * s000
    )

    total_q = (
        comb(p_total, 4)
        - comb(p_total, 3)
        + s_val // 3
        + (7 - 2 * p_total) * c3
        + 7 * (c4 // 2)
    )
    return total_q % mod


if __name__ == "__main__":
    print(solve())
