"""Optimal solution for LeetCode 1053: Previous Permutation With One Swap."""


def solve(arr: list[int]) -> list[int]:
    i = len(arr) - 2
    while i >= 0 and arr[i] <= arr[i + 1]:
        i -= 1
    if i < 0:
        return arr

    j = len(arr) - 1
    while arr[j] >= arr[i]:
        j -= 1
    while j > i and arr[j] == arr[j - 1]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    return arr
