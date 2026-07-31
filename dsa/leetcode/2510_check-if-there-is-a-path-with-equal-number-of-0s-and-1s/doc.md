# Check if There is a Path With Equal Number of 0's And 1's

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2510 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-there-is-a-path-with-equal-number-of-0s-and-1s/) |

## Problem Description
### Goal
You are given a 0-indexed binary matrix `grid` with `r` rows and `c` columns. From a cell `(row, col)`, a path may move one cell down to `(row + 1, col)` or one cell right to `(row, col + 1)` whenever that destination remains inside the matrix.

Determine whether at least one path from the top-left cell `(0, 0)` to the bottom-right cell `(r - 1, c - 1)` visits an equal number of cells containing `0` and cells containing `1`. Both endpoint cells are included in the counts.

### Function Contract
**Inputs**

- `grid`: An `r` by `c` matrix whose entries are either `0` or `1`.

The constraints are $2 \le r,c \le 100$.

**Return value**

`True` if some down-and-right path visits equally many zeros and ones; otherwise, `False`.

### Examples
**Example 1**

- Input: `grid = [[0,1,0,0],[0,1,0,0],[1,0,1,0]]`
- Output: `true`
- Explanation: A valid path visits six cells containing three zeros and three ones.

**Example 2**

- Input: `grid = [[1,1,0],[0,0,1],[1,0,0]]`
- Output: `false`
- Explanation: None of the paths from the top-left to the bottom-right cell has equal counts.
