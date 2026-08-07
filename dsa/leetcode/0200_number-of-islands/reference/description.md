## Description

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return *the number of islands*.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
### Function Contract

**Inputs**

- `grid`: A rectangular matrix whose entries are the strings `"0"` and `"1"`.

**Return value**

Return the number of horizontally or vertically connected land components.

### Examples
#### Example 1

- **Input:** $grid = [$
["1","1","1","1","0"],
["1","1","0","1","0"],
["1","1","0","0","0"],
["0","0","0","0","0"]
]
- **Output:** `1`
#### Example 2

- **Input:** $grid = [$
["1","1","0","0","0"],
["1","1","0","0","0"],
["0","0","1","0","0"],
["0","0","0","1","1"]
]
- **Output:** `3`
### Constraints

- $m = \text{grid.length}$

- $n = \text{grid}[i].length$

- $1 \le m, n \le 300$

- $\text{grid}[i][j]$ is `'0'` or `'1'`.