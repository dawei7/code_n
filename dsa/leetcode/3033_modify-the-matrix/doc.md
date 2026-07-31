# Modify the Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3033 |
| Difficulty | Easy |
| Topics | Array, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/modify-the-matrix/) |

## Problem Description
### Goal
Start with a 0-indexed $m \times n$ integer matrix named `matrix`. Create another 0-indexed matrix `answer` whose initial contents are equal to `matrix`.

For every position whose value is `-1`, replace that value in `answer` with the maximum element found in the same column of the original matrix. Values other than `-1` remain unchanged. Each column is guaranteed to contain at least one non-negative integer, so its replacement value is well defined and is never `-1`.

Return the completed matrix `answer` after every required replacement.

### Function Contract
Let $m$ be the number of rows, let $n$ be the number of columns, and let $N=mn$ be the number of matrix cells.

**Inputs**

- `matrix`: A rectangular integer matrix with $2 \le m,n \le 50$ and $-1 \le \texttt{matrix[i][j]} \le 100$. Every column contains at least one non-negative value.

**Return value**

Return a new $m \times n$ matrix in which each original `-1` is replaced by its column's maximum original value and every other cell retains its value.

### Examples
**Example 1**

- Input: `matrix = [[1,2,-1],[4,-1,6],[7,8,9]]`
- Output: `[[1,2,9],[4,8,6],[7,8,9]]`
- Explanation: Column 1 has maximum `8`, and column 2 has maximum `9`, so those values replace the two `-1` entries.

**Example 2**

- Input: `matrix = [[3,-1],[5,2]]`
- Output: `[[3,2],[5,2]]`
- Explanation: The maximum of the second column is `2`, which replaces its `-1` entry.
