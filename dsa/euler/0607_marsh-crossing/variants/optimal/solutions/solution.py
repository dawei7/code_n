"""Project Euler Problem 607: Marsh Crossing.

Find the shortest time in days to travel from A to B across the 5-strip marsh,
rounded to 10 decimal places.
"""

import math
from typing import List


def solve(total_distance: float = 100.0) -> str:
    """Compute the minimum traversal time across refractive layers using Snell's Law and bisection."""
    sqrt2 = math.sqrt(2)
    w_total = 50.0 * sqrt2

    widths: List[float] = [
        25.0 * sqrt2 - 25.0,
        10.0,
        10.0,
        10.0,
        10.0,
        10.0,
        25.0 * sqrt2 - 25.0,
    ]
    speeds: List[float] = [10.0, 9.0, 8.0, 7.0, 6.0, 5.0, 10.0]

    def parallel_disp(k_val: float) -> float:
        total_w = 0.0
        for w, v in zip(widths, speeds):
            sin_th = k_val * v
            if sin_th >= 1.0:
                return float("inf")
            tan_th = sin_th / math.sqrt(1.0 - sin_th * sin_th)
            total_w += w * tan_th
        return total_w

    lo, hi = 0.0, 1.0 / max(speeds) - 1e-15
    for _ in range(120):
        mid = (lo + hi) / 2.0
        if parallel_disp(mid) < w_total:
            lo = mid
        else:
            hi = mid

    k_const = (lo + hi) / 2.0
    total_time = 0.0
    for w, v in zip(widths, speeds):
        sin_th = k_const * v
        cos_th = math.sqrt(1.0 - sin_th * sin_th)
        total_time += w / (v * cos_th)

    return f"{total_time:.10f}"


if __name__ == "__main__":
    print(solve())
