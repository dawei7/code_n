# Swim in Rising Water

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 778 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Depth-First Search, Breadth-First Search, Union-Find, Heap (Priority Queue), Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/swim-in-rising-water/) |

## Problem Description

### Goal

An $n \times n$ grid gives the elevation of every square, and rain raises the water level to `t` at time `t`. A square can be occupied once its elevation is at most the current water level, and movement is allowed only between horizontally or vertically adjacent swimmable squares.

Starting at `(0, 0)`, return the minimum time at which $(n - 1, n - 1)$ can be reached. Equivalently, minimize the highest elevation encountered along a valid path; path length itself does not affect the time.

### Function Contract

**Inputs**

- `grid`: a nonempty $n \times n$ matrix whose distinct elevations are the integers from `0` through $n^{2} - 1$.

**Return value**

- The minimum possible value of the highest elevation encountered on a path from `(0, 0)` to $(n - 1, n - 1)$.

### Examples

**Example 1**

- Input: `grid = [[0,2],[1,3]]`
- Output: `3`
- Explanation: The destination itself has elevation `3`, so no earlier arrival is possible.

**Example 2**

- Input: `grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]`
- Output: `16`
- Explanation: The low-elevation route winds around the grid and reaches the destination once elevation `16` is available.

**Example 3**

- Input: `grid = [[0]]`
- Output: `0`
- Explanation: The start is already the destination.
