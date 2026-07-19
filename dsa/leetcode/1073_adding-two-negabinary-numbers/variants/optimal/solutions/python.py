"""Optimal solution for LeetCode 1073: Adding Two Negabinary Numbers."""


def solve(arr1: list[int], arr2: list[int]) -> list[int]:
    i = len(arr1) - 1
    j = len(arr2) - 1
    carry = 0
    result: list[int] = []
    while i >= 0 or j >= 0 or carry:
        carry += arr1[i] if i >= 0 else 0
        carry += arr2[j] if j >= 0 else 0
        result.append(carry & 1)
        carry = -(carry >> 1)
        i -= 1
        j -= 1
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result[::-1]
