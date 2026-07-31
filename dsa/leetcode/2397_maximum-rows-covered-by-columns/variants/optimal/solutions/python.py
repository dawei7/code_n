from itertools import combinations


def solve(matrix: list[list[int]], numSelect: int) -> int:
    column_count = len(matrix[0])
    row_masks: list[int] = []

    for row in matrix:
        row_mask = 0
        for column, value in enumerate(row):
            if value:
                row_mask |= 1 << column
        row_masks.append(row_mask)

    maximum = 0
    for selected_columns in combinations(range(column_count), numSelect):
        selected_mask = 0
        for column in selected_columns:
            selected_mask |= 1 << column

        covered = sum(
            row_mask & selected_mask == row_mask
            for row_mask in row_masks
        )
        maximum = max(maximum, covered)

    return maximum
