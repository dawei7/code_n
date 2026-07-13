"""Optimal solution for LeetCode 1380: Lucky Numbers in a Matrix."""


def solve(matrix: list[list[int]]) -> list[int]:
    row_mins = {min(row) for row in matrix}
    col_maxes = {max(matrix[r][c] for r in range(len(matrix))) for c in range(len(matrix[0]))}
    return list(row_mins & col_maxes)
