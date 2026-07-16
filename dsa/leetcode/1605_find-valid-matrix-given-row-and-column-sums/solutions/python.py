def solve(rowSum: list[int], colSum: list[int]) -> list[list[int]]:
    remaining_rows = rowSum.copy()
    remaining_columns = colSum.copy()
    matrix = [[0] * len(colSum) for _ in rowSum]
    row = column = 0

    while row < len(rowSum) and column < len(colSum):
        value = min(remaining_rows[row], remaining_columns[column])
        matrix[row][column] = value
        remaining_rows[row] -= value
        remaining_columns[column] -= value
        if remaining_rows[row] == 0:
            row += 1
        if remaining_columns[column] == 0:
            column += 1

    return matrix
