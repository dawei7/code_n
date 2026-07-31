def solve(n: int, m: int, k: int) -> int:
    span = 2 * k + 1
    row_bands = (n + span - 1) // span
    column_bands = (m + span - 1) // span
    return row_bands * column_bands
