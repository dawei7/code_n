"""Optimal solution for fenwick_06: Count Inversions (BIT).

Count the number of inversions in an array: pairs
"""


def solve(arr, n):
    """Inversion count via BIT, with value compression."""
    if n <= 1:
        return 0
    # Compress arr to 1..n by rank order.
    sorted_unique = sorted(set(arr))
    rank = {v: i + 1 for i, v in enumerate(sorted_unique)}
    compressed = [rank[v] for v in arr]
    # BIT of size n (max compressed value is n).
    bit = [0] * (n + 2)
    inv = 0
    for i in range(n - 1, -1, -1):
        v = compressed[i]
        # prefix sum of bit up to v-1.
        j = v - 1
        s = 0
        while j > 0:
            s += bit[j]
            j -= j & -j
        inv += s
        # Add 1 at index v.
        j = v
        while j <= n:
            bit[j] += 1
            j += j & -j
    return inv
