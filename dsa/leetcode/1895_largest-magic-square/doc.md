# Largest Magic Square

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1895 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/largest-magic-square/) |

## Problem Description

### Goal

A square region of side length $k$ is magic when the sum along each of its $k$ rows, the sum along each of its $k$ columns, and the sums along its two corner-to-corner diagonals are all the same. Its entries are not required to be distinct, and every single-cell square satisfies the definition.

Given a rectangular integer matrix, consider every contiguous square subgrid contained within it. Return the side length of the largest one that is magic.

### Function Contract

**Inputs**

- `grid`: an $M \times N$ matrix of positive integers, where $1 \le M, N \le 50$ and every entry is at most $10^6$.

Let $S = \min(M, N)$ be the greatest possible side length of a square inside the matrix.

**Return value**

Return the largest side length $k$ for which some contiguous $k \times k$ subgrid has equal row, column, and diagonal sums. The result is always at least $1$.

### Examples

**Example 1**

- Input: `grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]`
- Output: `3`
- Explanation: The square with top-left entry `5` has every row, column, and diagonal sum equal to $12$.

**Example 2**

- Input: `grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]`
- Output: `2`

**Example 3**

- Input: `grid = [[1000000]]`
- Output: `1`
- Explanation: A single cell is magic by definition.
