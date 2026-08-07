### 1. Description

Given an `m x n` integer matrix `grid`, return *the maximum **score** of a path starting at *`(0, 0)`* and ending at *$(m - 1, n - 1)$ moving in the 4 cardinal directions.

The **score** of a path is the minimum value in that path.

- For example, the score of the path `8 → 4 → 5 → 9` is `4`.

### 2. Function Contract

**Input**

- `grid`: a nonempty rectangular integer matrix with $m$ rows and $n$ columns.

A valid path starts at `(0, 0)`, ends at $(m - 1, n - 1)$, and moves only between horizontally or vertically adjacent cells. Its score includes both endpoint values and every intermediate cell value.

Let $V = mn$ be the number of cells.

**Return value**

Return the largest possible minimum cell value over every valid corner-to-corner path.

### 3. Examples

#### Example 1

![](images/maxgrid1.jpg)

- **Input:** `grid = [[5,4,5],[1,2,6],[7,4,6]]`
- **Output:** `4`
- **Explanation:** The path with the maximum score is highlighted in yellow.
#### Example 2

![](images/maxgrid2.jpg)

- **Input:** `grid = [[2,2,1,2,2,2],[1,2,2,2,1,2]]`
- **Output:** `2`
#### Example 3

![](images/maxgrid3.jpg)

- **Input:** `grid = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]`
- **Output:** `3`

### 4. Constraints

- $m = \text{grid.length}$

- $n = \text{grid}[i].length$

- $1 \le m, n \le 100$

- $0 \le \text{grid}[i][j] \le 10^{9}$