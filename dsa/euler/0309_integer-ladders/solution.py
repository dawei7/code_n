"""Project Euler 309: Integer Ladders

Find how many triplets (x, y, h) with 0 < x < y < 1000000 produce an integer solution for street width w
in the classic crossing ladders problem.
"""

from __future__ import annotations

import math


def solve(limit: int = 1_000_000) -> str:
    """Calculates the number of integer ladder triplets (x, y, h) with x < y < limit

    using Pythagorean triple parametrization grouped by common leg w.
    """
    # legs[w] stores all other leg lengths A such that A^2 + w^2 = c^2 with c < limit
    legs: list[list[int]] = [[] for _ in range(limit)]

    max_u = int(math.isqrt(limit))
    for u in range(2, max_u + 1):
        u2 = u * u
        for v in range(1 + (u % 2), u, 2):
            if math.gcd(u, v) == 1:
                c0 = u2 + v * v
                if c0 >= limit:
                    continue
                a0 = u2 - v * v
                b0 = 2 * u * v
                max_k = (limit - 1) // c0
                for k in range(1, max_k + 1):
                    a = k * a0
                    b = k * b0
                    legs[a].append(b)
                    legs[b].append(a)

    count = 0
    # For each width w, check pairs of vertical ladder heights A < B
    for w in range(1, limit):
        a_list = legs[w]
        n = len(a_list)
        if n >= 2:
            a_list.sort()
            for i in range(n):
                a_val = a_list[i]
                for j in range(i + 1, n):
                    b_val = a_list[j]
                    if (a_val * b_val) % (a_val + b_val) == 0:
                        count += 1

    return str(count)


if __name__ == "__main__":
    print(solve())
