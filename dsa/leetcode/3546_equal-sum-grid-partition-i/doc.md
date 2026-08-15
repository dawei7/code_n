# Equal Sum Grid Partition I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3546 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Enumeration, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/equal-sum-grid-partition-i/) |

## Problem Description

### Goal

You are given an $m \times n$ matrix `grid` whose entries are positive integers. Determine whether one straight cut can divide the matrix into two sections with the same element sum.

The cut may be horizontal, between two consecutive rows, or vertical, between two consecutive columns. It must span the entire grid, and both sections created by the cut must be nonempty. Only one orientation and one cut position are chosen; a horizontal and a vertical cut are not made together.

Return `true` when at least one legal cut produces equal section sums, and return `false` otherwise.

### Function Contract

**Inputs**

- `grid`: A rectangular matrix of positive integers.

Let $m$ be the number of rows and $n$ the number of columns. The constraints are $1 \le m,n \le 10^5$, $2 \le mn \le 10^5$, and $1 \le \texttt{grid[i][j]} \le 10^5$.

**Return value**

Return a boolean indicating whether one horizontal or vertical cut can form two nonempty sections with equal sums.

### Examples

#### Example 1

- **Input:** `grid = [[1,4],[2,3]]`
- **Output:** `true`
- **Explanation:** Cutting horizontally between the two rows gives sums $1+4=5$ and $2+3=5$.

#### Example 2

- **Input:** `grid = [[1,3],[2,4]]`
- **Output:** `false`
- **Explanation:** Neither the horizontal cut nor the vertical cut divides the total equally.

---
