### 1. Description

Given a `m x n` matrix `grid` which is sorted in non-increasing order both row-wise and column-wise, return *the number of **negative** numbers in* `grid`.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]`
- **Output:** `8`
- **Explanation:** There are 8 negatives number in the matrix.
#### Example 2

- **Input:** `grid = [[3,2],[1,0]]`
- **Output:** `0`

### 4. Constraints

- $m = \text{grid.length}$

- $n = \text{grid}[i].length$

- $1 \le m, n \le 100$

- $-100 \le \text{grid}[i][j] \le 100$

**Follow up:** Could you find an $O(n + m)$ solution?