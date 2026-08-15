# Sort Matrix by Diagonals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3446 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sort-matrix-by-diagonals/) |

## Problem Description

### Goal

Given an $n\times n$ integer matrix `grid`, reorder the values independently along every diagonal that runs from the upper left toward the lower right. The main diagonal belongs to the bottom-left half of the matrix.

For every diagonal that begins in the first column, including the main diagonal, arrange its values in non-increasing order when read from upper left to lower right. For every remaining diagonal, which begins in the first row to the right of the main diagonal, arrange its values in non-decreasing order. Return the resulting matrix without moving any value to a different diagonal.

### Function Contract

**Inputs**

- `grid`: An $n\times n$ matrix of integers, where $1\le n\le10$ and every entry lies between $-10^5$ and $10^5$, inclusive.

**Return value**

Return the matrix after sorting bottom-left diagonals in non-increasing order and top-right diagonals in non-decreasing order.

### Examples

#### Example 1

- **Input:** `grid = [[1,7,3],[9,8,2],[4,5,6]]`
- **Output:** `[[8,2,3],[9,6,7],[4,5,1]]`

The main diagonal becomes `[8,6,1]`, while the top-right diagonal `[7,2]` becomes `[2,7]`.

#### Example 2

- **Input:** `grid = [[0,1],[1,2]]`
- **Output:** `[[2,1],[1,0]]`

Only the main diagonal has more than one entry, and it is arranged in non-increasing order.

#### Example 3

- **Input:** `grid = [[1]]`
- **Output:** `[[1]]`

A one-element diagonal already satisfies either ordering.
