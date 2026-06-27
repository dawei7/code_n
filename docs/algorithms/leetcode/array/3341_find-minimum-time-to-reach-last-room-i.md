# Find Minimum Time to Reach Last Room I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3341 |
| Difficulty | Medium |
| Topics | Array, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path |
| Official Link | [find-minimum-time-to-reach-last-room-i](https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/) |

## Problem Description & Examples
### Goal
Given a 2D grid representing rooms, where each cell contains a non-negative integer representing the earliest time you can enter that room, calculate the minimum time required to travel from the top-left corner (0, 0) to the bottom-right corner (n-1, m-1). You can move to adjacent cells (up, down, left, right) at any time, but you must wait until the specified time in the destination cell if you arrive earlier. Each move takes exactly 1 unit of time.

### Function Contract
**Inputs**

- `moveTime`: A 2D list of integers where `moveTime[i][j]` is the earliest time you can enter the room at row `i` and column `j`.

**Return value**

- An integer representing the minimum time to reach the bottom-right cell.

### Examples
**Example 1**

- Input: `moveTime = [[0,4],[4,4]]`
- Output: `6`

**Example 2**

- Input: `moveTime = [[0,0,0],[0,0,0]]`
- Output: `3`

**Example 3**

- Input: `moveTime = [[0,1],[1,2]]`
- Output: `3`

---

## Underlying Base Algorithm(s)
Dijkstra's Algorithm. Since the grid can be modeled as a weighted graph where edge weights are dynamic based on the arrival time and the cell's entry requirement, Dijkstra's is the optimal approach to find the shortest path in a graph with non-negative edge weights.

---

## Complexity Analysis
- **Time Complexity**: `O(N * M * log(N * M))`, where N is the number of rows and M is the number of columns. Each cell is pushed and popped from the priority queue at most once.
- **Space Complexity**: `O(N * M)` to store the `dist` matrix and the priority queue.
