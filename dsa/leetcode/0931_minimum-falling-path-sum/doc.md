# Minimum Falling Path Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 931 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-falling-path-sum/) |

## Problem Description

### Goal

Given an $n \times n$ integer `matrix`, find the minimum sum among all falling paths through the matrix. A falling path begins at any element in the first row and includes exactly one element from every row until it reaches the last row.

After selecting position `(row, col)`, the next element must be in row `row + 1` and may be directly below at column `col`, diagonally left at `col - 1`, or diagonally right at `col + 1`, provided that column exists. Return the smallest possible sum of the selected values; matrix entries may be negative.

### Function Contract

**Inputs**

- `matrix`: an $n \times n$ integer matrix, where $1 \le n \le 100$ and every entry lies between $-100$ and $100$ inclusive.

**Return value**

Return the minimum sum of any valid falling path from the first row through the last row.

### Examples

**Example 1**

- Input: `matrix = [[2,1,3],[6,5,4],[7,8,9]]`
- Output: `13`
- Explanation: A minimum path can take values $1$, $5$, and $7$, or $1$, $4$, and $8$.

**Example 2**

- Input: `matrix = [[-19,57],[-40,-5]]`
- Output: `-59`
- Explanation: The path using $-19$ followed by $-40$ has the minimum sum.
