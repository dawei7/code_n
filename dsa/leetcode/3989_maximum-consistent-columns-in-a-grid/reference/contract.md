## Function Contract

`solve(grid, limit) -> int`

Let $m=\lvert\texttt{grid}\rvert$ and $n=\lvert\texttt{grid[0]}\rvert$.

**Inputs**

- `grid`: A nonempty rectangular matrix of integers with `m` rows and `n` columns.
- `limit`: The inclusive maximum absolute difference allowed between adjacent retained columns in each row.

Column removal preserves relative order, and at least one column must remain. A pair of retained columns is compatible only when its absolute difference is at most `limit` in all `m` rows.

**Output**

Return the largest number of columns that can be retained while every adjacent retained pair is compatible.
