def solve(mat, k):
    rows = len(mat)
    cols = len(mat[0]) if rows else 0
    prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
    for r in range(rows):
        for c in range(cols):
            prefix[r + 1][c + 1] = mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c]

    answer = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        r1 = max(0, r - k)
        r2 = min(rows, r + k + 1)
        for c in range(cols):
            c1 = max(0, c - k)
            c2 = min(cols, c + k + 1)
            answer[r][c] = prefix[r2][c2] - prefix[r1][c2] - prefix[r2][c1] + prefix[r1][c1]
    return answer
