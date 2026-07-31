"""Optimal app-local solution for LeetCode 1131."""


def solve(arr1: list[int], arr2: list[int]) -> int:
    best = 0
    for sign1, sign2 in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
        low = float("inf")
        high = float("-inf")
        for index, (value1, value2) in enumerate(zip(arr1, arr2)):
            transformed = sign1 * value1 + sign2 * value2 + index
            low = min(low, transformed)
            high = max(high, transformed)
        best = max(best, high - low)
    return best
