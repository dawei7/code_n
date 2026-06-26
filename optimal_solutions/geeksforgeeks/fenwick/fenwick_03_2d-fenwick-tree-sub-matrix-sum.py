"""Optimal solution for fenwick_03: 2D Fenwick Tree (Sub-matrix Sum).

Build a 2D Binary Indexed Tree on an n x n matrix,
"""


def solve(matrix, n, updates, queries, q):
    """2D BIT with point updates and sub-matrix sum queries.

    1-based BIT indexing internally (so cell (r, c) maps to
    BIT[r+1][c+1]).
    """
    if n == 0:
        return [0] * q
    # Build BIT.
    bit = [[0] * (n + 1) for _ in range(n + 1)]
    work = [row[:] for row in matrix]

    def update(r, c, delta):
        r += 1
        c += 1
        i = r
        while i <= n:
            j = c
            while j <= n:
                bit[i][j] += delta
                j += j & -j
            i += i & -i

    def prefix(r, c):
        # Sum over (0,0) .. (r,c) inclusive. Caller must clamp
        # r, c to -1 (which yields 0).
        if r < 0 or c < 0:
            return 0
        r += 1
        c += 1
        s = 0
        i = r
        while i > 0:
            j = c
            while j > 0:
                s += bit[i][j]
                j -= j & -j
            i -= i & -i
        return s

    # Build the BIT by inserting each cell's initial value.
    for r in range(n):
        for c in range(n):
            if matrix[r][c] != 0:
                update(r, c, matrix[r][c])

    # Apply updates.
    for r, c, delta in updates:
        work[r][c] += delta
        update(r, c, delta)

    # Answer queries.
    out = []
    for r1, c1, r2, c2 in queries:
        s = (prefix(r2, c2)
             - prefix(r1 - 1, c2)
             - prefix(r2, c1 - 1)
             + prefix(r1 - 1, c1 - 1))
        out.append(s)
    return out
