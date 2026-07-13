def solve(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows else 0
    total = 0
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] and r and c:
                matrix[r][c] = 1 + min(matrix[r - 1][c], matrix[r][c - 1], matrix[r - 1][c - 1])
            total += matrix[r][c]
    return total
