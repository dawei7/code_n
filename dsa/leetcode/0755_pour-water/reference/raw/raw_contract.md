## Function Contract

`solve(heights: list[int], volume: int, k: int) -> list[int]`

Let $n$ be the number of terrain columns.

**Inputs**

- `heights`: the nonnegative initial terrain height of each unit-width column.
- `volume`: the number of one-unit water droplets to pour.
- `k`: the index where every droplet begins.

**Return value**

Return the $n$ final column levels after all `volume` droplets have settled sequentially according to the left-before-right eventual-fall rule. Each result entry equals the original terrain height plus the water accumulated in that column.
