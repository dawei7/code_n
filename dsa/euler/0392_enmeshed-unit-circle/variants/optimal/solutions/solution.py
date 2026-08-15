"""Project Euler Problem 392: Enmeshed Unit Circle.

Find the minimal area occupied by red cells in an (N+1)x(N+1) grid covering the unit circle
for N=400, rounded to 10 decimal places.
"""

from math import sqrt
from typing import List


def _f(x_val: float) -> float:
    """Return sqrt(1 - x^2) for x in [0, 1]."""
    return sqrt(max(0.0, 1.0 - x_val * x_val))


def _end_x(m: int, x1: float) -> float:
    """Generate x_m using the Euler-Lagrange optimality recurrence."""
    if not (0.0 < x1 < 1.0):
        return float("inf")

    x_cur = x1
    g_prev = 1.0

    for _ in range(1, m):
        if x_cur <= 0.0:
            return float("inf")
        if x_cur >= 1.0:
            return x_cur

        g_cur = _f(x_cur)
        x_next = x_cur + (g_prev - g_cur) * g_cur / x_cur
        if not (x_cur < x_next):
            return float("inf")

        x_cur = x_next
        g_prev = g_cur

    return x_cur


def solve(n: int = 400) -> str:
    """Compute minimal red cell area for N inner gridlines rounded to 10 decimal places."""
    m = n // 2 + 1

    lo = 1e-6
    while _end_x(m, lo) >= 1.0:
        lo *= 0.5

    hi = 0.9
    while _end_x(m, hi) <= 1.0:
        hi = (hi + 1.0) / 2.0

    for _ in range(200):
        mid = (lo + hi) / 2.0
        if _end_x(m, mid) > 1.0:
            hi = mid
        else:
            lo = mid

    x1 = (lo + hi) / 2.0

    # Build optimal grid
    xs: List[float] = [0.0, x1]
    g_prev = 1.0
    for k in range(1, m):
        xk = xs[k]
        gk = _f(xk)
        xs.append(xk + (g_prev - gk) * gk / xk)
        g_prev = gk

    area_q = sum((xs[i + 1] - xs[i]) * _f(xs[i]) for i in range(m))
    area_total = 4.0 * area_q
    return f"{area_total:.10f}"


if __name__ == "__main__":
    print(solve())
