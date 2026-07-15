"""Optimal app-local solution for LeetCode 1030."""


def solve(rows, cols, r_center, c_center):
    buckets = [[] for _ in range(rows + cols - 1)]
    for row in range(rows):
        for col in range(cols):
            distance = abs(row - r_center) + abs(col - c_center)
            buckets[distance].append([row, col])

    return [cell for bucket in buckets for cell in bucket]
