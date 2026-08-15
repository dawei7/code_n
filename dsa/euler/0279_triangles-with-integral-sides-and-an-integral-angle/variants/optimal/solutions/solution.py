"""Project Euler 279: Triangles with integral sides and an integral angle

Find the number of integer sided triangles with at least one integral angle
and perimeter not exceeding 10^8.
"""

from __future__ import annotations

import math


def solve(limit: int = 10**8) -> str:
    """Calculates the total number of integer-sided triangles with perimeter <= limit

    having at least one integral degree angle (90, 60, or 120 degrees, or equilateral)
    using exact, non-overlapping Gaussian and Eisenstein triple parameterizations.
    """
    total_triangles = 0

    # 1. Equilateral triangles (all three angles 60 deg): a = b = c
    total_triangles += limit // 3

    # 2. Right-angled triangles (90 deg): Pythagorean triples
    # a = m^2 - n^2, b = 2mn, c = m^2 + n^2 => P = 2m(m + n)
    # with m > n >= 1, gcd(m, n) = 1, (m - n) % 2 == 1
    m_max_90 = int(math.isqrt(limit // 2)) + 1
    for m in range(2, m_max_90):
        for n in range(1 + (m % 2), m, 2):
            if math.gcd(m, n) == 1:
                p_90 = 2 * m * (m + n)
                if p_90 <= limit:
                    total_triangles += limit // p_90
                else:
                    break

    # 3. 120 deg and 60 deg triangles from Eisenstein integer triples
    # m > n >= 1, gcd(m, n) = 1, (m - n) % 3 != 0
    m_max_eisenstein = int(math.isqrt(limit)) + 1
    for m in range(2, m_max_eisenstein):
        for n in range(1, m):
            if (m - n) % 3 != 0 and math.gcd(m, n) == 1:
                # 120 deg: P = (2m + n)(m + n)
                p_120 = (2 * m + n) * (m + n)
                if p_120 <= limit:
                    total_triangles += limit // p_120

                # 60 deg branch 1: P = (2m + n)(m + 2n)
                p_60_1 = (2 * m + n) * (m + 2 * n)
                if p_60_1 <= limit:
                    total_triangles += limit // p_60_1

                # 60 deg branch 2: P = 3m(m + n)
                p_60_2 = 3 * m * (m + n)
                if p_60_2 <= limit:
                    total_triangles += limit // p_60_2

    return str(total_triangles)


if __name__ == "__main__":
    print(solve())
