"""Project Euler Problem 563: Robot Welders.

Find sum_{n=2..100} M(n), where M(n) is the minimal 23-smooth area that can be
manufactured in exactly n variants with long side <= 1.1 * short side.
"""

import bisect
import heapq
import math
from typing import List


def solve(max_combinations: int = 100) -> int:
    """Compute sum_{n=2..max_combinations} M(n) using 23-smooth priority queue and binary search."""
    solutions = [0] * (max_combinations + 1)
    num_solutions = 1
    result = 0

    areas: List[int] = []
    heapq.heappush(areas, 1)

    sides: List[int] = []
    ignore_above = 2_300_000_000_000_000

    while num_solutions < max_combinations:
        current = heapq.heappop(areas)

        if current * current <= ignore_above:
            sides.append(current)

        multiples = [23, 19, 17, 13, 11, 7, 5, 3, 2]
        for multiple in multiples:
            next_value = multiple * current
            if next_value <= ignore_above:
                heapq.heappush(areas, next_value)
            if current % multiple == 0:
                break

        if num_solutions >= 56:
            if current % 800 != 0:
                continue
        elif num_solutions >= 8:
            if current % 80 != 0:
                continue
        elif current % 40 != 0:
            continue

        idx = bisect.bisect_right(sides, int(math.isqrt(current))) - 1
        if idx <= 0:
            continue

        num_found = 0
        while idx > 0:
            short_side = sides[idx]
            idx -= 1
            long_side = current // short_side

            if long_side * 10 > short_side * 11:
                break

            if long_side * short_side == current:
                num_found += 1

        if num_found < 2 or num_found > max_combinations:
            continue

        if solutions[num_found] == 0:
            solutions[num_found] = current
            result += current
            num_solutions += 1

    return result


if __name__ == "__main__":
    print(solve())
