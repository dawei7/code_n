def solve(mat, threshold):
    rows = len(mat)
    cols = len(mat[0]) if rows else 0
    prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
    for r in range(rows):
        for c in range(cols):
            prefix[r + 1][c + 1] = mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c]

    def square_sum(r, c, side):
        return prefix[r + side][c + side] - prefix[r][c + side] - prefix[r + side][c] + prefix[r][c]

    best = 0
    for r in range(rows):
        for c in range(cols):
            while r + best < rows and c + best < cols and square_sum(r, c, best + 1) <= threshold:
                best += 1
    return best
