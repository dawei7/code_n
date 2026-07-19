# Maximum Non Negative Product in a Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1594 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/) |

## Problem Description
### Goal
You are given an $m \times n$ integer matrix `grid`. Begin at its top-left cell `(0, 0)`. Each move must go exactly one cell to the right or one cell down, and the path must finish at the bottom-right cell `(m - 1, n - 1)`. A path's product is obtained by multiplying every cell value visited, including both endpoints.

Among all such paths, find the greatest product that is non-negative. If every path product is negative, return `-1`. Otherwise, return the chosen product modulo $10^9 + 7$. The comparison must use the complete products: applying the modulus before selecting the maximum can change their ordering and is not valid.

### Function Contract
**Inputs**

- `grid`: an $m \times n$ matrix with $1 \le m,n \le 15$ and $-4 \le \texttt{grid[i][j]} \le 4$.

**Return value**

Return the maximum non-negative top-left-to-bottom-right path product modulo $10^9 + 7$, or `-1` if no path has a non-negative product.

### Examples
**Example 1**

- Input: `grid = [[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]]`
- Output: `-1`

**Example 2**

- Input: `grid = [[1, -2, 1], [1, -2, 1], [3, -4, 1]]`
- Output: `8`
- Explanation: One maximizing path has product `1 * 1 * -2 * -4 * 1 = 8`.

**Example 3**

- Input: `grid = [[1, 3], [0, -4]]`
- Output: `0`
