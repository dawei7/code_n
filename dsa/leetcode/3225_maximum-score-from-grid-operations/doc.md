# Maximum Score From Grid Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3225 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-score-from-grid-operations/) |

## Problem Description

### Goal

You are given a non-negative $n\times n$ matrix `grid`. Initially every cell is white. An operation chooses a row `i` and column `j`, then colors black every cell in column `j` from the top row through row `i`. Repeating an operation on a column can only extend its black prefix.

After any number of operations, a white cell contributes its stored value exactly when at least one horizontally adjacent cell is black. Cells outside the grid do not count as neighbors, and black cells never contribute. Return the maximum possible sum of contributing white cells.

### Function Contract

**Inputs**

- `grid`: A square matrix with $1 \leq n \leq 100$ and $0 \leq \texttt{grid[i][j]} \leq 10^9$.

**Return value**

Return the maximum score obtainable by choosing the black-prefix height of every column.

### Examples

#### Example 1

- **Input:** `grid = [[0,0,0,0,0],[0,0,3,0,0],[0,1,0,0,0],[5,0,0,3,0],[0,0,0,0,2]]`
- **Output:** `11`
- **Explanation:** Appropriate black prefixes expose the white values `5`, `3`, and `3` beside black cells.

#### Example 2

- **Input:** `grid = [[10,9,0,0,15],[7,1,0,8,0],[5,20,0,11,0],[0,0,0,1,2],[8,12,1,10,3]]`
- **Output:** `94`

#### Example 3

- **Input:** `grid = [[7]]`
- **Output:** `0`
- **Explanation:** A one-column grid has no horizontal neighbors.
