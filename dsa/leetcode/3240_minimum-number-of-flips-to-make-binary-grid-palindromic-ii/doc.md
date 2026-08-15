# Minimum Number of Flips to Make Binary Grid Palindromic II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3240 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-ii/) |

## Problem Description

### Goal

You are given an $m \times n$ binary matrix `grid`. In one operation, choose any cell and change its value from `0` to `1` or from `1` to `0`.

After the operations, every row must read identically from left to right and right to left, and every column must read identically from top to bottom and bottom to top. The total number of cells whose final value is `1` must also be divisible by $4$.

Return the minimum number of cell flips needed to satisfy all three conditions simultaneously.

### Function Contract

**Inputs**

- `grid`: A nonempty rectangular matrix whose entries are `0` or `1`.

Let $m$ be the number of rows and $n$ the number of columns. The constraints guarantee $1 \le mn \le 2 \cdot 10^5$.

**Return value**

- The minimum number of flips required to make all rows and columns palindromic while leaving a multiple of four `1` cells.

### Examples

#### Example 1

- **Input:** `grid = [[1,0,0],[0,1,0],[0,0,1]]`
- **Output:** `3`

#### Example 2

- **Input:** `grid = [[0,1],[0,1],[0,0]]`
- **Output:** `2`

#### Example 3

- **Input:** `grid = [[1],[1]]`
- **Output:** `2`
