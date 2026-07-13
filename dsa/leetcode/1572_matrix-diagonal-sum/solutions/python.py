def solve(mat):
    n = min(len(mat), len(mat[0]) if mat else 0)
    total = 0
    for i in range(n):
        total += mat[i][i]
        j = n - 1 - i
        if j != i:
            total += mat[i][j]
    return total
