"""Project Euler Problem 508: Integers in Base i-1.

Find B(10^15) mod 1_000_000_007, where B(L) is the sum of f(a + bi)
for all integers |a| <= L, |b| <= L (number of 1s in base i-1 representation).
"""

from functools import lru_cache
from typing import Tuple

MOD = 1_000_000_007
BRUTE_LIMIT = 4000


def _ceil_div(n: int, d: int) -> int:
    return -(-n // d)


def f_gauss(a: int, b: int) -> int:
    """Count 1s in base (i-1) representation of a + bi."""
    cnt = 0
    while a != 0 or b != 0:
        if (a ^ b) & 1:
            a -= 1
            cnt += 1
        a, b = (b - a) // 2, -(a + b) // 2
    return cnt


def _count_rect(x0: int, x1: int, y0: int, y1: int) -> int:
    if x0 > x1 or y0 > y1:
        return 0
    return (x1 - x0 + 1) * (y1 - y0 + 1)


def _count_parity(lo: int, hi: int, parity: int) -> int:
    if lo > hi:
        return 0
    first = lo if (lo & 1) == parity else lo + 1
    if first > hi:
        return 0
    return (hi - first) // 2 + 1


def _count_diamond(u0: int, u1: int, v0: int, v1: int) -> int:
    if u0 > u1 or v0 > v1:
        return 0
    eu = _count_parity(u0, u1, 0)
    ou = (u1 - u0 + 1) - eu
    ev = _count_parity(v0, v1, 0)
    ov = (v1 - v0 + 1) - ev
    return eu * ev + ou * ov


def _rect_to_diamond_bounds(
    x0: int, x1: int, y0: int, y1: int, r: int
) -> Tuple[int, int, int, int]:
    return -x1 + r, -x0 + r, y0, y1


def _diamond_to_rect_bounds(
    u0: int, u1: int, v0: int, v1: int, r: int
) -> Tuple[int, int, int, int]:
    x0 = _ceil_div(r - v1, 2)
    x1 = (r - v0) // 2
    y0 = _ceil_div(r - u1, 2)
    y1 = (r - u0) // 2
    return x0, x1, y0, y1


def _brute_rect(x0: int, x1: int, y0: int, y1: int) -> int:
    s = 0
    for a in range(x0, x1 + 1):
        for b in range(y0, y1 + 1):
            s += f_gauss(a, b)
    return s % MOD


def _brute_diamond(u0: int, u1: int, v0: int, v1: int) -> int:
    s = 0
    for u in range(u0, u1 + 1):
        parity = u & 1
        v_start = v0 if (v0 & 1) == parity else v0 + 1
        for v in range(v_start, v1 + 1, 2):
            a = (u + v) // 2
            b = (u - v) // 2
            s += f_gauss(a, b)
    return s % MOD


@lru_cache(maxsize=None)
def _sum_rect(x0: int, x1: int, y0: int, y1: int) -> int:
    if x0 > x1 or y0 > y1:
        return 0
    n = _count_rect(x0, x1, y0, y1)
    if n <= BRUTE_LIMIT:
        return _brute_rect(x0, x1, y0, y1)

    d0 = _rect_to_diamond_bounds(x0, x1, y0, y1, 0)
    d1 = _rect_to_diamond_bounds(x0, x1, y0, y1, 1)

    res = (_sum_diamond(*d0) + _sum_diamond(*d1)) % MOD
    res = (res + _count_diamond(*d1)) % MOD
    return res


@lru_cache(maxsize=None)
def _sum_diamond(u0: int, u1: int, v0: int, v1: int) -> int:
    if u0 > u1 or v0 > v1:
        return 0
    n = _count_diamond(u0, u1, v0, v1)
    if n <= BRUTE_LIMIT:
        return _brute_diamond(u0, u1, v0, v1)

    r0 = _diamond_to_rect_bounds(u0, u1, v0, v1, 0)
    r1 = _diamond_to_rect_bounds(u0, u1, v0, v1, 1)

    res = (_sum_rect(*r0) + _sum_rect(*r1)) % MOD
    res = (res + _count_rect(*r1)) % MOD
    return res


def solve(limit_l: int = 10**15, mod: int = MOD) -> int:
    """Compute B(L) mod mod using alternating rectangle-diamond domain shrinking recursion."""
    _sum_rect.cache_clear()
    _sum_diamond.cache_clear()
    total = 0
    for l_val in [limit_l]:
        total = (total + _sum_rect(-l_val, l_val, -l_val, l_val)) % mod
    return total


if __name__ == "__main__":
    print(solve())
