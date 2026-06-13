"""Optimal solution for fenwick_01: Build Fenwick Tree.

bit[i] = sum of arr[i - 2^k + 1 .. i] where k is the
number of trailing zeros in i.
"""


def solve(arr, n):
    if n == 0:
        return []
    bit = [0] * (n + 1)
    for i in range(1, n + 1):
        bit[i] = arr[i - 1]
    for i in range(1, n + 1):
        j = i + (i & -i)
        if j <= n:
            bit[j] += bit[i]
    return bit
