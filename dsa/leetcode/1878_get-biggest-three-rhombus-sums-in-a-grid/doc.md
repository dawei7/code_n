# Get Biggest Three Rhombus Sums in a Grid

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/) |
| Frontend ID | 1878 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Sorting, Heap (Priority Queue), Matrix, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Given an $M\times N$ integer matrix `grid`, consider rhombi whose four corners are centered on cells and whose sides follow the two grid diagonals. Such a shape is a square rotated by $45^\circ$. Its rhombus sum includes only cells on the border, not cells strictly inside it.

A rhombus may also have zero area: a single cell then forms both the entire shape and its border. Compute every valid border sum, discard duplicate numerical sums, and return the largest three distinct values in descending order. If the grid produces fewer than three distinct sums, return all that exist.

### Function Contract

**Inputs**

- `grid`: a rectangular $M\times N$ matrix, where $1 \le M,N \le 50$ and $1 \le \texttt{grid[r][c]} \le 10^5$.

**Return value**

- Return up to three distinct rhombus border sums, ordered from largest to smallest.

### Examples

**Example 1**

- Input: `grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]`
- Output: `[228,216,211]`

The three answers come from different valid borders; interior cells do not contribute.

**Example 2**

- Input: `grid = [[1,2,3],[4,5,6],[7,8,9]]`
- Output: `[20,9,8]`

The nonzero rhombus has border sum $2+4+6+8=20$, followed by two zero-area rhombi.

**Example 3**

- Input: `grid = [[7,7,7]]`
- Output: `[7]`

Only zero-area rhombi fit, and their equal sums count once.
