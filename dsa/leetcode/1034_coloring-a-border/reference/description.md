## Description

You are given an `m x n` integer matrix `grid`, and three integers `row`, `col`, and `color`. Each value in the grid represents the color of the grid square at that location.

Two squares are called **adjacent** if they are next to each other in any of the 4 directions.

Two squares belong to the same **connected component** if they have the same color and they are adjacent.

The **border of a connected component** is all the squares in the connected component that are either adjacent to (at least) a square not in the component, or on the boundary of the grid (the first or last row or column).

You should color the **border** of the **connected component** that contains the square $\text{grid}[row][col]$ with `color`.

Return *the final grid*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** `grid = [[1,1],[1,2]], row = 0, col = 0, color = 3`
- **Output:** `[[3,3],[3,2]]`
#### Example 2

- **Input:** `grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3`
- **Output:** `[[1,3,3],[2,3,3]]`
#### Example 3

- **Input:** `grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2`
- **Output:** `[[2,2,2],[2,1,2],[2,2,2]]`
### Constraints

- $m = \text{grid.length}$

- $n = \text{grid}[i].length$

- $1 \le m, n \le 50$

- $1 \le \text{grid}[i][j], color \le 1000$

- $0 \le row < m$

- $0 \le col < n$