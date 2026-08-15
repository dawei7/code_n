"""Project Euler Problem 572: Idempotent Matrices.

Find C(200), where C(n) is the number of 3x3 integer matrices M with M^2 = M
and all entries in [-n, n].
"""

from functools import lru_cache
import math
from typing import List, Tuple

Range = Tuple[int, int]
Triple = Tuple[int, int, int]


def _floor_div(a: int, b: int) -> int:
    return a // b


def _ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def _div_interval(low: int, high: int, coef: int) -> Range:
    if coef > 0:
        return _ceil_div(low, coef), _floor_div(high, coef)
    return _ceil_div(high, coef), _floor_div(low, coef)


def _t_bounds(base: int, step: int, low: int, high: int) -> Range:
    if step > 0:
        tmin = _ceil_div(low - base, step)
        tmax = _floor_div(high - base, step)
    else:
        tmin = _ceil_div(high - base, step)
        tmax = _floor_div(low - base, step)
    return tmin, tmax


@lru_cache(maxsize=None)
def _egcd(a: int, b: int) -> Tuple[int, int, int]:
    if b == 0:
        if a == 0:
            return 0, 0, 0
        return abs(a), (1 if a > 0 else -1), 0
    g, x1, y1 = _egcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


def _count_2d(
    a: int, b: int, c: int, ly: int, ry: int, lz: int, rz: int
) -> int:
    if ly > ry or lz > rz:
        return 0

    if a == 0:
        if b == 0:
            return (ry - ly + 1) * (rz - lz + 1) if c == 0 else 0
        if c % b != 0:
            return 0
        z = c // b
        return (ry - ly + 1) if lz <= z <= rz else 0

    if b == 0:
        if c % a != 0:
            return 0
        y = c // a
        return (rz - lz + 1) if ly <= y <= ry else 0

    g, xg, yg = _egcd(a, b)
    if g == 0 or c % g != 0:
        return 0

    k = c // g
    y0 = xg * k
    z0 = yg * k
    step_y = b // g
    step_z = -a // g

    lo1, hi1 = _t_bounds(y0, step_y, ly, ry)
    lo2, hi2 = _t_bounds(z0, step_z, lz, rz)
    lo = max(lo1, lo2)
    hi = min(hi1, hi2)
    return max(0, hi - lo + 1)


def _count_3d_linear(a: int, b: int, c: int, ranges: List[Range]) -> int:
    (lx, rx), (ly, ry), (lz, rz) = ranges
    if lx > rx or ly > ry or lz > rz:
        return 0

    if a == 0 and b == 0 and c == 0:
        return 0

    nnz = (a != 0) + (b != 0) + (c != 0)

    if nnz == 1:
        if a != 0:
            if 1 % a != 0:
                return 0
            x = 1 // a
            return (ry - ly + 1) * (rz - lz + 1) if lx <= x <= rx else 0
        if b != 0:
            if 1 % b != 0:
                return 0
            y = 1 // b
            return (rx - lx + 1) * (rz - lz + 1) if ly <= y <= ry else 0
        if 1 % c != 0:
            return 0
        z = 1 // c
        return (rx - lx + 1) * (ry - ly + 1) if lz <= z <= rz else 0

    if nnz == 2:
        if a == 0:
            return _count_2d(b, c, 1, ly, ry, lz, rz) * (rx - lx + 1)
        if b == 0:
            return _count_2d(a, c, 1, lx, rx, lz, rz) * (ry - ly + 1)
        return _count_2d(a, b, 1, lx, rx, ly, ry) * (rz - lz + 1)

    lens = [(rx - lx + 1, 0), (ry - ly + 1, 1), (rz - lz + 1, 2)]
    lens.sort()
    idx = lens[0][1]

    total = 0
    if idx == 0:
        for x in range(lx, rx + 1):
            total += _count_2d(b, c, 1 - a * x, ly, ry, lz, rz)
    elif idx == 1:
        for y in range(ly, ry + 1):
            total += _count_2d(a, c, 1 - b * y, lx, rx, lz, rz)
    else:
        for z in range(lz, rz + 1):
            total += _count_2d(a, b, 1 - c * z, lx, rx, ly, ry)

    return total


def _triples_up_to(t_val: int) -> List[Triple]:
    res: List[Triple] = []
    for a in range(-t_val, t_val + 1):
        for b in range(-t_val, t_val + 1):
            for c in range(-t_val, t_val + 1):
                if a == 0 and b == 0 and c == 0:
                    continue
                res.append((a, b, c))
    return res


def _v_ranges_for_rank2(u: Triple, n: int) -> List[Range]:
    uvals = u
    low = 1 - n
    high = 1 + n

    rng: List[Range] = []
    for j in range(3):
        off = n
        for i in range(3):
            if i == j:
                continue
            ui = uvals[i]
            if ui != 0:
                off = min(off, n // abs(ui))

        l_bound = -off
        r_bound = off

        uj = uvals[j]
        if uj != 0:
            ld, rd = _div_interval(low, high, uj)
            if ld > rd:
                ld, rd = rd, ld
            l_bound = max(l_bound, ld)
            r_bound = min(r_bound, rd)

        rng.append((l_bound, r_bound))

    return rng


def solve(n: int = 200) -> int:
    """Compute C(n) using rank-1 and rank-2 outer product decomposition."""
    t_val = math.isqrt(n)
    us = _triples_up_to(t_val)
    cube_t = [(-t_val, t_val), (-t_val, t_val), (-t_val, t_val)]

    # Rank 1 calculation
    s_sum = 0
    overlap_r1 = 0
    for a, b, c in us:
        u_max = max(abs(a), abs(b), abs(c))
        b_bound = n // u_max
        cube_b = [(-b_bound, b_bound), (-b_bound, b_bound), (-b_bound, b_bound)]

        s_sum += _count_3d_linear(a, b, c, cube_b)
        overlap_r1 += _count_3d_linear(a, b, c, cube_t)

    rank1_count = (2 * s_sum - overlap_r1) // 2

    # Rank 2 calculation
    sa_sum = 0
    overlap_r2 = 0
    for u in us:
        a, b, c = u
        vr = _v_ranges_for_rank2(u, n)

        if vr[0][0] > vr[0][1] or vr[1][0] > vr[1][1] or vr[2][0] > vr[2][1]:
            continue

        sa_sum += _count_3d_linear(a, b, c, vr)

        vr2: List[Range] = []
        ok = True
        for l_bound, r_bound in vr:
            l2 = max(l_bound, -t_val)
            r2 = min(r_bound, t_val)
            if l2 > r2:
                ok = False
                break
            vr2.append((l2, r2))

        if ok:
            overlap_r2 += _count_3d_linear(a, b, c, vr2)

    rank2_count = (2 * sa_sum - overlap_r2) // 2

    # Total: Zero matrix (1), Identity matrix (1), plus rank-1 and rank-2 matrices
    return 2 + rank1_count + rank2_count


if __name__ == "__main__":
    print(solve())
