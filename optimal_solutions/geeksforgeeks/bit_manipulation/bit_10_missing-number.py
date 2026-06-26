"""Optimal solution for bit_10: Missing Number.

Given an array arr of n distinct integers in
"""


def solve(arr, n):
    """Find the missing integer in arr (length n, values in [0, n])."""
    # XOR all values and all indices 0..n; the missing value
    # is the survivor.
    result = n  # include the index n in the XOR
    for i, v in enumerate(arr):
        result ^= i ^ v
    return result
