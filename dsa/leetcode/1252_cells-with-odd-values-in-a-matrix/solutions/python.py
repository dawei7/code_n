from typing import List


def solve(m: int, n: int, indices: List[List[int]]) -> int:
    rows = [0] * m
    cols = [0] * n
    for r, c in indices:
        rows[r] ^= 1
        cols[c] ^= 1
    odd_rows = sum(rows)
    odd_cols = sum(cols)
    return odd_rows * (n - odd_cols) + (m - odd_rows) * odd_cols
