
# Increment Submatrices by One

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2536 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [increment-submatrices-by-one](https://leetcode.com/problems/increment-submatrices-by-one/) |

## Problem Description

### Goal

Begin with an $n \times n$ integer matrix whose entries are all zero. Each query has the form `[row1, col1, row2, col2]` and describes an inclusive rectangular submatrix: its rows run from `row1` through `row2`, and its columns run from `col1` through `col2`.

For every query, add one to each entry inside that rectangle. Return the matrix obtained after all queries have been applied.

### Function Contract

**Inputs**

- `n`: The positive side length of the square matrix.
- `queries`: The rectangle queries, each encoded as `[row1, col1, row2, col2]`.

Let $q = \lvert\texttt{queries}\rvert$. The coordinates are 0-indexed and satisfy $0 \leq \texttt{row1} \leq \texttt{row2} < n$ and $0 \leq \texttt{col1} \leq \texttt{col2} < n$. The public constraints permit $n \leq 500$ and $q \leq 10^4$.

**Return value**

Return an $n \times n$ matrix in which each entry equals the number of query rectangles that contain that position.

### Examples

**Example 1**

- Input: `n = 3, queries = [[1,1,2,2],[0,0,1,1]]`
- Output: `[[1,1,0],[1,2,1],[0,1,1]]`

The two rectangles overlap at row 1, column 1, so that entry is incremented twice.

**Example 2**

- Input: `n = 2, queries = [[0,0,1,1]]`
- Output: `[[1,1],[1,1]]`

The single query covers the entire matrix.
