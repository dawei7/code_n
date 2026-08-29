"""Project Euler 257: Angular Bisectors

Find the number of integer-sided triangles ABC with a <= b <= c and perimeter <= 100,000,000
such that the ratio area(ABC) / area(AEG) is integral.
"""

from __future__ import annotations

import math


def solve(max_p: int = 100_000_000) -> str:
    """Counts triangles ABC with perimeter <= max_p having integral area(ABC)/area(AEG)

    using algebraic parameterization of the three possible integer ratios k in {2, 3, 4}.
    """
    total_triangles = 0

    # Ratio k = 4: Equilateral triangles (a = b = c)
    total_triangles += max_p // 3

    # Ratio k = 2: (b - a)(c - a) = 2a^2
    # Parameterized by coprime pairs (x, y) with x < y <= sqrt(2)*x
    max_x1 = int(max_p**0.5) + 1
    for x in range(1, max_x1):
        y_min = x + 1
        y_max = int(math.isqrt(2 * x * x))
        for y in range(y_min, y_max + 1):
            if math.gcd(x, y) == 1:
                d0 = y if y % 2 == 1 else y // 2
                a0 = x * d0
                u0 = y * d0
                v0 = 2 * x * x * d0 // y
                p0 = 3 * a0 + u0 + v0
                if p0 <= max_p:
                    total_triangles += max_p // p0

    # Ratio k = 3: (2b - a)(2c - a) = 3a^2
    # Parameterized by coprime pairs (x, y) with x < y <= sqrt(3)*x and matching parity
    max_x2 = int((2 * max_p) ** 0.5) + 1
    for x in range(1, max_x2):
        y_min = x + 1
        y_max = int(math.isqrt(3 * x * x))
        for y in range(y_min, y_max + 1):
            if math.gcd(x, y) == 1:
                g_base = y // math.gcd(y, 3)
                a_b = x * g_base
                u_b = y * g_base
                v_b = (3 // math.gcd(y, 3)) * x * x

                if a_b % 2 == u_b % 2 == v_b % 2:
                    p_base = a_b + (a_b + u_b) // 2 + (a_b + v_b) // 2
                else:
                    a_b2 = a_b * 2
                    u_b2 = u_b * 2
                    v_b2 = v_b * 2
                    p_base = a_b2 + (a_b2 + u_b2) // 2 + (a_b2 + v_b2) // 2

                if p_base <= max_p:
                    total_triangles += max_p // p_base

    return str(total_triangles)


if __name__ == "__main__":
    print(solve())
