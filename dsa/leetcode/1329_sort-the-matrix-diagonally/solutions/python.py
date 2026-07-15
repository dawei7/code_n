"""Optimal app-local solution for LeetCode 1329."""

from collections import defaultdict


def solve(mat):
    diagonals = defaultdict(list)
    for row in range(len(mat)):
        for column in range(len(mat[0])):
            diagonals[row - column].append(mat[row][column])

    for values in diagonals.values():
        values.sort(reverse=True)

    for row in range(len(mat)):
        for column in range(len(mat[0])):
            mat[row][column] = diagonals[row - column].pop()
    return mat
