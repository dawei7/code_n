def solve(mat: list[list[int]]) -> int:
    row_ones = [sum(row) for row in mat]
    column_ones = [
        sum(mat[row][column] for row in range(len(mat)))
        for column in range(len(mat[0]))
    ]

    total = 0
    for row in range(len(mat)):
        for column in range(len(mat[0])):
            if mat[row][column] == 1 and row_ones[row] == 1 and column_ones[column] == 1:
                total += 1

    return total
