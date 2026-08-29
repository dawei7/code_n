"""Project Euler Problem 504: Square on the Inside.

Find the number of quadrilaterals ABCD with vertices (a, 0), (0, b), (-c, 0), (0, -d)
for 1 <= a, b, c, d <= 100 that strictly contain a square number of lattice points.
"""

from math import gcd, isqrt
from typing import List


def solve(m: int = 100) -> int:
    """Compute number of quadrilaterals with square interior lattice points using Pick's Theorem and symmetry."""
    gcd_tab = [[gcd(i, j) for j in range(m + 1)] for i in range(m + 1)]

    max_i = (2 * m * 2 * m) // 2 + 1
    is_sq = [False] * (max_i + 1)
    for i in range(1, isqrt(max_i) + 1):
        is_sq[i * i] = True

    count = 0
    for a in range(1, m + 1):
        for c in range(a, m + 1):
            mult_ac = 1 if a == c else 2
            sum_ac = a + c

            g_b = [gcd_tab[a][b] + gcd_tab[b][c] for b in range(m + 1)]

            for b in range(1, m + 1):
                gb = g_b[b]
                for d in range(b, m + 1):
                    mult_bd = 1 if b == d else 2
                    gcd_sum = gb + g_b[d]
                    interior_pts = (sum_ac * (b + d) - gcd_sum) // 2 + 1
                    if is_sq[interior_pts]:
                        count += mult_ac * mult_bd

    return count


if __name__ == "__main__":
    print(solve())
