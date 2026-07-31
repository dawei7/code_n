def solve(matrix: list[list[int]]) -> bool:
    for row in range(1, len(matrix)):
        for column in range(1, len(matrix[0])):
            if matrix[row][column] != matrix[row - 1][column - 1]:
                return False
    return True
