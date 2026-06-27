# Grid Teleportation Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3552 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Breadth-First Search, Matrix |
| Official Link | [grid-teleportation-traversal](https://leetcode.com/problems/grid-teleportation-traversal/) |

## Problem Description & Examples
### Goal
Given a 2D grid where certain cells contain teleportation portals, determine the minimum number of steps required to travel from a starting coordinate to a target coordinate. A portal at `(r, c)` allows an instantaneous jump to any other cell `(r', c')` that shares the same portal ID. Standard movement is restricted to adjacent cells (up, down, left, right).

### Function Contract
**Inputs**

- `grid`: A 2D list of integers where `0` represents an empty path, `-1` represents an obstacle, and positive integers represent portal IDs.
- `start`: A tuple `(r, c)` representing the starting coordinates.
- `target`: A tuple `(r, c)` representing the destination coordinates.

**Return value**

- An integer representing the minimum steps to reach the target, or `-1` if the target is unreachable.

### Examples
**Example 1**

- Input: `grid = [[0, 1, 0], [0, -1, 0], [0, 1, 0]], start = (0, 0), target = (2, 2)`
- Output: `3`

**Example 2**

- Input: `grid = [[0, 0, 0], [0, -1, 0], [0, 0, 0]], start = (0, 0), target = (2, 2)`
- Output: `4`

**Example 3**

- Input: `grid = [[0, 1, 2], [0, -1, 0], [2, 1, 0]], start = (0, 0), target = (2, 2)`
- Output: `2`

---

## Underlying Base Algorithm(s)
Breadth-First Search (BFS) is used to find the shortest path in an unweighted graph. The grid is treated as a graph where nodes are cells and edges exist between adjacent cells or between cells sharing the same portal ID. To optimize, we use a hash map to group portal coordinates by their ID, ensuring we only traverse each portal network once.

---

## Complexity Analysis
- **Time Complexity**: `O(R * C)`, where `R` is the number of rows and `C` is the number of columns. Each cell is visited at most once, and each portal network is processed once.
- **Space Complexity**: `O(R * C)` to store the visited set and the portal mapping dictionary.
