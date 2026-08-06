## Function Contract

`solve(grid: list[list[int]]) -> int`

**Inputs**

- `grid`: an $m \times n$ binary matrix whose `1` cells are land and whose `0` cells are water.

**Return value**

Return the number of island shape classes under translation alone. Horizontal and vertical contact joins land; rotation and reflection do not make two shapes equivalent.
