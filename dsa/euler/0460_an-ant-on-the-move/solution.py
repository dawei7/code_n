"""Project Euler Problem 460: An Ant on the Move.

Find F(10000), the minimum travel time for an ant on the Euclidean lattice
from (0, 1) to (d, 1) with logarithmic mean segment velocities, rounded to 9 decimal places.
"""

from math import hypot, log, sqrt
from typing import List


def _min_step_excess(
    y0: int, y1: int, h: int, logs: List[float]
) -> float:
    dy = y1 - y0
    v = dy / (logs[y1] - logs[y0])
    denom = sqrt(h * h - v * v)
    dx_star = dy * v / denom

    best = float("inf")
    k = int(dx_star)
    for dx in (k, k + 1):
        if dx < 0:
            continue
        val = hypot(dx, dy) / v - dx / h
        if val < best:
            best = val
    return best


def _best_climb_excess(h: int, window_const: int = 64) -> float:
    logs = [0.0] * (h + 1)
    for y in range(1, h + 1):
        logs[y] = log(y)

    dp = [float("inf")] * (h + 1)
    dp[1] = 0.0

    for y in range(2, h + 1):
        m_val = int(window_const * h / y) + 2
        y0_min = 1 if y - m_val < 1 else y - m_val

        best = float("inf")
        for y0 in range(y0_min, y):
            cand = dp[y0] + _min_step_excess(y0, y, h, logs)
            if cand < best:
                best = cand
        dp[y] = best

    return dp[h]


def solve(d: int = 10000) -> str:
    """Compute F(d) using convex excess DP along the hyperbolic geodesic ascent."""
    h0 = d // 2
    candidates = [h0] if (d & 1) == 0 else [h0, h0 + 1]
    best = float("inf")
    for h in candidates:
        if h < 1:
            continue
        excess = _best_climb_excess(h)
        total = 2.0 * excess + d / h
        if total < best:
            best = total
    return f"{best:.9f}"


if __name__ == "__main__":
    print(solve())
