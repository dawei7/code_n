"""Optimal solution for LeetCode 1089: Duplicate Zeros."""


def solve(arr: list[int]) -> list[int]:
    n = len(arr)
    possible_dups = 0
    last = n - 1
    left = 0
    while left <= last - possible_dups:
        if arr[left] == 0:
            if left == last - possible_dups:
                arr[last] = 0
                last -= 1
                break
            possible_dups += 1
        left += 1

    for i in range(last - possible_dups, -1, -1):
        if arr[i] == 0:
            arr[i + possible_dups] = 0
            possible_dups -= 1
            arr[i + possible_dups] = 0
        else:
            arr[i + possible_dups] = arr[i]
    return arr
