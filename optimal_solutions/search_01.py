"""Optimal solution for search_01: Linear Search.

Walk the array until the target is found or the end is reached.
O(n) time.
"""


def solve(data, target):
    for index in range(len(data)):
        if data[index] == target:
            return index
    return -1
