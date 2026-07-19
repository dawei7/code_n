"""Optimal app-local solution for LeetCode 836."""


def solve(rec1, rec2):
    horizontal = max(rec1[0], rec2[0]) < min(rec1[2], rec2[2])
    vertical = max(rec1[1], rec2[1]) < min(rec1[3], rec2[3])
    return horizontal and vertical
