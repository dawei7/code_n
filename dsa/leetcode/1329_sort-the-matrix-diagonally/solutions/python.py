from collections import defaultdict


def solve(mat):
    diagonals = defaultdict(list)
    rows = len(mat)
    cols = len(mat[0]) if rows else 0
    for r in range(rows):
        for c in range(cols):
            diagonals[r - c].append(mat[r][c])
    for values in diagonals.values():
        values.sort(reverse=True)
    for r in range(rows):
        for c in range(cols):
            mat[r][c] = diagonals[r - c].pop()
    return mat
