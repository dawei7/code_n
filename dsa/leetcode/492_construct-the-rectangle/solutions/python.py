"""Closest factor-pair search for LeetCode 492."""

from math import isqrt


def solve(area: int) -> list[int]:
    width = isqrt(area)
    while area % width != 0:
        width -= 1
    return [area // width, width]
