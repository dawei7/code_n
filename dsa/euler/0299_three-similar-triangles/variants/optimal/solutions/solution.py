"""Project Euler 299: Three Similar Triangles

Find how many distinct triplets (a, b, d) with b + d < 100 000 000 exist such that
a point P on line segment AC with integer coordinates makes triangles ABP, CDP, BDP all similar.
"""

from __future__ import annotations

import math


def solve(limit: int = 100_000_000) -> str:
    """Calculates the number of triplets (a, b, d) with b + d < limit.

    All valid triplets partition into two disjoint geometric families:

    1. Family 1 (x = y, so a = 2x, b != d):
       (b - a)(d - a) = 2x^2
       Primitive generators: gcd(m, 2n) = 1.
       base_sum = m^2 + 4mn + 2n^2
       Each generates 2 distinct triplets (b, d) and (d, b).

    2. Family 2 (b = d):
       (b - a)^2 = 2x(a - x)
       Primitive generators: m odd, gcd(m, n) = 1.
       base_sum = 2(m^2 + 2mn + 2n^2)
       Each generates 1 triplet where b = d.
    """
    count1 = 0
    max_m1 = int(math.isqrt(limit)) + 1
    for m in range(1, max_m1):
        for n in range(1, max_m1):
            if math.gcd(m, 2 * n) == 1:
                base_sum = m * m + 4 * m * n + 2 * n * n
                if base_sum < limit:
                    count1 += 2 * ((limit - 1) // base_sum)

    count2 = 0
    max_m2 = int(math.isqrt(limit)) + 1
    for m in range(1, max_m2, 2):  # m is odd
        for n in range(1, max_m2):
            if math.gcd(m, n) == 1:
                base_sum = 2 * (m * m + 2 * m * n + 2 * n * n)
                if base_sum < limit:
                    count2 += (limit - 1) // base_sum

    total = count1 + count2
    return str(total)


if __name__ == "__main__":
    print(solve())
