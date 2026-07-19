# Matrix Cells in Distance Order

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1030 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, Geometry, Sorting, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/matrix-cells-in-distance-order/) |

## Problem Description

### Goal

You are given a matrix with `rows` rows and `cols` columns and a starting cell `(rCenter, cCenter)` inside that matrix.

Return the coordinates of every matrix cell, ordered from the smallest Manhattan distance to the largest Manhattan distance from the center. For cells ((r_1,c_1)) and ((r_2,c_2)), that distance is
$$
\lvert r_1-r_2\rvert+\lvert c_1-c_2\rvert.
$$
Cells at the same distance may appear in any relative order.

### Function Contract

**Inputs**

- `rows`: the number of matrix rows, where $1 \le \texttt{rows} \le 100$.
- `cols`: the number of matrix columns, where $1 \le \texttt{cols} \le 100$.
- `r_center`: the center row, where $0 \le \texttt{r_center} < \texttt{rows}$.
- `c_center`: the center column, where $0 \le \texttt{c_center} < \texttt{cols}$.
- Let $M=\texttt{rows}\cdot\texttt{cols}$ be the number of cells.

**Return value**

- All $M$ coordinate pairs `[row, col]` in non-decreasing Manhattan-distance order.

### Examples

**Example 1**

- Input: `rows = 1, cols = 2, r_center = 0, c_center = 0`
- Output: `[[0,0],[0,1]]`
- Explanation: The two distances are $0$ and $1$.

**Example 2**

- Input: `rows = 2, cols = 2, r_center = 0, c_center = 1`
- Output: `[[0,1],[0,0],[1,1],[1,0]]`
- Explanation: The distances are $0,1,1,2$; the two distance-one cells may be exchanged.

**Example 3**

- Input: `rows = 2, cols = 3, r_center = 1, c_center = 2`
- Output: `[[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]`
- Explanation: The distances are $0,1,1,2,2,3$, and other orders within equal-distance groups are valid.
