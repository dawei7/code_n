# Paths in Matrix Whose Sum Is Divisible by K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2435 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Paths in Matrix Whose Sum Is Divisible by K](https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/) |

## Problem Description

### Goal

You are given a zero-indexed $m \times n$ matrix `grid` and an integer `k`. Start at the top-left cell `(0, 0)` and reach the bottom-right cell `(m - 1, n - 1)`. Each move must go exactly one cell down or one cell right.

For every such path, include both endpoints and every visited cell in its sum. Count the paths whose sum is divisible by `k`. Because the count can be large, return it modulo $10^9+7$.

### Function Contract

**Inputs**

- `grid`: A nonempty rectangular matrix of non-negative integers.
- `k`: The positive divisor used to classify path sums.

The dimensions satisfy $1 \le m,n \le 5\cdot10^4$ and $1 \le mn \le 5\cdot10^4$. Cell values lie in $[0,100]$, and $1 \le k \le 50$.

**Return value**

- The number of down/right paths whose cell sum is congruent to zero modulo `k`, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `grid = [[5, 2, 4], [3, 0, 5], [0, 7, 2]], k = 3`
- Output: `2`

Exactly two paths have sums divisible by 3.

**Example 2**

- Input: `grid = [[0, 0]], k = 5`
- Output: `1`

The only path has sum zero, which is divisible by 5.

**Example 3**

- Input: `grid = [[7, 3, 4, 9], [2, 3, 6, 2], [2, 3, 7, 0]], k = 1`
- Output: `10`

Every path sum is divisible by 1, and the grid has ten down/right paths.
