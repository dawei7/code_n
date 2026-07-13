"""Nearest-heater binary search for LeetCode 475."""

from bisect import bisect_left


def solve(houses: list[int], heaters: list[int]) -> int:
    ordered = sorted(heaters)
    radius = 0
    for house in houses:
        insertion = bisect_left(ordered, house)
        right = ordered[insertion] - house if insertion < len(ordered) else float("inf")
        left = house - ordered[insertion - 1] if insertion > 0 else float("inf")
        radius = max(radius, min(left, right))
    return int(radius)
