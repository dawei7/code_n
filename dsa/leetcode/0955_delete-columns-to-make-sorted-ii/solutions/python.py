"""Optimal app-local solution for LeetCode 955."""


def solve(strs):
    resolved = [False] * (len(strs) - 1)
    deletions = 0

    for column in range(len(strs[0])):
        if any(
            not resolved[row] and strs[row][column] > strs[row + 1][column]
            for row in range(len(strs) - 1)
        ):
            deletions += 1
            continue
        for row in range(len(strs) - 1):
            if strs[row][column] < strs[row + 1][column]:
                resolved[row] = True
    return deletions
