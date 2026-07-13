def solve(m: int, n: int, ops: list[list[int]]) -> int:
    """Return the area common to every increment rectangle."""
    common_rows = m
    common_columns = n

    for rows, columns in ops:
        common_rows = min(common_rows, rows)
        common_columns = min(common_columns, columns)

    return common_rows * common_columns

