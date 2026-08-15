"""Project Euler 296: Angular Bisector and Tangent

Find how many integer-sided triangles ABC with perimeter <= 100 000 exist such that BE has integral length.
BC <= AC <= AB, k is angle bisector of angle ACB, m is tangent at C to circumcircle,
n is parallel to m through B, and E is the intersection of n and k.
"""

from __future__ import annotations

import math


def solve(limit_p: int = 100_000) -> str:
    """Calculates the number of triangles ABC with perimeter <= limit_p and integer BE.

    Geometric reduction:
      Let a = BC, b = AC, c = AB with a <= b <= c.
      By angle chasing with the Alternate Segment Theorem and angle bisector properties:
        BE = a * c / (a + b)
      For BE to be an integer:
        (a + b) must divide a * c.
      Let g = gcd(a, b), a = g * x, b = g * y with gcd(x, y) = 1, 1 <= x <= y.
      Then (x + y) must divide c, so c = k * (x + y) for an integer k.
      - Triangle inequalities and ordering:
        b <= c < a + b ==> ceil(g * y / (x + y)) <= k <= g - 1
      - Perimeter bound:
        (g + k) * (x + y) <= limit_p ==> k <= limit_p / (x + y) - g
    """
    total = 0
    max_s = limit_p // 3

    for s in range(2, max_s + 1):
        max_g = limit_p // s
        for x in range(1, s // 2 + 1):
            if math.gcd(x, s) != 1:
                continue
            y = s - x
            for g in range(2, max_g):
                k_min = (g * y + s - 1) // s
                k_max = min(g - 1, max_g - g)
                if k_min <= k_max:
                    total += k_max - k_min + 1

    return str(total)


if __name__ == "__main__":
    print(solve())
