### 1. Description

You are given a **0-indexed** `m x n` **binary** matrix `grid`. You can move from a cell `(row, col)` to any of the cells $(row + 1, col)$ or $(row, col + 1)$ that has the value `1`. The matrix is **disconnected** if there is no path from `(0, 0)` to $(m - 1, n - 1)$.

You can flip the value of **at most one** (possibly none) cell. You **cannot flip** the cells `(0, 0)` and $(m - 1, n - 1)$.

Return `true` *if it is possible to make the matrix disconnect or *`false`* otherwise*.

### 2. Function Contract

**Inputs**

- `grid`: Input parameter (`List[List[int]]`).

**Return value**

- Returns `bool`.

### 3. Note

that flipping a cell changes its value from `0` to `1` or from `1` to `0`.

### 4. Examples

#### Example 1

![](images/yetgrid2drawio.png)

- **Input:** `grid = [[1,1,1],[1,0,0],[1,1,1]]`
- **Output:** `true`
- **Explanation:** We can change the cell shown in the diagram above. There is no path from (0, 0) to (2, 2) in the resulting grid.

#### Example 2

![](images/yetgrid3drawio.png)

- **Input:** `grid = [[1,1,1],[1,0,1],[1,1,1]]`
- **Output:** `false`
- **Explanation:** It is not possible to change at most one cell such that there is not path from (0, 0) to (2, 2).

### 5. Constraints

- $m = \text{grid.length}$

- $n = \text{grid}[i].length$

- $1 \le m, n \le 1000$

- $1 \le m * n \le 10^{5}$

- $\text{grid}[i][j]$ is either `0` or `1`.

- $\text{grid}[0][0] = grid[m - 1][n - 1] = 1$
