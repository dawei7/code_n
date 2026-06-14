"""Optimal solution for bit_04: Power Set.

Return every subset of the input list as a list
"""


def solve(arr, n):
    """Return every subset of arr as a list of lists."""
    result = []
    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(arr[i])
        result.append(subset)
    return result
