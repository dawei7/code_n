"""Optimal app-local solution for LeetCode 1299."""


def solve(arr):
    best = -1
    for index in range(len(arr) - 1, -1, -1):
        original = arr[index]
        arr[index] = best
        best = max(best, original)
    return arr
