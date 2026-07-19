# As Far from Land as Possible

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1162 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/as-far-from-land-as-possible/) |

## Problem Description

### Goal

You are given an $n \times n$ grid containing only `0` and `1`. A `0` represents a water cell and a `1` represents a land cell.

Choose a water cell whose distance to its nearest land cell is as large as possible, and return that distance. Distance is Manhattan distance: between cells $(x_0, y_0)$ and $(x_1, y_1)$ it is $\lvert x_0 - x_1 \rvert + \lvert y_0 - y_1 \rvert$. If the grid contains no land or contains no water, return `-1` because no valid water-to-land distance exists.

### Function Contract

**Inputs**

- `grid`: A square $n \times n$ matrix, where $1 \le n \le 100$ and every entry is either `0` for water or `1` for land.

**Return value**

- The maximum, over all water cells, of the Manhattan distance to that cell's nearest land cell; or `-1` when the grid is all water or all land.

### Examples

**Example 1**

- Input: `grid = [[1,0,1],[0,0,0],[1,0,1]]`
- Output: `2`

The central water cell `(1, 1)` is two steps from its nearest land.

**Example 2**

- Input: `grid = [[1,0,0],[0,0,0],[0,0,0]]`
- Output: `4`

**Example 3**

- Input: `grid = [[1,1],[1,1]]`
- Output: `-1`
