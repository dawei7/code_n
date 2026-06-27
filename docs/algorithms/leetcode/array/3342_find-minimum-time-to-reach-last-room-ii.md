# Find Minimum Time to Reach Last Room II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3342 |
| Difficulty | Medium |
| Topics | Array, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path |
| Official Link | [find-minimum-time-to-reach-last-room-ii](https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/) |

## Problem Description & Examples
### Goal
Given a 2D grid representing move times, calculate the minimum time required to travel from the top-left cell (0, 0) to the bottom-right cell (n-1, m-1). Moving to an adjacent cell takes time equal to the maximum of the cell's value plus one, or the current time plus one. Crucially, the time cost alternates between adding 1 and adding 2 to the required wait time for each consecutive step taken.

### Function Contract
**Inputs**

- `moveTime`: A 2D list of integers where `moveTime[i][j]` represents the earliest time you can enter cell `(i, j)`.

**Return value**

- An integer representing the minimum time to reach the bottom-right corner.

### Examples
**Example 1**

- Input: `moveTime = [[0,3,2],[0,2,4]]`
- Output: `3`

**Example 2**

- Input: `moveTime = [[0,0,0],[0,0,0]]`
- Output: `3`

**Example 3**

- Input: `moveTime = [[0,1],[1,2]]`
- Output: `4`

---

## Underlying Base Algorithm(s)
Dijkstra's Algorithm. Since the edge weights are dynamic and depend on the number of steps taken (parity of the path length), we expand the state space to `(time, r, c, parity)` to ensure we always find the shortest path in a graph with non-negative edge weights.

---

## Complexity Analysis
- **Time Complexity**: `O(N * M * log(N * M))`, where N and M are the dimensions of the grid, due to the priority queue operations.
- **Space Complexity**: `O(N * M)`, required to store the minimum time to reach each cell for both parity states.
