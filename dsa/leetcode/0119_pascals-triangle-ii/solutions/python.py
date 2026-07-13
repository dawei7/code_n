def solve(row_index: int) -> list[int]:
    row = [1]
    coefficient = 1
    for column in range(1, row_index + 1):
        coefficient = coefficient * (row_index - column + 1) // column
        row.append(coefficient)
    return row
