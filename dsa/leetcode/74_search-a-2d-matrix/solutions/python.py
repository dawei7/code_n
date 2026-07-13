def solve(matrix: list[list[int]], target: int) -> bool:
    rows, columns = len(matrix), len(matrix[0])
    left, right = 0, rows * columns - 1
    while left <= right:
        middle = (left + right) // 2
        value = matrix[middle // columns][middle % columns]
        if value == target:
            return True
        if value < target:
            left = middle + 1
        else:
            right = middle - 1
    return False
