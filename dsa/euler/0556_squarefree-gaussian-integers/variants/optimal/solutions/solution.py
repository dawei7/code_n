"""Project Euler Problem 556: Squarefree Gaussian Integers.

Find f(10^14), where f(n) is the count of proper squarefree Gaussian integers
with a^2 + b^2 <= n (a > 0, b >= 0).
"""

from array import array
from math import isqrt
from typing import Dict, Tuple


def _build_spf(limit: int) -> array:
    spf = array("I", [0]) * (limit + 1)
    if limit >= 0:
        spf[0] = 1
    if limit >= 1:
        spf[1] = 1

    r = isqrt(limit)
    for i in range(2, r + 1):
        if spf[i] == 0:
            spf[i] = i
            start = i * i
            step = i
            for j in range(start, limit + 1, step):
                if spf[j] == 0:
                    spf[j] = i

    for i in range(2, limit + 1):
        if spf[i] == 0:
            spf[i] = i
    return spf


def _precompute(limit: int) -> Tuple[array, array]:
    spf = _build_spf(limit)

    f_table = array("h", [0]) * (limit + 1)
    f_table[1] = 1

    for n in range(2, limit + 1):
        p = spf[n]
        rest = n // p
        e = 1
        while rest % p == 0:
            rest //= p
            e += 1

        if p == 2:
            coef = -1 if e == 1 else 0
        elif (p & 3) == 1:
            coef = -2 if e == 1 else (1 if e == 2 else 0)
        else:
            coef = -1 if e == 2 else 0

        f_table[n] = 0 if coef == 0 else f_table[rest] * coef

    prefix_f = array("q", [0]) * (limit + 1)
    s = 0
    for i in range(1, limit + 1):
        s += f_table[i]
        prefix_f[i] = s

    r2 = array("H", [0]) * (limit + 1)
    if limit >= 1:
        r2[1] = 4

    for n in range(2, limit + 1):
        p = spf[n]
        rest = n // p
        e = 1
        while rest % p == 0:
            rest //= p
            e += 1

        base = r2[rest]
        if base == 0:
            r2[n] = 0
        elif p == 2:
            r2[n] = base
        elif (p & 3) == 1:
            r2[n] = base * (e + 1)
        else:
            r2[n] = 0 if (e & 1) else base

    a_small = array("I", [0]) * (limit + 1)
    acc = 0
    for n in range(1, limit + 1):
        acc += r2[n]
        a_small[n] = acc

    return prefix_f, a_small


def _lattice_points_nonzero(x: int) -> int:
    if x <= 0:
        return 0
    big_r = isqrt(x)
    b = big_r
    bb = b * b
    s = 0
    for a in range(1, big_r + 1):
        aa = a * a
        while aa + bb > x:
            b -= 1
            bb = b * b
        s += b
    return (s << 2) + (big_r << 2)


def solve(n: int = 10**14) -> int:
    """Compute f(n) using Gaussian Möbius norm aggregation and Gauss circle boundary walks."""
    small_limit = isqrt(n)
    prefix_f, a_small = _precompute(small_limit)

    cache: Dict[int, int] = {}
    total = 0
    m = 1

    while m <= small_limit:
        x = n // (m * m)
        if x == 0:
            break

        m2 = isqrt(n // x)
        if m2 > small_limit:
            m2 = small_limit

        sum_f = prefix_f[m2] - prefix_f[m - 1]
        if sum_f:
            if x <= small_limit:
                a_val = a_small[x]
            else:
                a_val = cache.get(x)
                if a_val is None:
                    a_val = _lattice_points_nonzero(x)
                    cache[x] = a_val
            total += sum_f * a_val

        m = m2 + 1

    return total // 4


if __name__ == "__main__":
    print(solve())
