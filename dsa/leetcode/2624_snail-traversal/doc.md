# Snail Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2624 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/snail-traversal/) |

## Problem Description

### Goal

Extend JavaScript arrays with a `snail` method that rearranges the array's values into a matrix with the requested number of rows and columns.

Read the source array in its existing order and fill the matrix one column at a time. The first column is filled from top to bottom, the second from bottom to top, and each later column alternates direction in the same way. This produces a vertical zigzag resembling a snail traversal.

The dimensions must use every source value exactly once. If `rowsCount * colsCount` does not equal the array length, return an empty array instead of a partially filled matrix.

### Function Contract

**Inputs**

- `nums`: The source array of numbers, in the order in which they must be placed.
- `rowsCount`: The positive number of rows in the requested matrix.
- `colsCount`: The positive number of columns in the requested matrix.

Let $n$ be the length of `nums`. The constraints guarantee $0 \le n \le 250$, $1 \le \texttt{rowsCount}, \texttt{colsCount} \le 250$, and every value lies between $1$ and $1000$.

**Return value**

Return the `rowsCount` by `colsCount` snail matrix when $n = \texttt{rowsCount} \cdot \texttt{colsCount}$. Otherwise, return `[]`.

### Examples

**Example 1**

- Input: `nums = [19,10,3,7,9,8,5,2,1,17,16,14,12,18,6,15,4,20,11,13]`, `rowsCount = 5`, `colsCount = 4`
- Output: `[[19,17,16,13],[10,1,14,11],[3,2,12,20],[7,5,18,4],[9,8,6,15]]`
- Explanation: Consecutive groups of five values form columns. Their directions alternate downward, upward, downward, and upward.

**Example 2**

- Input: `nums = [1,2,3,4]`, `rowsCount = 1`, `colsCount = 4`
- Output: `[[1,2,3,4]]`
- Explanation: With only one row, both traversal directions place every value in that same row.

**Example 3**

- Input: `nums = [1,3]`, `rowsCount = 2`, `colsCount = 2`
- Output: `[]`
- Explanation: A $2 \times 2$ matrix needs four values, so the requested dimensions are invalid for this array.
