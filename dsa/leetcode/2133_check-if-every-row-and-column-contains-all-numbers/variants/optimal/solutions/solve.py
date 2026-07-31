def solve(matrix: list[list[int]]) -> bool:
    n = len(matrix)
    required = set(range(1, n + 1))
    for index in range(n):
        if set(matrix[index]) != required:
            return False
        if {matrix[row][index] for row in range(n)} != required:
            return False
    return True
