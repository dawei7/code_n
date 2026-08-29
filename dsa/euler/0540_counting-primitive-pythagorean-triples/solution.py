"""Project Euler Problem 540: Counting Primitive Pythagorean Triples.

Find P(3141592653589793), where P(n) is the number of primitive Pythagorean triples
with hypotenuse c <= n.
"""

from __future__ import annotations

import math
from typing import List

N = 3141592653589793


def _icbrt(n: int) -> int:
    if n <= 1:
        return n
    r = int(round(n ** (1.0 / 3.0)))
    while (r + 1) ** 3 <= n:
        r += 1
    while r**3 > n:
        r -= 1
    return r


def _odd_ge3_count_le(n: int) -> int:
    return (n - 1) // 2 if n >= 3 else 0


def _raw_opposite_parity_count(limit: int) -> int:
    if limit < 5:
        return 0

    isqrt = math.isqrt
    full = (1 + isqrt(2 * limit - 1)) // 2
    while (full + 1) * (full + 1) + full * full <= limit:
        full += 1
    while full * full + (full - 1) * (full - 1) > limit:
        full -= 1

    k = full // 2
    total = k * k

    m = 2 * k + 1
    if m * m > limit:
        return total

    y = isqrt(limit - m * m)
    while m * m + 1 <= limit:
        rem = limit - m * m
        while y * y > rem:
            y -= 1

        nmax = y if y < m else m - 1
        if m & 1:
            total += nmax // 2
        else:
            total += (nmax + 1) // 2
        m += 1

    return total


def _small_primitive_table(limit: int) -> List[int]:
    isqrt = math.isqrt
    small = [0] * (limit + 1)

    for x in range(1, limit + 1):
        total = _raw_opposite_parity_count(x)
        max_d = isqrt(x)
        split = _icbrt(x)

        d = 3
        while d <= max_d and d <= split:
            total -= small[x // (d * d)]
            d += 2

        if d <= max_d:
            max_z = x // (d * d)
            for z in range(1, max_z + 1):
                hi = _odd_ge3_count_le(isqrt(x // z))
                lo = _odd_ge3_count_le(isqrt(x // (z + 1)))
                total -= (hi - lo) * small[z]

        small[x] = total

    return small


def solve(limit: int = N) -> int:
    """Compute P(limit) using sublinear Dirichlet hyperbola sieve and odd-divisor Möbius inversion."""
    if limit < 5:
        return 0

    isqrt = math.isqrt
    cube = _icbrt(limit)
    small = _small_primitive_table(cube)

    tail = [0] * (cube + 1)
    s_max = isqrt(limit // 5)
    for t in range(1, cube + 1, 2):
        s = (cube // t + 1) * t
        if s % 2 == 0:
            s += t

        acc = 0
        step = 2 * t
        while s <= s_max:
            acc += small[limit // (s * s)]
            s += step
        tail[t] = acc

    transformed = [0] * (cube + 1)
    start = cube if cube & 1 else cube - 1
    for t in range(start, 0, -2):
        x = limit // (t * t)
        total = _raw_opposite_parity_count(x)

        s = 3 * t
        step = 2 * t
        while s <= cube:
            total -= transformed[s]
            s += step

        total -= tail[t]
        transformed[t] = total

    return transformed[1]


if __name__ == "__main__":
    print(solve())
