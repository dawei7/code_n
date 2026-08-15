"""Project Euler Problem 582: Nearly Isosceles 120 Degree Triangles.

Find T(10^100), where T(n) is the count of integer triangles (a, b, c) with
one 120-degree angle, a <= b <= c, b - a <= 100, and c <= n.
"""

import math
from typing import List, Set, Tuple


def _is_square(n: int) -> int:
    if n < 0:
        return -1
    r = math.isqrt(n)
    return r if r * r == n else -1


def _seeds_for_k(k: int, y_max: int = 2000) -> List[Tuple[int, int]]:
    k2 = k * k
    sols: List[Tuple[int, int]] = []

    for y in range(0, y_max + 1):
        if (y - k) & 1:
            continue
        x = _is_square(3 * y * y + k2)
        if x == -1 or (x & 1):
            continue
        if x * x - 3 * y * y != k2:
            continue
        sols.append((x, y))

    if k % 2 == 0:
        def prev(x_val: int, y_val: int) -> Tuple[int, int]:
            return (2 * x_val - 3 * y_val, 2 * y_val - x_val)
    else:
        def prev(x_val: int, y_val: int) -> Tuple[int, int]:
            return (7 * x_val - 12 * y_val, 7 * y_val - 4 * x_val)

    seeds: Set[Tuple[int, int]] = set()
    for x, y in sols:
        xp, yp = prev(x, y)
        if (
            xp > 0
            and yp >= 0
            and ((yp - k) & 1) == 0
            and (xp & 1) == 0
            and xp * xp - 3 * yp * yp == k2
        ):
            continue
        seeds.add((x, y))

    return sorted(seeds)


def solve(n: int = 10**100) -> int:
    """Count nearly isosceles 120-degree triangles with c <= n using Pell recurrences."""
    total = 0
    limit_x = 2 * n

    for k in range(1, 101):
        seeds = _seeds_for_k(k)

        if k % 2 == 0:
            def step(x_val: int, y_val: int) -> Tuple[int, int]:
                return (2 * x_val + 3 * y_val, x_val + 2 * y_val)
        else:
            def step(x_val: int, y_val: int) -> Tuple[int, int]:
                return (7 * x_val + 12 * y_val, 4 * x_val + 7 * y_val)

        for x, y in seeds:
            while x <= limit_x:
                if y > k:
                    total += 1
                x, y = step(x, y)

    return total


if __name__ == "__main__":
    print(solve())
