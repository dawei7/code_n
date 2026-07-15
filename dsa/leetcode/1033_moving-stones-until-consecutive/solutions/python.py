"""Optimal app-local solution for LeetCode 1033."""


def solve(a, b, c):
    x, y, z = sorted((a, b, c))
    left_gap = y - x
    right_gap = z - y

    if left_gap == 1 and right_gap == 1:
        minimum = 0
    elif left_gap <= 2 or right_gap <= 2:
        minimum = 1
    else:
        minimum = 2

    return [minimum, z - x - 2]

