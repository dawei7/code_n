"""Optimal solution for bit_03: Single Number (XOR).

XOR all elements — duplicates cancel, the unique element remains.
"""


def solve(arr):
    result = 0
    for v in arr:
        result ^= v
    return result
