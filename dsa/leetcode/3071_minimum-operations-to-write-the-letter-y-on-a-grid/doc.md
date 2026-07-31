# Minimum Operations to Write the Letter Y on a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3071 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Matrix, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/) |

## Problem Description

### Goal

You are given a zero-indexed $n \times n$ matrix `grid`, where $n$ is odd and every cell contains `0`, `1`, or `2`.

A cell belongs to the letter Y when it lies on one of three segments: the diagonal from the top-left corner to the center, the diagonal from the top-right corner to the center, or the vertical segment from the center to the bottom edge. The center cell belongs to all three descriptions but is still one cell.

The grid displays a valid Y exactly when all Y cells share one value, all remaining cells share another value, and those two values are different. In one operation, you may replace any cell with `0`, `1`, or `2`. Return the minimum number of operations required to make the grid display a valid Y.

### Function Contract

**Inputs**

- `grid`: An $n \times n$ matrix containing only `0`, `1`, and `2`, where $3 \le n \le 49$ and $n$ is odd.

**Return value**

Return the minimum number of individual cell-value changes needed to produce the required Y and background values.

### Examples

**Example 1**

- Input: `grid = [[1,2,2],[1,1,0],[0,1,0]]`
- Output: `3`
- Explanation: Three changes make every Y cell `1` and every background cell `0`.

**Example 2**

- Input: `grid = [[0,1,0,1,0],[2,1,0,1,2],[2,2,2,0,1],[2,2,2,2,2],[2,1,2,2,2]]`
- Output: `12`
- Explanation: The minimum is achieved by assigning one value to all Y cells and a different value to all other cells, requiring twelve changes.
