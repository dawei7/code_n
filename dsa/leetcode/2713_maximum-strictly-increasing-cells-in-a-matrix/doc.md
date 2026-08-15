# Maximum Strictly Increasing Cells in a Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2713 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search, Dynamic Programming, Memoization, Sorting, Matrix, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/) |

## Problem Description

### Goal

Given an $m \times n$ integer matrix `mat`, choose any cell as the starting point of a visit sequence. From the current cell, a move may jump to any other cell in the same row or the same column; adjacent positions do not receive special treatment.

A destination is legal only when its value is strictly greater than the current value. Continue making such moves for as long as desired, counting the starting cell and every destination visited. Return the greatest number of cells that any valid sequence can contain. Equal-valued cells cannot follow one another, even when they share a row or column.

### Function Contract

**Inputs**

- `mat`: An $m \times n$ matrix of integers.

The dimensions satisfy $1 \le m,n \le 10^5$ and $1 \le mn \le 10^5$. Every entry lies in the inclusive range $[-10^5,10^5]$.

**Return value**

Return the maximum number of cells in a strictly increasing sequence whose consecutive cells share a row or column.

### Examples

#### Example 1

- **Input:** `mat = [[3,1],[3,4]]`
- **Output:** `2`
- **Explanation:** Starting at value $1$, one may move to either value $3$ in its row or value $4$ in its column. No valid sequence visits three cells.

#### Example 2

- **Input:** `mat = [[1,1],[1,1]]`
- **Output:** `1`
- **Explanation:** A strict increase is impossible, so a sequence contains only its starting cell.

#### Example 3

- **Input:** `mat = [[3,1,6],[-9,5,7]]`
- **Output:** `4`
- **Explanation:** The values $-9 \to 1 \to 5 \to 7$ form a valid four-cell sequence by alternating column and row moves.
