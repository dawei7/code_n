"""Project Euler Problem 894: Spiral of Circles.

Mathematical formulation:
A sequence of circles C_k has centers z_k = R * s^k * exp(i * k * theta) and radii r_k = s^k.
C_0 is externally tangent to C_1, C_7, and C_8, yielding the system of distance equations:
  R^2 = (1 + s)^2 / (1 - 2*s*cos(theta) + s^2)
      = (1 + s^7)^2 / (1 - 2*s^7*cos(7*theta) + s^14)
      = (1 + s^8)^2 / (1 - 2*s^8*cos(8*theta) + s^16).

Geometric Area Summation:
Solving for (s, theta) via 2D Newton-Raphson yields s approx 0.906331406148595, theta approx 0.826729539414059.
The green region is composed of two base circular triangles per scale step:
  T_1 = Triangle(C_0, C_1, C_8), T_2 = Triangle(C_0, C_7, C_8).
By self-similarity, the total area sums as an infinite geometric series:
  Total Area = (Area(T_1) + Area(T_2)) / (1 - s^2) = 0.7718678168.

Evaluated in under 0.001s in pure Python.
"""

from __future__ import annotations

import math


def circular_triangle_area(ra: float, rb: float, rc: float) -> float:
    """Compute the area of a curved circular triangle bounded by three mutually tangent circles."""
    # Center triangle area by Heron's formula
    area_tri = math.sqrt((ra + rb + rc) * ra * rb * rc)

    # Law of Cosines for interior angles
    a = rb + rc
    b = rc + ra
    c = ra + rb

    cos_a = (b * b + c * c - a * a) / (2.0 * b * c)
    cos_b = (a * a + c * c - b * b) / (2.0 * a * c)
    cos_c = (a * a + b * b - c * c) / (2.0 * a * b)

    ang_a = math.acos(max(-1.0, min(1.0, cos_a)))
    ang_b = math.acos(max(-1.0, min(1.0, cos_b)))
    ang_c = math.acos(max(-1.0, min(1.0, cos_c)))

    sector_sum = 0.5 * (ra * ra * ang_a + rb * rb * ang_b + rc * rc * ang_c)
    return area_tri - sector_sum


def solve() -> str:
    """Find the total area of all circular triangles rounded to 10 decimal places."""
    # 2D Newton-Raphson solver for (s, theta)
    s = 0.90
    th = 2.0 * math.pi / 7.5

    for _ in range(50):
        d1 = 1.0 - 2.0 * s * math.cos(th) + s * s
        r1 = (1.0 + s) ** 2 / d1

        s7 = s**7
        d7 = 1.0 - 2.0 * s7 * math.cos(7.0 * th) + s7 * s7
        r7 = (1.0 + s7) ** 2 / d7

        s8 = s**8
        d8 = 1.0 - 2.0 * s8 * math.cos(8.0 * th) + s8 * s8
        r8 = (1.0 + s8) ** 2 / d8

        f1 = r1 - r7
        f2 = r1 - r8

        if abs(f1) < 1e-15 and abs(f2) < 1e-15:
            break

        eps = 1e-8
        d1_s = 1.0 - 2.0 * (s + eps) * math.cos(th) + (s + eps) ** 2
        r1_s = (1.0 + (s + eps)) ** 2 / d1_s
        s7_s = (s + eps) ** 7
        d7_s = 1.0 - 2.0 * s7_s * math.cos(7.0 * th) + s7_s * s7_s
        r7_s = (1.0 + s7_s) ** 2 / d7_s
        s8_s = (s + eps) ** 8
        d8_s = 1.0 - 2.0 * s8_s * math.cos(8.0 * th) + s8_s * s8_s
        r8_s = (1.0 + s8_s) ** 2 / d8_s

        df1_ds = ((r1_s - r7_s) - f1) / eps
        df2_ds = ((r1_s - r8_s) - f2) / eps

        d1_th = 1.0 - 2.0 * s * math.cos(th + eps) + s * s
        r1_th = (1.0 + s) ** 2 / d1_th
        d7_th = 1.0 - 2.0 * s7 * math.cos(7.0 * (th + eps)) + s7 * s7
        r7_th = (1.0 + s7) ** 2 / d7_th
        d8_th = 1.0 - 2.0 * s8 * math.cos(8.0 * (th + eps)) + s8 * s8
        r8_th = (1.0 + s8) ** 2 / d8_th

        df1_dth = ((r1_th - r7_th) - f1) / eps
        df2_dth = ((r1_th - r8_th) - f2) / eps

        det = df1_ds * df2_dth - df1_dth * df2_ds
        ds = (f1 * df2_dth - f2 * df1_dth) / det
        dth = (df1_ds * f2 - df2_ds * f1) / det

        s -= ds
        th -= dth

    # Base curved circular triangles
    area1 = circular_triangle_area(1.0, s, s**8)
    area2 = circular_triangle_area(1.0, s**7, s**8)

    total_area = (area1 + area2) / (1.0 - s * s)
    return f"{total_area:.10f}"


if __name__ == "__main__":
    print(solve())
