# Matrix Block Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1314 |
| Difficulty | Medium |
| Topics | Array, Matrix, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/matrix-block-sum/) |

## Problem Description
### Goal
Given an $m\times n$ integer matrix `mat` and a positive integer `k`, produce an answer matrix with the same dimensions. For each output cell `answer[i][j]`, sum every `mat[r][c]` whose row lies from $i-k$ through $i+k$ and whose column lies from $j-k$ through $j+k$.

Only valid matrix positions contribute. In other words, the square block centered at `(i, j)` is clipped at the top, bottom, left, and right boundaries rather than padded with additional values.

### Function Contract
**Inputs**

- `mat`: an $m\times n$ matrix, where $1\le m,n\le100$.
- Every `mat[i][j]` is between 1 and 100 inclusive.
- `k`: the block radius, where $1\le k\le100$.

**Return value**

An $m\times n$ matrix `answer` satisfying

$$
\texttt{answer[i][j]}
=
\sum_{r=\max(0,i-k)}^{\min(m-1,i+k)}
\sum_{c=\max(0,j-k)}^{\min(n-1,j+k)}
\texttt{mat[r][c]}.
$$

### Examples
**Example 1**

- Input: `mat = [[1,2,3],[4,5,6],[7,8,9]]`, `k = 1`
- Output: `[[12,21,16],[27,45,33],[24,39,28]]`

**Example 2**

- Input: the same matrix, `k = 2`
- Output: `[[45,45,45],[45,45,45],[45,45,45]]`

**Example 3**

- Input: `mat = [[5]]`, `k = 1`
- Output: `[[5]]`
