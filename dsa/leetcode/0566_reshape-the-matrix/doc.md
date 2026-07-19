# Reshape the Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 566 |
| Difficulty | Easy |
| Topics | Array, Matrix, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/reshape-the-matrix/) |

## Problem Description
### Goal
Given an $m \times n$ matrix `mat` and two requested dimensions `r` and `c`, reshape the matrix into `r` rows and `c` columns when that shape can hold exactly the same number of elements. Read the original matrix in row-traversing order and place the values into the new matrix in that same order.

Return the reshaped matrix when $m \cdot n$ equals $r \cdot c$. If the requested dimensions would lose elements or require additional ones, reshaping is impossible and you must return the original matrix unchanged.

### Function Contract
**Inputs**

- `mat`: a non-empty rectangular integer matrix
- `r`: the requested row count
- `c`: the requested column count

**Return value**

- The row-major reshaped matrix, or the original matrix when reshaping is impossible

### Examples
**Example 1**

- Input: `mat = [[1, 2], [3, 4]], r = 1, c = 4`
- Output: `[[1, 2, 3, 4]]`

**Example 2**

- Input: `mat = [[1, 2], [3, 4]], r = 2, c = 4`
- Output: `[[1, 2], [3, 4]]`

**Example 3**

- Input: `mat = [[1, 2, 3, 4]], r = 2, c = 2`
- Output: `[[1, 2], [3, 4]]`
