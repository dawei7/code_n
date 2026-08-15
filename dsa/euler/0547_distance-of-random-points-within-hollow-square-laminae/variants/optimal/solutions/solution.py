"""Project Euler Problem 547: Distance of Random Points Within Hollow Square Laminae.

Find S(40) rounded to four decimal places, where S(n) is the sum of expected distances
between two random points in each of the possible hollow square laminae of size n.
"""

from __future__ import annotations

import math
from typing import List, Tuple

Segment = Tuple[int, int, float, float]


def _precompute_tables(
    max_n: int,
) -> Tuple[List[List[float]], List[List[float]], List[List[float]], int]:
    size = 2 * max_n + 1
    off = max_n

    a_table = [[0.0] * size for _ in range(size)]

    def a_pos(a: int, b: int) -> float:
        if a == 0 or b == 0:
            return 0.0
        r = math.hypot(a, b)
        return (
            2.0 * a * b * r
            + (a**3) * math.asinh(b / a)
            + (b**3) * math.asinh(a / b)
        ) / 6.0

    for x in range(-max_n, max_n + 1):
        sx = -1.0 if x < 0 else 1.0
        ax = abs(x)
        for y in range(-max_n, max_n + 1):
            if x == 0 or y == 0:
                a_table[x + off][y + off] = 0.0
            else:
                sy = -1.0 if y < 0 else 1.0
                a_table[x + off][y + off] = sx * sy * a_pos(ax, abs(y))

    f3_table = [[0.0] * size for _ in range(max_n + 1)]
    for a in range(0, max_n + 1):
        a2 = a * a
        a4 = a2 * a2
        for y in range(-max_n, max_n + 1):
            if a == 0:
                f3_table[a][y + off] = (y * (abs(y) ** 3)) / 4.0
            else:
                r = math.hypot(a, y)
                yy = y * y
                f3_table[a][y + off] = (
                    y * r * (2.0 * yy + 5.0 * a2)
                    + 3.0 * a4 * math.asinh(y / a)
                ) / 8.0

    p5_table = [[0.0] * (max_n + 1) for _ in range(max_n + 1)]
    for a in range(max_n + 1):
        aa = a * a
        for b in range(max_n + 1):
            p5_table[a][b] = (aa + b * b) ** 2.5

    return a_table, f3_table, p5_table, off


def _overlap_segments(
    outer_len: int, inner_len: int, left: int
) -> List[Segment]:
    right = outer_len - left - inner_len
    segs: List[Segment] = []

    a0 = -(left + inner_len)
    a1 = -left
    if a0 != a1:
        segs.append((a0, a1, 1.0, float(left + inner_len)))

    b0 = -left
    b1 = right
    if b0 != b1:
        segs.append((b0, b1, 0.0, float(inner_len)))

    c0 = right
    c1 = outer_len - left
    if c0 != c1:
        segs.append((c0, c1, -1.0, float(outer_len - left)))

    return segs


def solve(n: int = 40) -> str:
    """Compute S(n) rounded to four decimal places using exact 4D rectangle difference integration."""
    a_table, f3_table, p5_table, off = _precompute_tables(n)

    def i0(x0: int, x1: int, y0: int, y1: int) -> float:
        return (
            a_table[x1 + off][y1 + off]
            - a_table[x0 + off][y1 + off]
            - a_table[x1 + off][y0 + off]
            + a_table[x0 + off][y0 + off]
        )

    def ix(x0: int, x1: int, y0: int, y1: int) -> float:
        a1 = abs(x1)
        a0 = abs(x0)
        return (
            (f3_table[a1][y1 + off] - f3_table[a1][y0 + off])
            - (f3_table[a0][y1 + off] - f3_table[a0][y0 + off])
        ) / 3.0

    def iy(x0: int, x1: int, y0: int, y1: int) -> float:
        return ix(y0, y1, x0, x1)

    def ixy(x0: int, x1: int, y0: int, y1: int) -> float:
        ax1, ax0 = abs(x1), abs(x0)
        ay1, ay0 = abs(y1), abs(y0)
        return (
            p5_table[ax1][ay1]
            - p5_table[ax0][ay1]
            - p5_table[ax1][ay0]
            + p5_table[ax0][ay0]
        ) / 15.0

    def cross_integral(
        outer_w: int,
        outer_h: int,
        inner_w: int,
        inner_h: int,
        left: int,
        bottom: int,
    ) -> float:
        xsegs = _overlap_segments(outer_w, inner_w, left)
        ysegs = _overlap_segments(outer_h, inner_h, bottom)
        total = 0.0
        for x0, x1, mx, cx in xsegs:
            for y0, y1, my, cy in ysegs:
                base_term = cx * cy * i0(x0, x1, y0, y1)
                if mx:
                    base_term += mx * cy * ix(x0, x1, y0, y1)
                if my:
                    base_term += cx * my * iy(x0, x1, y0, y1)
                if mx and my:
                    base_term += mx * my * ixy(x0, x1, y0, y1)
                total += base_term
        return total

    i_outer = cross_integral(n, n, n, n, 0, 0)

    i_hole = [[0.0] * n for _ in range(n)]
    for w in range(1, n - 1):
        for h in range(1, n - 1):
            i_hole[w][h] = cross_integral(w, h, w, h, 0, 0)

    segx: List[List[List[Segment]]] = [
        [[] for _ in range(n + 1)] for _ in range(n + 1)
    ]
    segy: List[List[List[Segment]]] = [
        [[] for _ in range(n + 1)] for _ in range(n + 1)
    ]
    for w in range(1, n - 1):
        for left in range(0, n - w + 1):
            segx[w][left] = _overlap_segments(n, w, left)
    for h in range(1, n - 1):
        for bottom in range(0, n - h + 1):
            segy[h][bottom] = _overlap_segments(n, h, bottom)

    s_total = 0.0
    for w in range(1, n - 1):
        for h in range(1, n - 1):
            area = n * n - w * h
            inv_area2 = 1.0 / (area * area)
            ih = i_hole[w][h]

            for left in range(1, n - w):
                xsegs = segx[w][left]
                for bottom in range(1, n - h):
                    ysegs = segy[h][bottom]
                    i_cross = 0.0
                    for x0, x1, mx, cx in xsegs:
                        for y0, y1, my, cy in ysegs:
                            term = cx * cy * i0(x0, x1, y0, y1)
                            if mx:
                                term += mx * cy * ix(x0, x1, y0, y1)
                            if my:
                                term += cx * my * iy(x0, x1, y0, y1)
                            if mx and my:
                                term += mx * my * ixy(x0, x1, y0, y1)
                            i_cross += term

                    i_region = i_outer - 2.0 * i_cross + ih
                    s_total += i_region * inv_area2

    return f"{s_total:.4f}"


if __name__ == "__main__":
    print(solve())
