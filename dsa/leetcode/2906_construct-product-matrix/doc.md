# Construct Product Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2906 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/construct-product-matrix/) |

## Problem Description
### Goal
You are given a 0-indexed integer matrix `grid` with $n$ rows and $m$ columns. Construct another $n\times m$ matrix `p` in which `p[i][j]` equals the product of every value in `grid` except `grid[i][j]`, reduced modulo $12345$.

The excluded position changes for every output cell. Return the complete product matrix without using division to remove the current value from a total product.

### Function Contract
**Inputs**

- `grid`: A rectangular integer matrix with $1\le n,m\le 10^5$, $2\le nm\le 10^5$, and $1\le\texttt{grid}[i][j]\le 10^9$.

Let $N=nm$ denote the total number of cells.

**Return value**

Return an $n\times m$ matrix whose cell at `(i, j)` is the product of all other $N-1$ input values modulo $12345$.

### Examples
**Example 1**

- Input: `grid = [[1, 2], [3, 4]]`
- Output: `[[24, 12], [8, 6]]`
- Explanation: Each output omits the input at the same coordinates; for example, the first value is `2 * 3 * 4 = 24`.

**Example 2**

- Input: `grid = [[12345], [2], [1]]`
- Output: `[[2], [0], [0]]`
- Explanation: Omitting `12345` leaves product $2$, while either other omission leaves a product divisible by $12345$.
