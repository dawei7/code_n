"""Optimal solution for LeetCode 1064: Fixed Point."""


def solve(arr: list[int]) -> int:
    left = 0
    right = len(arr)

    while left < right:
        middle = (left + right) // 2
        if arr[middle] < middle:
            left = middle + 1
        else:
            right = middle

    if left < len(arr) and arr[left] == left:
        return left
    return -1
