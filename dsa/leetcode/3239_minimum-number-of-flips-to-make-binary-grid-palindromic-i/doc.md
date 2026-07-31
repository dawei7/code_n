# Minimum Number of Flips to Make Binary Grid Palindromic I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3239 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/) |

## Problem Description

### Goal

You are given an $m\times n$ binary matrix `grid`. A row or column is palindromic when its values are identical in forward and reverse order. One flip changes any chosen cell from `0` to `1` or from `1` to `0`.

Return the minimum number of cell flips needed to satisfy either of two alternatives: every row is palindromic, or every column is palindromic. Only one complete orientation is required; rows and columns do not both need to become palindromic.

### Function Contract

**Inputs**

- `grid`: A nonempty rectangular binary matrix with $1\leq m n\leq2\cdot10^5$.

Let $m$ be its row count and $n$ its column count.

**Return value**

Return the smaller flip count for making all rows palindromic and making all columns palindromic.

### Examples

**Example 1**

- Input: `grid = [[1,0,0],[0,0,0],[0,0,1]]`
- Output: `2`
- Explanation: Two flips can make every row palindromic.

**Example 2**

- Input: `grid = [[0,1],[0,1],[0,0]]`
- Output: `1`
- Explanation: One flip can make every column palindromic.

**Example 3**

- Input: `grid = [[1],[0]]`
- Output: `0`
- Explanation: Every one-cell row is already palindromic.
