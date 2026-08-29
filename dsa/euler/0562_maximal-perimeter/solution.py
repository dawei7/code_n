"""Project Euler Problem 562: Maximal Perimeter.

Find T(10^7) rounded to the nearest integer, where T(r) = R/r, and R is the circumradius
of the maximal perimeter empty lattice triangle inside a circle of radius r.
"""

import math
from typing import List, Optional, Tuple

LIMIT_DEFICIT = 8000


def _egcd(a: int, b: int) -> Tuple[int, int, int]:
    x0, y0 = 1, 0
    x1, y1 = 0, 1
    while b:
        q = a // b
        a, b = b, a - q * b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def _ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def _boundary_points_near_circle(
    r: int, deficit_limit: int
) -> Tuple[List[int], List[int]]:
    r2 = r * r
    x = r
    x2 = x * x
    y2 = 0

    xs: List[int] = []
    ys: List[int] = []

    for y in range(r + 1):
        while x2 + y2 > r2:
            x -= 1
            x2 = x * x

        deficit = r2 - x2 - y2
        if deficit <= deficit_limit:
            xs.append(x)
            ys.append(y)

        y2 += 2 * y + 1

    return xs, ys


def _best_base_candidates(
    xs: List[int], ys: List[int]
) -> Tuple[int, List[Tuple[int, int, int, int]]]:
    m = len(xs)
    gcd = math.gcd

    best_u2 = -1
    best: List[Tuple[int, int, int, int]] = []

    for i in range(m):
        xi = xs[i]
        yi = ys[i]
        for j in range(i + 1, m):
            ux = xi + xs[j]
            uy = yi + ys[j]
            u2 = ux * ux + uy * uy

            if u2 < best_u2:
                continue
            if ((ux | uy) & 1) == 0:
                continue
            if gcd(ux, uy) != 1:
                continue

            if u2 > best_u2:
                best_u2 = u2
                best = [(i, j, ux, uy)]
            elif u2 == best_u2:
                best.append((i, j, ux, uy))

    if best_u2 < 0:
        raise RuntimeError("No primitive base found.")
    return best_u2, best


def _best_triangle_for_base(
    r: int, ax: int, ay: int, ux: int, uy: int
) -> Tuple[int, int, int, float]:
    r2 = r * r
    s1 = ux * ux + uy * uy

    g, s, t = _egcd(abs(ux), abs(uy))
    if g != 1:
        raise RuntimeError("Base vector not primitive.")
    if ux < 0:
        s = -s
    if uy < 0:
        t = -t

    v0x, v0y = -t, s
    best_sides: Optional[Tuple[int, int, int]] = None
    best_per = -1.0

    isqrt = math.isqrt
    sqrt = math.sqrt

    for sign in (1, -1):
        bvx, bvy = sign * v0x, sign * v0y

        p0x = ax + bvx
        p0y = ay + bvy
        pu = p0x * ux + p0y * uy
        pp = p0x * p0x + p0y * p0y

        uu = s1
        disc = pu * pu - uu * (pp - r2)
        if disc < 0:
            continue
        root = isqrt(disc)

        k_lo = _ceil_div(-pu - root, uu)
        k_hi = (-pu + root) // uu

        for k in range(k_lo, k_hi + 1):
            vx = bvx + k * ux
            vy = bvy + k * uy
            cx = ax + vx
            cy = ay + vy
            if cx * cx + cy * cy > r2:
                continue

            s2 = vx * vx + vy * vy
            wx = ux - vx
            wy = uy - vy
            s3 = wx * wx + wy * wy

            per = sqrt(s1) + sqrt(s2) + sqrt(s3)
            if per > best_per:
                best_per = per
                best_sides = (s1, s2, s3)

    if best_sides is None:
        raise RuntimeError("No feasible third vertex.")
    return best_sides[0], best_sides[1], best_sides[2], best_per


def _round_sqrt_rational(numer: int, den: int) -> int:
    k = math.isqrt(numer // den)
    t = 2 * k + 1
    if 4 * numer >= den * t * t:
        return k + 1
    return k


def solve(r: int = 10_000_000, deficit_limit: int = LIMIT_DEFICIT) -> int:
    """Compute round(T(r)) for disk of radius r using unimodular primitive base search."""
    xs, ys = _boundary_points_near_circle(r, deficit_limit)
    _, base_cands = _best_base_candidates(xs, ys)

    best_sides: Optional[Tuple[int, int, int]] = None
    best_per = -1.0

    for i, j, ux, uy in base_cands:
        for ax, ay in [(-xs[i], -ys[i]), (-xs[j], -ys[j])]:
            try:
                s1, s2, s3, per = _best_triangle_for_base(
                    r, ax, ay, ux, uy
                )
            except RuntimeError:
                continue
            if per > best_per:
                best_per = per
                best_sides = (s1, s2, s3)

    if best_sides is None:
        raise RuntimeError("No triangle found.")

    s1, s2, s3 = best_sides
    numer = s1 * s2 * s3
    den = 4 * r * r
    return _round_sqrt_rational(numer, den)


if __name__ == "__main__":
    print(solve())
