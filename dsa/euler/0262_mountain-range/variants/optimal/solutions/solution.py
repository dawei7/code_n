"""Project Euler 262: Mountain Range

Find the length of the shortest path between A'(200, 200, f_min) and B'(1400, 1400, f_min)
at the minimum bottleneck elevation f_min without leaving [0, 1600] x [0, 1600].
"""

from __future__ import annotations

import math


def solve() -> str:
    """Computes the minimum flight elevation f_min and the shortest path length

    around the topography obstacle using numerical boundary tracing and tangent optimization.
    """

    def h(x: float, y: float) -> float:
        poly = 5000.0 - 0.005 * (x * x + y * y + x * y) + 12.5 * (x + y)
        exp_arg = -abs(0.000001 * (x * x + y * y) - 0.0015 * (x + y) + 0.7)
        return poly * math.exp(exp_arg)

    # 1. Determine f_min: maximum of h(0, y) along the boundary x = 0
    low_y, high_y = 700.0, 1100.0
    for _ in range(80):
        m1 = low_y + (high_y - low_y) / 3
        m2 = high_y - (high_y - low_y) / 3
        if h(0.0, m1) < h(0.0, m2):
            low_y = m1
        else:
            high_y = m2
    y_opt = (low_y + high_y) / 2
    f_min = h(0.0, y_opt)

    def find_y_peak(x: float) -> float:
        low, high = 0.0, 1600.0
        for _ in range(50):
            m1 = low + (high - low) / 3
            m2 = high - (high - low) / 3
            if h(x, m1) < h(x, m2):
                low = m1
            else:
                high = m2
        return (low + high) / 2

    def get_y_lower(x: float) -> float | None:
        if x <= 0.0:
            return y_opt
        y_peak = find_y_peak(x)
        if h(x, y_peak) <= f_min:
            return None
        low, high = 0.0, y_peak
        for _ in range(50):
            mid = (low + high) / 2
            if h(x, mid) < f_min:
                low = mid
            else:
                high = mid
        return (low + high) / 2

    def get_y_upper(x: float) -> float | None:
        if x <= 0.0:
            return y_opt
        y_peak = find_y_peak(x)
        if h(x, y_peak) <= f_min:
            return None
        low, high = y_peak, 1600.0
        for _ in range(50):
            mid = (low + high) / 2
            if h(x, mid) > f_min:
                low = mid
            else:
                high = mid
        return (low + high) / 2

    def dy_lower(x: float, eps: float = 1e-4) -> float:
        y1 = get_y_lower(x + eps)
        y0 = get_y_lower(x - eps)
        if y1 is None or y0 is None:
            return 0.0
        return (y1 - y0) / (2 * eps)

    def dy_upper(x: float, eps: float = 1e-4) -> float:
        y1 = get_y_upper(x + eps)
        y0 = get_y_upper(x - eps)
        if y1 is None or y0 is None:
            return 0.0
        return (y1 - y0) / (2 * eps)

    # 2. Trace lower boundary and locate tangent point from A(200, 200)
    step_l = 0.02
    pts_lower: list[tuple[float, float]] = []
    x_curr = 0.0
    while True:
        y_val = get_y_lower(x_curr)
        if y_val is None or x_curr > 60.0:
            break
        pts_lower.append((x_curr, y_val))
        x_curr += step_l

    arc_lower = [0.0] * len(pts_lower)
    for i in range(1, len(pts_lower)):
        dx = pts_lower[i][0] - pts_lower[i - 1][0]
        dy = pts_lower[i][1] - pts_lower[i - 1][1]
        arc_lower[i] = arc_lower[i - 1] + math.hypot(dx, dy)

    best_diff_a = float("inf")
    best_idx_a = 0
    for i, (px, py) in enumerate(pts_lower):
        if px > 0.5:
            slope_secant = (py - 200.0) / (px - 200.0)
            slope_tangent = dy_lower(px)
            diff = abs(slope_secant - slope_tangent)
            if diff < best_diff_a:
                best_diff_a = diff
                best_idx_a = i

    t1 = pts_lower[best_idx_a]
    len_a = math.hypot(t1[0] - 200.0, t1[1] - 200.0) + arc_lower[best_idx_a]

    # 3. Trace upper boundary and locate tangent point from B(1400, 1400)
    step_u = 0.05
    pts_upper: list[tuple[float, float]] = []
    x_curr = 0.0
    while True:
        y_val = get_y_upper(x_curr)
        if y_val is None or x_curr > 950.0:
            break
        pts_upper.append((x_curr, y_val))
        x_curr += step_u

    arc_upper = [0.0] * len(pts_upper)
    for i in range(1, len(pts_upper)):
        dx = pts_upper[i][0] - pts_upper[i - 1][0]
        dy = pts_upper[i][1] - pts_upper[i - 1][1]
        arc_upper[i] = arc_upper[i - 1] + math.hypot(dx, dy)

    best_diff_b = float("inf")
    best_idx_b = 0
    for i, (px, py) in enumerate(pts_upper):
        if px > 10.0:
            slope_secant = (py - 1400.0) / (px - 1400.0)
            slope_tangent = dy_upper(px)
            diff = abs(slope_secant - slope_tangent)
            if diff < best_diff_b:
                best_diff_b = diff
                best_idx_b = i

    t2 = pts_upper[best_idx_b]
    len_b = arc_upper[best_idx_b] + math.hypot(t2[0] - 1400.0, t2[1] - 1400.0)

    total_length = len_a + len_b
    return f"{total_length:.3f}"


if __name__ == "__main__":
    print(solve())
