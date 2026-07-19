"""Optimal app-local solution for LeetCode 960."""


def solve(strs):
    columns = len(strs[0])
    best = [1] * columns

    for right in range(columns):
        for left in range(right):
            if all(row[left] <= row[right] for row in strs):
                best[right] = max(best[right], best[left] + 1)

    return columns - max(best)
