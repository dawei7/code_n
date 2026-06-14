"""Optimal solution for bit_03: Single Number (XOR).

Every element in the input array appears exactly
"""


def solve(arr):
    """Return the element that appears exactly once (others appear twice)."""
    result = 0
    for v in arr:
        result ^= v
    return result
