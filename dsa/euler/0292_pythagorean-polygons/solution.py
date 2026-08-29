"""Project Euler 292: Pythagorean Polygons

Find P(120), the number of distinct pythagorean polygons with perimeter <= 120 (up to translation).
"""

from __future__ import annotations

import math


def solve(max_perimeter: int = 120) -> str:
    """Calculates P(max_perimeter), the number of convex lattice polygons with integer edge lengths

    and perimeter <= max_perimeter (distinct up to translation).

    Every convex Pythagorean polygon is uniquely determined by the sorted angular sequence of its
    edge vectors v_i = (x_i, y_i) with integer lengths h_i = sqrt(x_i^2 + y_i^2).
    - At most one vector is chosen from each ray direction.
    - Closed loop: sum(x_i) = 0 and sum(y_i) = 0.
    - Total perimeter: sum(h_i) <= max_perimeter.
    - Degenerate 1D 2-vertex segments (opposite collinear vectors) are subtracted.
    """
    primitive_rays: list[tuple[int, int, int]] = []
    for dx in range(-max_perimeter, max_perimeter + 1):
        for dy in range(-max_perimeter, max_perimeter + 1):
            if dx == 0 and dy == 0:
                continue
            if math.gcd(abs(dx), abs(dy)) != 1:
                continue
            h2 = dx * dx + dy * dy
            h = math.isqrt(h2)
            if h * h == h2 and h <= max_perimeter:
                primitive_rays.append((dx, dy, h))

    # Sort rays strictly by angle in (-pi, pi]
    primitive_rays.sort(key=lambda r: math.atan2(r[1], r[0]))

    ray_choices: list[list[tuple[int, int, int]]] = []
    for dx, dy, h in primitive_rays:
        choices = [(0, 0, 0)]
        for k in range(1, max_perimeter // h + 1):
            choices.append((k * dx, k * dy, k * h))
        ray_choices.append(choices)

    # Dynamic Programming: dp[(x, y, perimeter)] = count
    dp: dict[tuple[int, int, int], int] = {(0, 0, 0): 1}

    for choices in ray_choices:
        next_dp: dict[tuple[int, int, int], int] = {}
        for (x, y, p), count in dp.items():
            for vx, vy, vh in choices:
                np = p + vh
                rem_p = max_perimeter - np
                if rem_p >= 0:
                    nx = x + vx
                    ny = y + vy
                    # Euclidean distance pruning: (nx, ny) must be able to return to (0, 0)
                    if nx * nx + ny * ny <= rem_p * rem_p:
                        k_state = (nx, ny, np)
                        next_dp[k_state] = next_dp.get(k_state, 0) + count
        dp = next_dp

    total_closed = 0
    for (x, y, p), count in dp.items():
        if x == 0 and y == 0 and p > 0:
            total_closed += count

    # Subtract degenerate 1D 2-vertex segments
    degenerate_segments = 0
    for dx, dy, h in primitive_rays:
        if dy > 0 or (dy == 0 and dx > 0):
            degenerate_segments += max_perimeter // (2 * h)

    ans = total_closed - degenerate_segments
    return str(ans)


if __name__ == "__main__":
    print(solve())
