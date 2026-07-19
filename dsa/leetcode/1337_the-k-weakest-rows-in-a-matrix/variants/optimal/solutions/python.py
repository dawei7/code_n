"""Optimal app-local solution for LeetCode 1337."""


def solve(mat, k):
    strengths = []

    for row_index, row in enumerate(mat):
        left = 0
        right = len(row)
        while left < right:
            middle = (left + right) // 2
            if row[middle] == 1:
                left = middle + 1
            else:
                right = middle
        strengths.append((left, row_index))

    strengths.sort()
    return [row_index for _, row_index in strengths[:k]]
