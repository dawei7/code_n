## Function Contract

`solve(grid: list[list[int]]) -> int`

Let $m$ be the number of rows and $n$ the number of columns.

**Inputs**

- `grid`: an $m \times n$ rectangular binary matrix in which `1` is land and `0` is water.

**Return value**

Return the number of island equivalence classes when absolute position, the permitted quarter-turn rotations, and horizontal or vertical reflection do not distinguish shapes. Only horizontal and vertical adjacency connects land cells.
