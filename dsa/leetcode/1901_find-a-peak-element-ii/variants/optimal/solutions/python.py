def solve(mat: list[list[int]]) -> list[int]:
    row_count = len(mat)
    column_count = len(mat[0])
    low = 0
    high = column_count - 1

    while low <= high:
        column = (low + high) // 2
        row = max(range(row_count), key=lambda index: mat[index][column])
        value = mat[row][column]
        left = mat[row][column - 1] if column > 0 else -1
        right = mat[row][column + 1] if column + 1 < column_count else -1
        if value > left and value > right:
            return [row, column]
        if right > value:
            low = column + 1
        else:
            high = column - 1

    raise RuntimeError("the matrix contract guarantees a peak")
