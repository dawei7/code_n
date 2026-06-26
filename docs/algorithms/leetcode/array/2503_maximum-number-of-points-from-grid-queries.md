# Maximum Number of Points From Grid Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2503 |
| Difficulty | Hard |
| Topics | Array, Two Pointers, Breadth-First Search, Union-Find, Sorting, Heap (Priority Queue), Matrix |
| Official Link | [maximum-number-of-points-from-grid-queries](https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/) |

## Problem Description & Examples
### Goal
Given an $m \times n$ grid of integers and a list of queries, determine for each query $k$ the maximum number of cells you can visit starting from the top-left cell $(0, 0)$. You can only move to adjacent cells (up, down, left, right) if the value in the target cell is strictly less than $k$.

### Function Contract
**Inputs**

- `grid`: A 2D list of integers representing the grid values.
- `queries`: A list of integers representing the threshold values for each query.

**Return value**

- A list of integers where the $i$-th element is the count of reachable cells for the $i$-th query.

### Examples
**Example 1**

- Input: `grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]`
- Output: `[5,8,0]`

**Example 2**

- Input: `grid = [[5,2,1],[1,1,2]], queries = [3]`
- Output: `[0]`

**Example 3**

- Input: `grid = [[1,0],[0,1]], queries = [1,2]`
- Output: `[0,4]`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Min-Priority Queue (Dijkstra-like approach)** combined with **Offline Query Processing**. By sorting the queries, we can process them in increasing order. We maintain a priority queue of reachable boundary cells, always expanding into the smallest available neighbor. This allows us to incrementally count reachable cells as the threshold $k$ increases.

---

## Complexity Analysis
- **Time Complexity**: $O(MN \log(MN) + Q \log Q)$, where $M \times N$ is the grid size and $Q$ is the number of queries. We visit each cell once and perform heap operations, and we sort the queries.
- **Space Complexity**: $O(MN + Q)$ to store the grid, the priority queue, and the results.
