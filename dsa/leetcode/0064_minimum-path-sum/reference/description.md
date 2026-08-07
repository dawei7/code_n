### 1. Description

Given a `m x n` `grid` filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

### 2. Function Contract

**Inputs**

- `grid`: A non-empty rectangular grid of non-negative integers.

**Return value**

Return the smallest sum attainable along an allowed top-left-to-bottom-right path, including both endpoints.

### 3. Note

You can only move either down or right at any point in time.

### 4. Examples

#### Example 1

![](images/minpath.jpg)

- **Input:** `grid = [[1,3,1],[1,5,1],[4,2,1]]`
- **Output:** `7`
- **Explanation:** Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
#### Example 2

- **Input:** `grid = [[1,2,3],[4,5,6]]`
- **Output:** `12`

### 5. Constraints

- $m = \text{grid.length}$

- $n = \text{grid}[i].length$

- $1 \le m, n \le 200$

- $0 \le \text{grid}[i][j] \le 200$