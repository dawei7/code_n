"""Optimal app-local solution for LeetCode 852."""


def solve(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        middle = (left + right) // 2
        if arr[middle] < arr[middle + 1]:
            left = middle + 1
        else:
            right = middle

    return left
