# Flip Square Submatrix Vertically

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3643 |
| Difficulty | Easy |
| Topics | Array, Two Pointers, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/flip-square-submatrix-vertically/) |

## Problem Description

### Goal

You are given an $m\times n$ integer matrix `grid`. The zero-based coordinates `x` and `y` identify the top-left cell of a square submatrix whose side length is `k`. The constraints guarantee that the entire square lies inside the matrix.

Flip only that square vertically: its first row becomes its last row, its second row becomes its second-to-last row, and so on. Within each moved row, column order stays unchanged. Every cell outside the selected rows and columns must retain its original value. Return the updated matrix.

### Function Contract

**Inputs**

- `grid`: An $m\times n$ matrix of integers, with $1\le m,n\le 50$.
- `x`: The zero-based top row of the selected square.
- `y`: The zero-based left column of the selected square.
- `k`: The square's side length, satisfying $1\le k\le\min(m-x,n-y)$.

**Return value**

Return `grid` after vertically reversing the rows inside the specified $k\times k$ region.

### Examples

#### Example 1

- **Input:** `grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]`, `x = 1`, `y = 0`, `k = 3`
- **Output:** `[[1,2,3,4],[13,14,15,8],[9,10,11,12],[5,6,7,16]]`
- **Explanation:** The three-cell segments in rows 1 and 3 exchange places; the middle segment and column 3 remain unchanged.

#### Example 2

- **Input:** `grid = [[3,4,2,3],[2,3,4,2]]`, `x = 0`, `y = 2`, `k = 2`
- **Output:** `[[3,4,4,2],[2,3,2,3]]`
- **Explanation:** Only the final two columns belong to the square, so their two row segments exchange places.
