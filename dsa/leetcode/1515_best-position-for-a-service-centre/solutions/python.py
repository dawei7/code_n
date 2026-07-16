"""Optimal app-local solution for LeetCode 1515."""

import math


def solve(positions):
    """Return the geometric median's minimum total distance."""
    min_x = min(point[0] for point in positions)
    max_x = max(point[0] for point in positions)
    min_y = min(point[1] for point in positions)
    max_y = max(point[1] for point in positions)

    def total(x, y):
        return sum(math.hypot(px - x, py - y) for px, py in positions)

    def best_at_x(x):
        low, high = min_y, max_y
        for _ in range(45):
            first = (2 * low + high) / 3
            second = (low + 2 * high) / 3
            if total(x, first) <= total(x, second):
                high = second
            else:
                low = first
        return total(x, (low + high) / 2)

    low, high = min_x, max_x
    for _ in range(45):
        first = (2 * low + high) / 3
        second = (low + 2 * high) / 3
        if best_at_x(first) <= best_at_x(second):
            high = second
        else:
            low = first
    return best_at_x((low + high) / 2)
