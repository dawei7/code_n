# Maximum Rows Covered by Columns

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2397 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Backtracking, Bit Manipulation, Matrix, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-rows-covered-by-columns/) |

## Problem Description

### Goal

You are given an $m \times n$ binary matrix and an integer `numSelect`.
Choose exactly `numSelect` distinct columns. A row is covered when every
position containing `1` in that row belongs to one of the chosen columns.

A row containing no `1` values is covered regardless of which columns are
selected. Among all column sets of the required size, return the greatest
number of rows that can be covered simultaneously. The selected columns need
not be contiguous, and only the maximum count is required rather than the
selection itself.

### Function Contract

**Inputs**

- `matrix`: An $m \times n$ list of binary rows, where
  $1 \le m,n \le 12$.
- `numSelect`: The exact number $k$ of distinct columns to choose, with
  $1 \le k \le n$.

**Return value**

Return the maximum number of rows whose every `1` lies in the same selected
set of exactly $k$ columns. Rows containing only zeroes always count as
covered.

### Examples

#### Example 1

- **Input:** `matrix = [[0,0,0],[1,0,1],[0,1,1],[0,0,1]]`,
  `numSelect = 2`
- **Output:** `3`
- **Explanation:** Selecting columns 0 and 2 covers the zero row, `[1,0,1]`, and
  `[0,0,1]`.

#### Example 2

- **Input:** `matrix = [[1],[0]]`, `numSelect = 1`
- **Output:** `2`
- **Explanation:** Selecting the only column covers both rows.

#### Example 3

- **Input:** `matrix = [[1,1,1],[0,0,0],[1,0,0]]`, `numSelect = 1`
- **Output:** `2`
- **Explanation:** The all-zero row and the final row are covered by selecting
  column 0; the first row requires more selected columns.
