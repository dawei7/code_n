# Minimum Absolute Difference in Sliding Submatrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3567 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/) |

## Problem Description

### Goal

Slide a square window of side length `k` across an integer matrix. For every contiguous $k\times k$ submatrix, consider the distinct numeric values that occur inside it and find the smallest absolute difference between any two of those values.

Duplicate occurrences of the same value do not form a pair of distinct values. If a window contains only one distinct value—including every $1\times1$ window—its answer is zero.

Return one answer for every legal top-left window position. The output preserves those positions as a matrix: entry `(i, j)` describes the window whose top-left cell is `grid[i][j]`.

### Function Contract

**Inputs**

- `grid`: An $m\times n$ integer matrix, where $1\le m,n\le30$ and every entry lies between $-10^5$ and $10^5$ inclusive.
- `k`: The side length of each square window, with $1\le k\le\min(m,n)$.

Let $R=m-k+1$ and $C=n-k+1$ be the output dimensions.

**Return value**

Return an $R\times C$ integer matrix in which each entry is the minimum gap between distinct values in its corresponding window, or zero when that window has fewer than two distinct values.

### Examples

#### Example 1

- **Input:** `grid = [[1,8],[3,-2]], k = 2`
- **Output:** `[[2]]`
- **Explanation:** Sorting the distinct values as `[-2,1,3,8]` shows the smallest adjacent gap is 2.

#### Example 2

- **Input:** `grid = [[3,-1]], k = 1`
- **Output:** `[[0,0]]`
- **Explanation:** Each one-cell window has only one distinct value.

#### Example 3

- **Input:** `grid = [[1,-2,3],[2,3,5]], k = 2`
- **Output:** `[[1,2]]`
- **Explanation:** The left window has minimum distinct-value gap 1, while the right window has gap 2.

---
