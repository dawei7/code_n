"""Optimal app-local solution for LeetCode 902."""

from bisect import bisect_left


def solve(digits, n):
    boundary = str(n)
    choices = len(digits)
    length = len(boundary)
    total = sum(choices**size for size in range(1, length))

    for index, target in enumerate(boundary):
        smaller = bisect_left(digits, target)
        remaining = length - index - 1
        total += smaller * choices**remaining
        if smaller == choices or digits[smaller] != target:
            return total

    return total + 1
