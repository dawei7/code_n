"""Project Euler 332: Spherical Triangles

Find sum_{r=1}^{50} A(r) rounded to six decimal places, where A(r) is the area
of the smallest non-degenerate spherical triangle with integer lattice vertices on x^2 + y^2 + z^2 = r^2.
"""

from __future__ import annotations

import math


def solve(max_r: int = 50) -> str:
    """Calculates sum_{r=1}^{max_r} A(r) using Euler's solid angle / Oosterom-Strackee formula

    Area(A, B, C) = 2 * r^2 * arctan(|det(A, B, C)| / (r^3 + r * (A.B + B.C + C.A))).
    """
    total_area = 0.0

    for r in range(1, max_r + 1):
        r2 = r * r
        r3 = r * r * r

        # 1. Generate all integer lattice points Z(r) on x^2 + y^2 + z^2 = r^2
        pts: list[tuple[int, int, int]] = []
        for x in range(-r, r + 1):
            rem = r2 - x * x
            for y in range(-r, r + 1):
                rem2 = rem - y * y
                if rem2 >= 0:
                    z = math.isqrt(rem2)
                    if z * z == rem2:
                        pts.append((x, y, z))
                        if z > 0:
                            pts.append((x, y, -z))

        n = len(pts)
        if n < 3:
            continue

        min_area = float("inf")
        pts.sort()

        # 2. Iterate all vertex triples (A, B, C) in Z(r)
        for i in range(n):
            ax, ay, az = pts[i]
            for j in range(i + 1, n):
                bx, by, bz = pts[j]
                cx_ab = ay * bz - az * by
                cy_ab = az * bx - ax * bz
                cz_ab = ax * by - ay * bx
                if cx_ab == 0 and cy_ab == 0 and cz_ab == 0:
                    continue
                ab_dot = ax * bx + ay * by + az * bz

                for k in range(j + 1, n):
                    cx, cy, cz = pts[k]
                    det = cx * cx_ab + cy * cy_ab + cz * cz_ab
                    if det != 0:
                        bc_dot = bx * cx + by * cy + bz * cz
                        ca_dot = cx * ax + cy * ay + cz * az
                        denom = r3 + r * (ab_dot + bc_dot + ca_dot)
                        if denom > 0:
                            area = 2.0 * r2 * math.atan(abs(det) / denom)
                            if area < min_area:
                                min_area = area

        total_area += min_area

    return f"{total_area:.6f}"


if __name__ == "__main__":
    print(solve())
