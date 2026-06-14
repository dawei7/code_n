"""Optimal solution for bit_11: Bitwise AND of Range.

Given two non-negative integers left and right
"""


def solve(left, right):
    """Return AND of all integers in [left, right] (the common prefix)."""
    shift = 0
    # While left and right differ, shift them both right by 1
    # (and count the shifts) to find the common prefix.
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1
    return left << shift
