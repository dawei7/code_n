### 1. Description

Given an `m x n` binary matrix `mat`, return *the distance of the nearest *`0`* for each cell*.

The distance between two cells sharing a common edge is `1`.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

![](images/01-1-grid.jpg)

- **Input:** $mat = [[0,0,0],[0,1,0],[0,0,0]]$
- **Output:** `[[0,0,0],[0,1,0],[0,0,0]]`
#### Example 2

![](images/01-2-grid.jpg)

- **Input:** $mat = [[0,0,0],[0,1,0],[1,1,1]]$
- **Output:** `[[0,0,0],[0,1,0],[1,2,1]]`

### 4. Constraints

- $m = \text{mat.length}$

- $n = \text{mat}[i].length$

- $1 \le m, n \le 10^{4}$

- $1 \le m * n \le 10^{4}$

- $\text{mat}[i][j]$ is either `0` or `1`.

- There is at least one `0` in `mat`.

### 5. Note

This question is the same as 1765: <a href="https://leetcode.com/problems/map-of-highest-peak/description/" target="_blank">https://leetcode.com/problems/map-of-highest-peak/</a>