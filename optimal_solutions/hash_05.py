"""Optimal solution for hash_05: Count Distinct Elements in Window.

For each window of size k, return the number of distinct
elements. Sliding window + count map: O(n) total.
"""


def solve(arr, k, n):
    if k <= 0 or k > n:
        return []
    counts = {}
    out = []
    for i in range(k):
        counts[arr[i]] = counts.get(arr[i], 0) + 1
    out.append(len(counts))
    for i in range(k, n):
        counts[arr[i]] = counts.get(arr[i], 0) + 1
        old = arr[i - k]
        counts[old] -= 1
        if counts[old] == 0:
            del counts[old]
        out.append(len(counts))
    return out
