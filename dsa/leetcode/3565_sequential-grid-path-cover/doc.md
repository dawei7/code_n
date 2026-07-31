# Sequential Grid Path Cover

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3565 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Recursion, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sequential-grid-path-cover/) |

## Problem Description

### Goal

Consider an $m\times n$ grid in which exactly $k$ cells contain the distinct checkpoint values from $1$ through $k$. Every other cell contains zero. A path may begin at any cell and may move one step at a time up, down, left, or right.

Construct a path that visits every grid cell exactly once. When the path reaches numbered cells, their values must appear in the order $1,2,\ldots,k$; zero-valued cells may occur anywhere between those checkpoints.

Return the coordinates in visit order. Any valid path is acceptable. Return an empty array when no path can satisfy both the full-cover and checkpoint-order requirements.

### Function Contract

**Inputs**

- `grid`: A nonempty rectangular integer matrix with $1\le m,n\le5$. Exactly one cell contains each value from $1$ through `k`; all remaining cells contain zero.
- `k`: The number of ordered checkpoints, with $1\le k\le mn$.

Let $V=mn$ be the number of grid cells.

**Return value**

Return a list of $V$ coordinate pairs `[row, column]` describing a valid path, or `[]` if none exists. Coordinates are zero-based.

### Examples

**Example 1**

- Input: `grid = [[0,0,0],[0,1,2]], k = 2`
- Output: `[[0,0],[1,0],[1,1],[1,2],[0,2],[0,1]]`
- Explanation: Consecutive coordinates share an edge, every cell appears once, and checkpoints 1 and 2 occur in order.

**Example 2**

- Input: `grid = [[1,0,4],[3,0,2]], k = 4`
- Output: `[]`
- Explanation: No Hamiltonian grid path can encounter all four numbered cells in their required order.

---
