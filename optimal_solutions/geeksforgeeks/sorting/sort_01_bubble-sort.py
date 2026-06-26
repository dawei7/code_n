"""Optimal solution for sort_01: Bubble Sort.

Sort the list in place by repeatedly swapping adjacent pairs.
O(n^2) time, O(1) extra space.
"""


def solve(data, n):
    for end in range(n - 1, 0, -1):
        for i in range(end):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
    return data
