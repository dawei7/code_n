# Longest Line of Consecutive One in Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 562 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/) |

## Problem Description
### Goal
Given a binary matrix `mat`, find the longest line made entirely of consecutive `1` values. A valid line may run horizontally across a row, vertically down a column, diagonally from upper left to lower right, or anti-diagonally from upper right to lower left.

Return the number of cells in the longest such line. The cells must be adjacent in one fixed direction, and a `0` interrupts the line; turns, gaps, and combinations of different directions do not count as one line.

### Function Contract
**Inputs**

- `mat`: a binary matrix

**Return value**

- The length of the longest allowed line of consecutive ones

### Examples
**Example 1**

- Input: `mat = [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]]`
- Output: `3`

**Example 2**

- Input: `mat = [[1, 1, 1, 1]]`
- Output: `4`

**Example 3**

- Input: `mat = [[1], [1], [0], [1]]`
- Output: `2`
