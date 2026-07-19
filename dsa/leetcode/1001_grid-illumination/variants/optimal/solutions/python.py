"""Optimal app-local solution for LeetCode 1001."""

from collections import Counter


def solve(n, lamps, queries):
    active = set()
    rows = Counter()
    columns = Counter()
    diagonals = Counter()
    anti_diagonals = Counter()

    for row, column in lamps:
        if (row, column) in active:
            continue
        active.add((row, column))
        rows[row] += 1
        columns[column] += 1
        diagonals[row - column] += 1
        anti_diagonals[row + column] += 1

    answer = []
    for row, column in queries:
        answer.append(
            int(
                rows[row] > 0
                or columns[column] > 0
                or diagonals[row - column] > 0
                or anti_diagonals[row + column] > 0
            )
        )

        for row_step in (-1, 0, 1):
            for column_step in (-1, 0, 1):
                neighbor = (row + row_step, column + column_step)
                if neighbor not in active:
                    continue
                active.remove(neighbor)
                lamp_row, lamp_column = neighbor
                rows[lamp_row] -= 1
                columns[lamp_column] -= 1
                diagonals[lamp_row - lamp_column] -= 1
                anti_diagonals[lamp_row + lamp_column] -= 1

    return answer
