# Find the Safest Path in a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2812 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Breadth-First Search, Union-Find, Heap (Priority Queue), Matrix |
| Official Link | [find-the-safest-path-in-a-grid](https://leetcode.com/problems/find-the-safest-path-in-a-grid/) |

## Problem Description & Examples
### Goal
Given an $n \times n$ grid containing some cells occupied by thieves (represented by 1) and others empty (represented by 0), find a path from the top-left corner $(0, 0)$ to the bottom-right corner $(n-1, n-1)$. The "safeness factor" of a path is defined as the minimum Manhattan distance from any cell in the path to the nearest thief. The objective is to maximize this safeness factor across all possible paths.

### Function Contract
**Inputs**

- `grid`: A list of lists of integers (size $n \times n$) where 0 represents an empty cell and 1 represents a thief.

**Return value**

- An integer representing the maximum possible safeness factor for a path from $(0, 0)$ to $(n-1, n-1)$.

### Examples
**Example 1**

- Input: `grid = [[1,0,0],[0,0,0],[0,0,1]]`
- Output: `0`

**Example 2**

- Input: `grid = [[0,0,1],[0,0,0],[0,0,0]]`
- Output: `2`

**Example 3**

- Input: `grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]`
- Output: `2`

---

## Underlying Base Algorithm(s)
1. **Multi-Source Breadth-First Search (BFS)**: Used to calculate the minimum Manhattan distance from every cell to the nearest thief.
2. **Dijkstra's Algorithm (or Max-Heap BFS)**: Used to find the path that maximizes the minimum safeness factor along the route.

---

## Complexity Analysis
- **Time Complexity**: $O(n^2 \log n)$, where $n$ is the side length of the grid. The multi-source BFS takes $O(n^2)$, and the priority queue-based pathfinding takes $O(n^2 \log n)$.
- **Space Complexity**: $O(n^2)$ to store the distance grid and the priority queue.
