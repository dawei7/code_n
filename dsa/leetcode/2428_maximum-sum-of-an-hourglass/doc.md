# Maximum Sum of an Hourglass

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2428 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Maximum Sum of an Hourglass](https://leetcode.com/problems/maximum-sum-of-an-hourglass/) |

## Problem Description

### Goal

You are given an $m \times n$ matrix `grid`. An hourglass occupies a fixed $3 \times 3$ area: all three cells in its top row, only the center cell in its middle row, and all three cells in its bottom row.

Consider every placement that lies entirely inside the matrix and return the largest sum of its seven selected cells. The hourglass orientation is fixed and cannot be rotated; the two outer cells of the middle row are not included.

### Function Contract

**Inputs**

- `grid`: A rectangular matrix of non-negative integers.

Let $m$ be the number of rows and $n$ the number of columns. The constraints are $3 \le m,n \le 150$ and $0 \le \texttt{grid[i][j]} \le 10^6$.

**Return value**

- The maximum seven-cell sum among all valid hourglass placements.

### Examples

#### Example 1

- **Input:** `grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]`
- **Output:** `30`

The top-left hourglass contributes `6 + 2 + 1 + 2 + 9 + 2 + 8`.

#### Example 2

- **Input:** `grid = [[1,2,3],[4,5,6],[7,8,9]]`
- **Output:** `35`

The matrix contains exactly one placement, whose selected cells sum to 35.

#### Example 3

- **Input:** `grid = [[1,1,1],[100,2,100],[1,1,1]]`
- **Output:** `8`

The two large outer cells in the middle row do not belong to the hourglass.
