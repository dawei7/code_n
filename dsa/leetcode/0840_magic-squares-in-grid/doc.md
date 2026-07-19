# Magic Squares In Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 840 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Math, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/magic-squares-in-grid/) |

## Problem Description
### Goal
A 3 by 3 magic square contains the distinct numbers from `1` through `9` and has one common sum for each of its three rows, three columns, and both diagonals. The surrounding grid is not restricted to those nine values and may contain integers as large as `15`.

Given a rectangular integer `grid`, count how many contiguous 3 by 3 subgrids satisfy the complete magic-square definition. Subgrids at different top-left positions are counted separately, including when they overlap.

### Function Contract
**Inputs**

- `grid`: a rectangular matrix with $r$ rows and $c$ columns, where $1 \leq r,c \leq 10$.
- Every cell contains an integer from `0` through `15`.

**Return value**

Return the number of contiguous 3 by 3 subgrids whose entries are exactly the distinct values `1` through `9` and whose rows, columns, and diagonals have equal sums.

### Examples
**Example 1**

- Input: `grid = [[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]`
- Output: `1`

The left 3 by 3 window is magic, while the right window is not.

**Example 2**

- Input: `grid = [[8]]`
- Output: `0`

**Example 3**

- Input: `grid = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]`
- Output: `1`
