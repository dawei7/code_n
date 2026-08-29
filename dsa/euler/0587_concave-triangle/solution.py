"""Project Euler Problem 587: Concave Triangle.

Find the least value of n for which the concave triangle occupies less than 0.1%
of the L-section in an n-circle horizontal packing.
"""

import math


def _concave_ratio(n: int) -> float:
    area_l = 1.0 - math.pi / 4.0
    x0 = (n * (n + 1) - n * math.sqrt(2 * n)) / (n * n + 1)
    t = 1.0 - x0
    tri_area = (x0 * x0) / (2.0 * n)
    circ_area = t - 0.5 * (t * math.sqrt(1.0 - t * t) + math.asin(t))
    return (tri_area + circ_area) / area_l


def solve(target_ratio: float = 0.001) -> int:
    """Find the minimal number of circles n where the concave triangle ratio < target_ratio."""
    n = 1
    while True:
        if _concave_ratio(n) < target_ratio:
            return n
        n += 1


if __name__ == "__main__":
    print(solve())
