"""Optimal solution for bit_04: Power Set.

Return every subset of the input list as a list of lists.
Iterate ``mask`` from 0 to 2^n-1; include arr[i] in the subset
iff bit i of mask is set.
"""


def solve(arr, n):
    result = []
    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(arr[i])
        result.append(subset)
    return result
