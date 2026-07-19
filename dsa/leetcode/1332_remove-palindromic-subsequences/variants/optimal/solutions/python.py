"""Optimal app-local solution for LeetCode 1332."""


def solve(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return 2
        left += 1
        right -= 1

    return 1
