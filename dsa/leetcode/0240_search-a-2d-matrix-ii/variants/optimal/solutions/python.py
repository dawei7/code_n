def solve(matrix: list[list[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
    row = 0
    column = len(matrix[0]) - 1
    while row < len(matrix) and column >= 0:
        value = matrix[row][column]
        if value == target:
            return True
        if value > target:
            column -= 1
        else:
            row += 1
    return False
