## Function Contract

`solve(m, n, k) -> list[str]`

**Inputs**

- `m`: The positive number of grid rows.
- `n`: The positive number of grid columns.
- `k`: The required positive number of valid paths.

Rows and columns use zero-based indices. A valid path begins at `(0, 0)`, ends at `(m - 1, n - 1)`, stays on `.` cells, and moves only right or down.

**Output**

Return a list of exactly `m` strings of length `n`, using only `.` for free cells and `#` for obstacles, such that the grid contains exactly `k` valid paths. More than one construction may be correct. Return `[]` precisely when no valid construction exists.
