"""Optimal solution for LeetCode 1053: Previous Permutation With One Swap."""


def solve(arr: list[int]) -> list[int]:
    pivot = len(arr) - 2
    while pivot >= 0 and arr[pivot] <= arr[pivot + 1]:
        pivot -= 1

    if pivot < 0:
        return arr

    target = len(arr) - 1
    while arr[target] >= arr[pivot]:
        target -= 1
    while target > pivot + 1 and arr[target] == arr[target - 1]:
        target -= 1

    arr[pivot], arr[target] = arr[target], arr[pivot]
    return arr
