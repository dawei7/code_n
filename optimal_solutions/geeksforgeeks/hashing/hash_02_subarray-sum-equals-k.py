"""Optimal solution for hash_02: Subarray Sum Equals K.

The number of subarrays with sum k equals the number of prefix
sums p_j such that p_j == p_i - k for some earlier prefix p_i.
Track running prefix sums and the count of each. O(n).
"""


def solve(arr, k, n):
    count = 0
    prefix = 0
    freq = {0: 1}
    for i in range(n):
        prefix += arr[i]
        count += freq.get(prefix - k, 0)
        freq[prefix] = freq.get(prefix, 0) + 1
    return count
