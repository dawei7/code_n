def solve(num_rows: int) -> list[list[int]]:
    triangle: list[list[int]] = []
    for row_index in range(num_rows):
        row = [1] * (row_index + 1)
        for column in range(1, row_index):
            row[column] = triangle[-1][column - 1] + triangle[-1][column]
        triangle.append(row)
    return triangle
