"""Project Euler 310: Nim Square

Find the number of losing positions for the next player in 3-heap Nim Square
with 0 <= a <= b <= c <= 100000.
"""

from __future__ import annotations

import math


def solve(limit: int = 100_000) -> str:
    """Calculates the number of losing positions (a <= b <= c <= limit with G(a) ^ G(b) ^ G(c) == 0)

    using bitmask Sprague-Grundy mex computation and combinatorial triple grouping.
    """
    # 1. Compute Grundy values G(n) = mex({G(n - k^2)}) using bitmask representation
    g: list[int] = [0] * (limit + 1)
    squares = [k * k for k in range(1, int(math.isqrt(limit)) + 1)]

    for n in range(1, limit + 1):
        seen = 0
        for sq in squares:
            if sq > n:
                break
            seen |= 1 << g[n - sq]

        # Bitwise mex: find first unset bit
        mex = 0
        while (seen >> mex) & 1:
            mex += 1
        g[n] = mex

    # 2. Count frequencies of each Grundy value
    max_g = max(g)
    c: list[int] = [0] * (max_g + 1)
    for val in g:
        c[val] += 1

    # 3. Combinatorial grouping of ordered triples (a <= b <= c)
    # Case 1: a = b = c (requires G(a) = 0)
    total_losing = c[0]

    # Case 2: exactly two equal (a = b < c or a < b = c, requiring the distinct element to have G = 0)
    total_losing += limit * c[0]

    # Case 3: all three distinct (a < b < c)
    # 3a: all three have G = 0
    total_losing += c[0] * (c[0] - 1) * (c[0] - 2) // 6

    # 3b: two equal non-zero G values, one zero G value (g ^ g ^ 0 = 0)
    for val in range(1, max_g + 1):
        total_losing += (c[val] * (c[val] - 1) // 2) * c[0]

    # 3c: three distinct non-zero G values with g1 ^ g2 ^ g3 == 0
    for g1 in range(1, max_g + 1):
        for g2 in range(g1 + 1, max_g + 1):
            g3 = g1 ^ g2
            if g3 > g2 and g3 <= max_g:
                total_losing += c[g1] * c[g2] * c[g3]

    return str(total_losing)


if __name__ == "__main__":
    print(solve())
