"""Optimal solution for LeetCode 1385: Find the Distance Value Between Two Arrays."""

from bisect import bisect_left


def solve(arr1: list[int], arr2: list[int], d: int) -> int:
    arr2.sort()
    answer = 0
    for value in arr1:
        pos = bisect_left(arr2, value)
        close = False
        if pos < len(arr2) and abs(arr2[pos] - value) <= d:
            close = True
        if pos > 0 and abs(arr2[pos - 1] - value) <= d:
            close = True
        if not close:
            answer += 1
    return answer
