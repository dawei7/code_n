def solve(rowIndex: int) -> list[int]:
    row = [1]
    coefficient = 1
    for column in range(1, rowIndex + 1):
        coefficient = coefficient * (rowIndex - column + 1) // column
        row.append(coefficient)
    return row
