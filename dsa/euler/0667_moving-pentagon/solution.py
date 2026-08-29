"""Project Euler Problem 667: Moving Pentagon.

Find the largest area of an equilateral pentagon that can pass through a unit-width
L-shaped corridor, rounded to 10 decimal places.
"""

import math
from typing import List, Optional, Tuple

Point = Tuple[float, float]


def _heron(a: float, b: float, c: float) -> float:
    s = (a + b + c) * 0.5
    v = s * (s - a) * (s - b) * (s - c)
    return math.sqrt(v) if v > 0.0 else 0.0


def _rotate_points(points: List[Point], theta: float) -> List[Point]:
    c = math.cos(theta)
    s = math.sin(theta)
    return [(c * x - s * y, s * x + c * y) for (x, y) in points]


def _min_x_above_y(points: List[Point], ythr: float) -> float:
    mn = float("inf")
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        if y1 >= ythr and x1 < mn:
            mn = x1
        if y2 >= ythr and x2 < mn:
            mn = x2
        dy = y2 - y1
        if dy != 0.0:
            t = (ythr - y1) / dy
            if 0.0 <= t <= 1.0:
                x = x1 + (x2 - x1) * t
                if x < mn:
                    mn = x
    return mn


def _build_unit_pentagon(r: float) -> Optional[List[Point]]:
    if not (0.5 < r < 2.0):
        return None
    h2 = r * r - 0.25
    if h2 <= 0.0:
        return None
    h = math.sqrt(h2)

    a_pt = (0.0, 0.0)
    e_pt = (1.0, 0.0)
    c_pt = (0.5, h)

    d = r
    if d >= 2.0:
        return None
    k2 = 1.0 - (d * 0.5) * (d * 0.5)
    if k2 <= 0.0:
        return None
    k = math.sqrt(k2)

    mx = (a_pt[0] + c_pt[0]) * 0.5
    my = (a_pt[1] + c_pt[1]) * 0.5

    ux = -(c_pt[1] - a_pt[1]) / d
    uy = (c_pt[0] - a_pt[0]) / d

    b_pt = (mx + k * ux, my + k * uy)
    d_pt = (1.0 - b_pt[0], b_pt[1])
    return [a_pt, b_pt, c_pt, d_pt, e_pt]


def _base_area(r: float) -> float:
    return 2.0 * _heron(1.0, 1.0, r) + _heron(r, r, 1.0)


def _precompute_rotations(points: List[Point], thetas: List[float]):
    out = []
    for th in thetas:
        pts = _rotate_points(points, th)
        miny = min(y for (_, y) in pts)
        maxx = max(x for (x, _) in pts)
        out.append((pts, miny, maxx))
    return out


def _clearance_for_theta(
    points_rot: List[Point],
    min_y: float,
    max_x: float,
    scale: float,
    eps_y: float,
) -> float:
    ythr = min_y + (1.0 + eps_y) / scale
    x_min = _min_x_above_y(points_rot, ythr)
    if x_min == float("inf"):
        return float("inf")
    return 1.0 + scale * (x_min - max_x)


def _min_clearance(
    points: List[Point],
    precomp,
    thetas: List[float],
    scale: float,
    eps_y: float,
    local_k: int = 3,
    local_iters: int = 22,
) -> float:
    vals = []
    best = float("inf")
    for pts, miny, maxx in precomp:
        cl = _clearance_for_theta(pts, miny, maxx, scale, eps_y)
        vals.append(cl)
        if cl < best:
            best = cl

    idx_sorted = sorted(range(len(thetas)), key=lambda i: vals[i])[:local_k]
    phi = (math.sqrt(5.0) - 1.0) / 2.0

    def f_eval(th):
        pts = _rotate_points(points, th)
        miny = min(y for (_, y) in pts)
        maxx = max(x for (x, _) in pts)
        return _clearance_for_theta(pts, miny, maxx, scale, eps_y)

    for idx in idx_sorted:
        a = thetas[max(0, idx - 1)]
        b = thetas[min(len(thetas) - 1, idx + 1)]
        if b - a <= 1e-15:
            continue
        c = b - (b - a) * phi
        d = a + (b - a) * phi
        fc = f_eval(c)
        fd = f_eval(d)
        for _ in range(local_iters):
            if fc < fd:
                b = d
                d = c
                fd = fc
                c = b - (b - a) * phi
                fc = f_eval(c)
            else:
                a = c
                c = d
                fc = fd
                d = a + (b - a) * phi
                fd = f_eval(d)
        best = min(best, fc, fd)

    return best


def _max_scale(
    points: List[Point], n_theta: int, bisection_iters: int, eps_y: float
) -> float:
    thetas = [(math.pi / 2.0) * i / (n_theta - 1) for i in range(n_theta)]
    precomp = _precompute_rotations(points, thetas)

    def feasible(s: float) -> bool:
        mc = _min_clearance(points, precomp, thetas, s, eps_y)
        return mc >= -1e-13

    lo, hi = 0.0, 2.0
    while feasible(hi):
        hi *= 1.3
        if hi > 50.0:
            break

    for _ in range(bisection_iters):
        mid = (lo + hi) * 0.5
        if feasible(mid):
            lo = mid
        else:
            hi = mid
    return lo


def _objective(r: float, mode: str) -> Tuple[float, float]:
    pts = _build_unit_pentagon(r)
    if pts is None:
        return -1.0, 0.0
    if mode == "coarse":
        s = _max_scale(pts, n_theta=450, bisection_iters=35, eps_y=1e-12)
    elif mode == "mid":
        s = _max_scale(pts, n_theta=1400, bisection_iters=55, eps_y=1e-14)
    elif mode == "fine":
        s = _max_scale(pts, n_theta=8000, bisection_iters=75, eps_y=1e-15)
    else:
        raise ValueError("bad mode")
    return _base_area(r) * s * s, s


def _golden_max(func, a: float, b: float, iters: int) -> Tuple[float, float]:
    phi = (math.sqrt(5.0) - 1.0) / 2.0
    c = b - (b - a) * phi
    d = a + (b - a) * phi
    fc = func(c)
    fd = func(d)
    for _ in range(iters):
        if fc > fd:
            b = d
            d = c
            fd = fc
            c = b - (b - a) * phi
            fc = func(c)
        else:
            a = c
            c = d
            fc = fd
            d = a + (b - a) * phi
            fd = func(d)
    if fc > fd:
        return c, fc
    return d, fd


def solve() -> str:
    """Find the largest area of an equilateral pentagon fitting through a unit L-shaped corridor."""
    rmin, rmax = 0.75, 1.05
    steps = 240
    best_r = 0.9
    best_val = -1.0

    for i in range(steps + 1):
        r = rmin + (rmax - rmin) * i / steps
        val, _ = _objective(r, "coarse")
        if val > best_val:
            best_val = val
            best_r = r

    cache = {}

    def f_mid(rr: float) -> float:
        key = round(rr, 15)
        if key in cache:
            return cache[key]
        val, _ = _objective(rr, "mid")
        cache[key] = val
        return val

    step_width = (rmax - rmin) / steps
    a = best_r - step_width
    b = best_r + step_width
    r1, _ = _golden_max(f_mid, a, b, iters=26)

    sub_step = (b - a) * 0.1
    a2 = r1 - sub_step
    b2 = r1 + sub_step
    r2, _ = _golden_max(f_mid, a2, b2, iters=35)

    final_area, _ = _objective(r2, "fine")
    return f"{final_area:.10f}"


if __name__ == "__main__":
    print(solve())
