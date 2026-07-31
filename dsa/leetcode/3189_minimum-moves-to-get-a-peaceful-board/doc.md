# Minimum Moves to Get a Peaceful Board

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3189 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting, Counting Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-moves-to-get-a-peaceful-board/) |

## Problem Description

### Goal

An $n \times n$ chessboard contains exactly $n$ rooks. The position
`rooks[i] = [x_i, y_i]` gives the row and column of the $i$-th rook, and the
input never places two rooks in the same cell.

One move shifts one rook by one cell to a vertically or horizontally adjacent
cell. Transform the position into a peaceful board, meaning that every row and
every column contains exactly one rook. Two rooks may not occupy the same cell
at any intermediate point. Return the minimum total number of unit moves needed.

### Function Contract

**Inputs**

- `rooks`: A list of $n$ distinct board cells, where each pair `[x_i, y_i]`
  satisfies $0 \le x_i, y_i < n$ and $1 \le n \le 500$.

**Return value**

Return the minimum number of single-cell horizontal or vertical moves required
to make the board peaceful.

### Examples

**Example 1**

- Input: `rooks = [[0, 0], [1, 0], [1, 1]]`
- Output: `3`

**Example 2**

- Input: `rooks = [[0, 0], [0, 1], [0, 2], [0, 3]]`
- Output: `6`
