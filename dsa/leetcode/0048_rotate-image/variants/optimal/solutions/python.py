def solve(matrix: list[list[int]]) -> list[list[int]]:
    size = len(matrix)
    for row in range(size):
        for column in range(row + 1, size):
            matrix[row][column], matrix[column][row] = (
                matrix[column][row],
                matrix[row][column],
            )
    for row in matrix:
        row.reverse()
    return matrix
