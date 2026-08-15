# Count Submatrices With Equal Frequency of X and Y

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3212 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/) |

## Problem Description

### Goal

`grid` is a rectangular character matrix containing only `"X"`, `"Y"`, and `"."`. Count the submatrices that contain the top-left cell `grid[0][0]`.

A counted submatrix must contain the same number of `"X"` and `"Y"` cells, and that equal count must be positive because at least one `"X"` is required. Dot cells contribute to neither frequency.

Return the number of submatrices satisfying all three conditions.

### Function Contract

**Inputs**

- `grid`: A nonempty rectangular matrix with $1 \le r,c \le 1000$, where $r$ is the row count, $c$ is the column count, and every cell is `"X"`, `"Y"`, or `"."`.

**Return value**

- The number of top-left-anchored rectangles whose `"X"` and `"Y"` counts are equal and nonzero.

### Examples

#### Example 1

- **Input:** `grid = [["X","Y","."],["Y",".","."]]`
- **Output:** `3`

#### Example 2

- **Input:** `grid = [["X","X"],["X","Y"]]`
- **Output:** `0`
- **Explanation:** No anchored rectangle contains equal frequencies of `"X"` and `"Y"`.

#### Example 3

- **Input:** `grid = [[".","."],[".","."]]`
- **Output:** `0`
- **Explanation:** Equal zero frequencies do not qualify because at least one `"X"` is required.
