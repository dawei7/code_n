"""Optimal solution for sort_02: Selection Sort.

For each index i, find the minimum element in data[i..n-1] and
swap it into position i. O(n^2) time, O(1) extra space, at most n
swaps.
"""


def solve(data, n):
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        if min_idx != i:
            data[i], data[min_idx] = data[min_idx], data[i]
    return data
