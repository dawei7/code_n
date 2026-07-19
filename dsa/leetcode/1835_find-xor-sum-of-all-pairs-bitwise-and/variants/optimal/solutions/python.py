"""App-local reference solution for LeetCode 1835."""


def solve(arr1: list[int], arr2: list[int]) -> int:
    first_xor = 0
    for value in arr1:
        first_xor ^= value

    second_xor = 0
    for value in arr2:
        second_xor ^= value

    return first_xor & second_xor
