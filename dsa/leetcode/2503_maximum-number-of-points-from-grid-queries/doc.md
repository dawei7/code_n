# Maximum Number of Points From Grid Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2503 |
| Difficulty | Hard |
| Topics | Array, Two Pointers, Breadth-First Search, Union-Find, Sorting, Heap (Priority Queue), Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/) |

## Problem Description

### Goal

You are given an $m\times n$ integer matrix `grid` and an array `queries` containing $k$ thresholds. Handle every query independently, always starting at the top-left cell `(0, 0)`.

For a threshold `queries[i]`, a cell can award one point on its first visit only when the threshold is strictly greater than that cell's value. From an eligible current cell, movement may continue to an orthogonally adjacent cell: up, down, left, or right. If the current cell is not eligible, the process stops without scoring it. Cells may be revisited, but revisits award no additional points.

For each query, maximize the total points obtainable and return the $k$ answers in the queries' original order.

### Function Contract

**Inputs**

- `grid`: An $m\times n$ matrix, where $2\le m,n\le1000$, $4\le mn\le10^5$, and every value is between $1$ and $10^6$ inclusive.
- `queries`: A list of $k$ thresholds, where $1\le k\le10^4$ and every threshold is between $1$ and $10^6$ inclusive.

**Return value**

A list of $k$ integers; result `i` is the maximum number of distinct cells that can score under `queries[i]`.

### Examples

#### Example 1

- **Input:** `grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]`
- **Output:** `[5,8,1]`

#### Example 2

- **Input:** `grid = [[5,2,1],[1,1,2]], queries = [3]`
- **Output:** `[0]`
- **Explanation:** The start value is not strictly below the threshold, so no cell scores.

#### Example 3

- **Input:** `grid = [[1,2],[2,1]], queries = [1,2,3]`
- **Output:** `[0,1,4]`
- **Explanation:** Equality is excluded. Threshold $2$ reaches only the start, while threshold $3$ reaches the entire grid.
