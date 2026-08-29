# Count Paths With the Given XOR Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3393 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-paths-with-the-given-xor-value/) |

## Problem Description

### Goal

An $m\times n$ integer grid defines paths that begin at the top-left cell `(0, 0)` and finish at the bottom-right cell `(m - 1, n - 1)`. From any cell, a path may move one position right or one position down whenever that destination remains inside the grid.

The value of a path is the bitwise XOR of every grid value it visits, including both endpoints. Count the paths whose value is exactly `k`. Because the count may be large, return it modulo $10^9+7$.

### Function Contract

**Inputs**

- `grid`: A rectangular list of integer rows with $1\le m,n\le300$. Every cell value is in `[0,15]`.
- `k`: The required path XOR, also in `[0,15]`.

Let $m$ be the row count and $n$ the column count. Every valid path visits exactly $m+n-1$ cells.

**Return value**

- The number of right/down paths from `(0, 0)` to `(m - 1, n - 1)` whose cumulative XOR equals `k`, modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `grid = [[2, 1, 5], [7, 10, 0], [12, 6, 4]], k = 11`
- **Output:** `3`

Exactly three right/down routes have cumulative XOR 11.

#### Example 2

- **Input:** `grid = [[1, 3, 3, 3], [0, 3, 3, 2], [3, 0, 1, 1]], k = 2`
- **Output:** `5`

#### Example 3

- **Input:** `grid = [[1, 1, 1, 2], [3, 0, 3, 2], [3, 0, 2, 2]], k = 10`
- **Output:** `0`

No valid route produces the target XOR.
