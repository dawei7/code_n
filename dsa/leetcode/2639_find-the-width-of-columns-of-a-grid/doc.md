# Find the Width of Columns of a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2639 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/) |

## Problem Description

### Goal

You are given an $m \times n$ integer matrix `grid`. The width of a column is the greatest written length of any integer in that column. A negative integer's written length includes its leading minus sign, while a nonnegative integer's length is simply its number of decimal digits.

Determine every column width independently and return an array `ans` of length $n$, where `ans[i]` is the width of column $i$. Each matrix entry lies between $-10^9$ and $10^9$, inclusive, so ordinary decimal notation is sufficient and zero has width one.

### Function Contract

**Inputs**

- `grid`: An $m \times n$ rectangular matrix of integers, where $1 \le m,n \le 100$ and $-10^9 \le \texttt{grid[r][c]} \le 10^9$.

Here, $m$ is the number of rows and $n$ is the number of columns.

**Return value**

- Return a length-$n$ integer array whose entry at index $i$ is the maximum decimal-string length among the values in column $i$.

### Examples

#### Example 1

- **Input:** `grid = [[1], [22], [333]]`
- **Output:** `[3]`
- **Explanation:** The only column contains values of lengths one, two, and three, so its width is three.

#### Example 2

- **Input:** `grid = [[-15, 1, 3], [15, 7, 12], [5, 6, -2]]`
- **Output:** `[3, 1, 2]`
- **Explanation:** The first column needs three characters for `-15`; the other columns need at most one and two characters, respectively.
