"""Optimal app-local solution for LeetCode 1424."""


def solve(nums: list[list[int]]) -> list[int]:
    diagonals: list[list[int]] = []
    for row, values in enumerate(nums):
        for column, value in enumerate(values):
            diagonal = row + column
            while len(diagonals) <= diagonal:
                diagonals.append([])
            diagonals[diagonal].append(value)

    traversal: list[int] = []
    for diagonal in diagonals:
        traversal.extend(reversed(diagonal))
    return traversal
