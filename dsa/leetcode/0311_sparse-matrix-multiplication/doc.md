# Sparse Matrix Multiplication

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 311 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sparse-matrix-multiplication/) |

## Problem Description
### Goal
Given an $m \times k$ integer matrix `mat1` and a compatible $k \times n$ integer matrix `mat2`, compute their standard matrix product. Output entry `(i, j)` is the sum of `mat1[i][p] * mat2[p][j]` over every shared-dimension index `p`.

Return the complete dense $m \times n$ result matrix, preserving negative values and zero sums. Both inputs may be sparse, with many entries known to be zero, so avoid unnecessary multiplication and accumulation involving those zero entries. The mathematical result must remain identical to ordinary multiplication; sparsity changes the work performed, not the output format or arithmetic definition.

### Function Contract
**Inputs**

- `mat1`: an `m × k` integer matrix
- `mat2`: a `k × n` integer matrix

**Return value**

The dense `m × n` product matrix `mat1 * mat2`.

### Examples
**Example 1**

- Input: `mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]`
- Output: `[[7,0,0],[-7,0,3]]`

**Example 2**

- Input: `mat1 = [[0,0]], mat2 = [[1],[2]]`
- Output: `[[0]]`

**Example 3**

- Input: `mat1 = [[2,0],[0,3]], mat2 = [[1,0],[0,1]]`
- Output: `[[2,0],[0,3]]`
