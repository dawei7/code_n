"""Project Euler 285: Pythagorean Odds

Find the expected value of the total score when playing 10^5 turns of the
Pythagorean Odds game with k = 1, 2, ..., 10^5, rounded to five decimal places.
"""

from __future__ import annotations

import math


def region_area(r: float) -> float:
    """Calculates the area of the region {(x, y) in [1, inf)^2 : x^2 + y^2 <= r^2}

    analytically via definite integration:
        A(r) = (r^2 / 2) * (pi / 2 - 2 * arcsin(1 / r)) - sqrt(r^2 - 1) + 1
    for r >= sqrt(2), and 0 otherwise.
    """
    if r < math.sqrt(2):
        return 0.0
    return (r * r / 2.0) * (math.pi / 2.0 - 2.0 * math.asin(1.0 / r)) - math.sqrt(r * r - 1.0) + 1.0


def solve(num_turns: int = 100000) -> str:
    """Calculates the expected total score across num_turns turns.

    For turn k:
      (x, y) = (1 + k*a, 1 + k*b) is uniformly distributed over the square [1, k+1]^2
      with total area k^2.
      A score of k is achieved iff (k - 0.5)^2 <= x^2 + y^2 < (k + 0.5)^2.
      The expected score for turn k is therefore:
          E_k = k * (Area_k / k^2) = Area_k / k
      where Area_k = region_area(k + 0.5) - region_area(k - 0.5).
    """
    total_expected_score = 0.0

    for k in range(1, num_turns + 1):
        if k == 1:
            area_k = region_area(1.5)
        else:
            area_k = region_area(k + 0.5) - region_area(k - 0.5)

        total_expected_score += area_k / k

    return f"{total_expected_score:.5f}"


if __name__ == "__main__":
    print(solve())
