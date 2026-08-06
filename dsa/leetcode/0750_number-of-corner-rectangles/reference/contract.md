## Function Contract

`solve(grid: list[list[int]]) -> int`

Let $m$ be the number of rows and $n$ be the number of columns.

**Inputs**

- `grid`: a nonempty rectangular $m \times n$ matrix whose entries are binary integers.

**Return value**

Return the number of choices of row indices $r_1 < r_2$ and column indices $c_1 < c_2$ for which all four cells `grid[r1][c1]`, `grid[r1][c2]`, `grid[r2][c1]`, and `grid[r2][c2]` equal `1`.
