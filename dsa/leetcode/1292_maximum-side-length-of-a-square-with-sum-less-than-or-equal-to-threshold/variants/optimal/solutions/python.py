def solve(mat, threshold):
    rows = len(mat)
    columns = len(mat[0])
    prefix = [[0] * (columns + 1) for _ in range(rows + 1)]
    for row in range(rows):
        for column in range(columns):
            prefix[row + 1][column + 1] = (
                mat[row][column]
                + prefix[row][column + 1]
                + prefix[row + 1][column]
                - prefix[row][column]
            )

    def square_sum(row, column, side):
        return (
            prefix[row + side][column + side]
            - prefix[row][column + side]
            - prefix[row + side][column]
            + prefix[row][column]
        )

    best = 0
    for row in range(rows):
        for column in range(columns):
            while (
                row + best < rows
                and column + best < columns
                and square_sum(row, column, best + 1) <= threshold
            ):
                best += 1
    return best
