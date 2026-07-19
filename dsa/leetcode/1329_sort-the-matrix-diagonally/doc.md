# Sort the Matrix Diagonally

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1329 |
| Difficulty | Medium |
| Topics | Array, Sorting, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/sort-the-matrix-diagonally/) |

## Problem Description
### Goal
In a matrix, a diagonal begins in either the top row or the leftmost column and continues one row down and one column right until it reaches an edge. Cells belong to the same such diagonal exactly when their row-minus-column difference is equal.

Given an integer matrix `mat`, sort the values on every top-left-to-bottom-right diagonal independently in ascending order. Values must remain on their original diagonal; only their order along that diagonal changes.

Return the resulting matrix. Diagonals of length one and diagonals whose values are already ascending remain unchanged.

### Function Contract
**Inputs**

- `mat`: an $m\times n$ integer matrix, where $1\le m,n\le100$ and $1\le\texttt{mat[i][j]}\le100$.

Let $L=\min(m,n)$ be the maximum diagonal length.

**Return value**

The matrix after each diagonal has been independently sorted in ascending order from its top-left end toward its bottom-right end.

### Examples
**Example 1**

- Input: `mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]`
- Output: `[[1,1,1,1],[1,2,2,2],[1,2,3,3]]`

**Example 2**

- Input: `mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]`
- Output: `[[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]`

**Example 3**

- Input: `mat = [[2,1],[1,2]]`
- Output: `[[2,1],[1,2]]`
- Explanation: Every diagonal is already ascending.
