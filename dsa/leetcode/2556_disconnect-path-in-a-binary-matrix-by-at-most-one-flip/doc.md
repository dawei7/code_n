# Disconnect Path in a Binary Matrix by at Most One Flip

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2556 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Depth-First Search, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Disconnect Path in a Binary Matrix by at Most One Flip](https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/) |

## Problem Description

### Goal

You are given a 0-indexed $m \times n$ binary matrix `grid`. From `(row, col)`, movement is allowed only to `(row + 1, col)` or `(row, col + 1)`, and the destination cell must contain `1`. The matrix is disconnected when no such path leads from `(0, 0)` to `(m - 1, n - 1)`.

You may flip at most one cell, possibly none, changing either `0` to `1` or `1` to `0`. The start and finish cells cannot be flipped. Return `true` exactly when some permitted choice leaves the matrix disconnected.

### Function Contract

**Inputs**

- `grid`: A rectangular binary matrix with $1 \le m,n \le 1000$ and $1 \le mn \le 10^5$. Both endpoint cells are guaranteed to contain `1`.

**Return value**

- `True` if the grid is already disconnected or can be disconnected by one legal flip; otherwise `False`.

### Examples

#### Example 1

- **Input:** `grid = [[1, 1, 1], [1, 0, 0], [1, 1, 1]]`
- **Output:** `true`
- **Explanation:** The existing monotone path has an interior bottleneck that can be changed to `0`.

#### Example 2

- **Input:** `grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]`
- **Output:** `false`
- **Explanation:** Two internally disjoint routes remain, so one non-endpoint flip cannot destroy both.
