# Minimum Time to Visit a Cell In a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2577 |
| Difficulty | Hard |
| Topics | Array, Breadth-First Search, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path |
| Official Link | [minimum-time-to-visit-a-cell-in-a-grid](https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/) |

## Problem Description & Examples
### Goal
Given a 2D grid of size `m x n` where each cell contains a non-negative integer representing the earliest time you can enter that cell, determine the minimum time required to travel from the top-left corner `(0, 0)` to the bottom-right corner `(m-1, n-1)`. You can move to adjacent cells (up, down, left, right) at each time step, but you can only enter a cell if your current time is greater than or equal to the value stored in that cell. If you arrive at an adjacent cell earlier than its required time, you must "wait" by moving back and forth between the current cell and an adjacent one until the time is sufficient to enter the target cell.

### Function Contract
**Inputs**

- `grid`: A 2D list of integers where `grid[i][j]` is the minimum time required to enter cell `(i, j)`.

**Return value**

- An integer representing the minimum time to reach `(m-1, n-1)`. If it is impossible to reach the destination, return `-1`.

### Examples
**Example 1**

- Input: `grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]`
- Output: `7`

**Example 2**

- Input: `grid = [[0,2,4],[3,2,1]]`
- Output: `7`

**Example 3**

- Input: `grid = [[0,1],[1,2]]`
- Output: `3`

---

## Underlying Base Algorithm(s)
The problem is modeled as a shortest-path problem on a weighted graph. Since we need to find the minimum time, **Dijkstra's Algorithm** is the optimal choice. The state is defined by `(time, row, col)`. When moving from a cell, if the current time plus one is less than the target cell's requirement, we calculate the wait time. If the difference between the target requirement and the current time is odd, we can reach the target exactly at the requirement time; if even, we must wait one extra unit to maintain parity.

---

## Complexity Analysis
- **Time Complexity**: `O(E log V)` where `E` is the number of edges (4 per cell) and `V` is the number of vertices (`m * n`). This simplifies to `O(m * n * log(m * n))`.
- **Space Complexity**: `O(m * n)` to store the `visited` matrix and the priority queue.
