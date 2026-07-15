"""Optimal app-local solution for LeetCode 944."""


def solve(strs):
    rows = len(strs)
    columns = len(strs[0])
    deleted = 0

    for column in range(columns):
        for row in range(rows - 1):
            if strs[row][column] > strs[row + 1][column]:
                deleted += 1
                break

    return deleted
