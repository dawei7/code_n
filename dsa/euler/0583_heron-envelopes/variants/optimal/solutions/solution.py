"""Project Euler Problem 583: Heron Envelopes.

Find S(10^7), where S(p) is the sum of perimeters of all Heron envelopes
with perimeter <= p.
"""

from array import array
import math
from typing import List, Tuple


def _primitive_leg_pairs(max_leg: int) -> List[Tuple[int, int]]:
    prims: List[Tuple[int, int]] = []
    gcd = math.gcd
    isqrt = math.isqrt

    mmax = isqrt(2 * max_leg) + 1
    for m in range(2, mmax + 1):
        mm = m * m
        n_start = 1 if (m & 1) == 0 else 2
        for n in range(n_start, m, 2):
            if gcd(m, n) != 1:
                continue
            a = mm - n * n
            b = 2 * m * n
            if a > b:
                a, b = b, a
            if b <= max_leg:
                prims.append((a, b))
    return prims


def _build_u_csr(n_val: int) -> Tuple[array, array]:
    prims = _primitive_leg_pairs(n_val)
    counts = array("I", [0]) * (n_val + 1)

    for a0, b0 in prims:
        kmax = n_val // b0
        a = a0
        b = b0
        for _ in range(kmax):
            counts[a] += 1
            counts[b] += 1
            a += a0
            b += b0

    offset = array("I", [0]) * (n_val + 2)
    total = 0
    for i in range(n_val + 1):
        total += counts[i]
        offset[i + 1] = total

    vals = array("I", [0]) * total
    cursor = offset[:]

    for a0, b0 in prims:
        kmax = n_val // b0
        a = a0
        b = b0
        for _ in range(kmax):
            ia = cursor[a]
            vals[ia] = b
            cursor[a] = ia + 1

            ib = cursor[b]
            vals[ib] = a
            cursor[b] = ib + 1

            a += a0
            b += b0

    return offset, vals


def solve(p: int = 10_000_000) -> int:
    """Compute S(p) by intersecting Pythagorean flap triples with CSR leg-pair graph."""
    n_val = p // 2
    offset_u, uvals = _build_u_csr(n_val)

    isqrt = math.isqrt
    gcd = math.gcd

    def is_square(x: int) -> bool:
        r = isqrt(x)
        return r * r == x

    total = 0
    mmax = isqrt(n_val) + 1

    for m in range(2, mmax + 1):
        mm = m * m
        n_start = 1 if (m & 1) == 0 else 2
        for n in range(n_start, m, 2):
            if gcd(m, n) != 1:
                continue

            a0 = mm - n * n
            b0 = 2 * m * n
            c0 = mm + n * n

            if c0 > n_val:
                continue
            if a0 > b0:
                a0, b0 = b0, a0

            kmax = n_val // c0
            a = a0
            b = b0
            c = c0

            for _ in range(kmax):
                # Orientation 1: A = a, T = b, S = c
                a_side = a
                t_side = b
                start = offset_u[a_side]
                end = offset_u[a_side + 1]
                if start != end:
                    h_max = n_val - a_side - c
                    if h_max > t_side:
                        lo = 2 * t_side + 1
                        hi = t_side + h_max
                        four_a2 = (a_side * a_side) << 2
                        per_base = 2 * (a_side + c)
                        for u in uvals[start:end]:
                            if u < lo or u > hi:
                                continue
                            h = u - t_side
                            if h <= t_side or h > h_max:
                                continue
                            if is_square(four_a2 + h * h):
                                total += per_base + 2 * h

                # Orientation 2: A = b, T = a, S = c
                a_side = b
                t_side = a
                start = offset_u[a_side]
                end = offset_u[a_side + 1]
                if start != end:
                    h_max = n_val - a_side - c
                    if h_max > t_side:
                        lo = 2 * t_side + 1
                        hi = t_side + h_max
                        four_a2 = (a_side * a_side) << 2
                        per_base = 2 * (a_side + c)
                        for u in uvals[start:end]:
                            if u < lo or u > hi:
                                continue
                            h = u - t_side
                            if h <= t_side or h > h_max:
                                continue
                            if is_square(four_a2 + h * h):
                                total += per_base + 2 * h

                a += a0
                b += b0
                c += c0

    return total


if __name__ == "__main__":
    print(solve())
