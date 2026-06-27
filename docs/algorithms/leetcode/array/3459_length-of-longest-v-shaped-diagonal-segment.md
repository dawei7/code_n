# Length of Longest V-Shaped Diagonal Segment

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3459 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Memoization, Matrix |
| Official Link | [length-of-longest-v-shaped-diagonal-segment](https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/) |

## Problem Description & Examples
### Goal
Given a 2D grid containing values 0, 1, and 2, find the length of the longest "V-shaped" diagonal segment. A V-shaped segment starts at a '2', moves diagonally through a sequence of '1's, reaches a '0' (the vertex), and then moves diagonally back through a sequence of '1's. The path must maintain a consistent diagonal direction (e.g., top-left to bottom-right, then bottom-left to top-right).

### Function Contract
**Inputs**

- `grid`: A 2D list of integers where each cell is 0, 1, or 2.

**Return value**

- An integer representing the maximum length of a valid V-shaped segment. If no such segment exists, return 0.

### Examples
**Example 1**

- Input: `grid = [[2,2,1],[1,0,1],[1,1,1]]`
- Output: `5`

**Example 2**

- Input: `grid = [[1,2,1],[0,1,0],[1,1,1]]`
- Output: `3`

**Example 3**

- Input: `grid = [[2,0,0],[0,0,0],[0,0,0]]`
- Output: `1`

---

## Underlying Base Algorithm(s)
The problem is solved using Dynamic Programming on a grid. We define four states for each cell representing the four possible diagonal directions. We compute the length of the "downward" path (from 2 to 1s) and the "upward" path (from 0 to 1s) using memoization. The V-shape is formed by connecting a downward path ending at a 0 with an upward path starting from that same 0.

---

## Complexity Analysis
- **Time Complexity**: O(M * N), where M is the number of rows and N is the number of columns, as each cell is visited a constant number of times for each of the four diagonal directions.
- **Space Complexity**: O(M * N) to store the memoization tables for the four directions.
