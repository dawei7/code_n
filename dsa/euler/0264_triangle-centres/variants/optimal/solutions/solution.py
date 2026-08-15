"""Project Euler 264: Triangle Centres

Find the sum of all distinct triangle perimeters <= 10^5 having:
1. All vertices on integer coordinates.
2. Circumcentre at the origin O(0, 0).
3. Orthocentre at H(5, 0).
"""

from __future__ import annotations

import math


def solve(max_perimeter: float = 100000.0) -> str:
    """Finds the sum of perimeters of all integer-coordinate triangles with circumcentre O(0, 0)

    and orthocentre H(5, 0) using algebraic complex circle parameterization.
    """
    triangles: dict[
        tuple[tuple[int, int], tuple[int, int], tuple[int, int]], float
    ] = {}

    for v in range(1, 3000):
        for u in range(1, int(math.sqrt(3) * v) + 20):
            if math.gcd(u, v) != 1:
                continue
            n = u * u - 3 * v * v
            if n == 0:
                continue
            d = u * u + v * v

            # Maximum k such that (N * k * v)^2 <= 100 * v^2 * D
            max_k_sq = (100 * d) // (n * n)
            max_k = int(math.isqrt(max_k_sq))
            if max_k_sq < 0:
                continue

            for k in range(-max_k, max_k + 1):
                y3 = k * v
                cap_y = n * y3
                rem = 100 * v * v * d - cap_y * cap_y
                if rem < 0:
                    continue
                cap_x = math.isqrt(rem)
                if cap_x * cap_x != rem:
                    continue

                for sx in [cap_x, -cap_x] if cap_x != 0 else [0]:
                    if (sx + 5 * d) % n != 0:
                        continue
                    x3 = (sx + 5 * d) // n

                    # Verify v divides (5 - x3)
                    if (5 - x3) % v != 0:
                        continue

                    val_x1 = 5 - x3 + (y3 * u) // v
                    val_y1 = -y3 + ((5 - x3) * u) // v
                    val_x2 = 5 - x3 - (y3 * u) // v
                    val_y2 = -y3 - ((5 - x3) * u) // v

                    if val_x1 % 2 == 0 and val_y1 % 2 == 0:
                        x1, y1 = val_x1 // 2, val_y1 // 2
                        x2, y2 = val_x2 // 2, val_y2 // 2

                        pts = tuple(
                            sorted([(x1, y1), (x2, y2), (x3, y3)])
                        )
                        if len(set(pts)) == 3:
                            r2 = x3 * x3 + y3 * y3
                            c = math.sqrt(3 * r2 + 10 * x3 - 25)
                            a = math.sqrt(3 * r2 + 10 * x1 - 25)
                            b = math.sqrt(3 * r2 + 10 * x2 - 25)
                            p = a + b + c
                            if p <= max_perimeter:
                                triangles[pts] = p

    total_perimeter = sum(triangles.values())
    return f"{total_perimeter:.4f}"


if __name__ == "__main__":
    print(solve())
