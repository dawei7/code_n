def solve(mat):
    if not mat:
        return 0
    rows = len(mat)
    cols = max((len(row) for row in mat), default=0)
    row_count = [0] * rows
    col_count = [0] * cols
    for r, row in enumerate(mat):
        for c, value in enumerate(row):
            if value == 1:
                row_count[r] += 1
                col_count[c] += 1
    total = 0
    for r, row in enumerate(mat):
        for c, value in enumerate(row):
            if value == 1 and row_count[r] == 1 and col_count[c] == 1:
                total += 1
    return total
