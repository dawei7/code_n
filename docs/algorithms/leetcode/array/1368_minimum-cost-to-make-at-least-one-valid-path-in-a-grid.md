# Minimum Cost to Make at Least One Valid Path in a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1368 |
| Difficulty | Hard |
| Topics | Array, Breadth-First Search, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path |
| Official Link | [minimum-cost-to-make-at-least-one-valid-path-in-a-grid](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/) |

## Problem Description & Examples
### Goal
Each grid cell points in one of four directions. Moving in the indicated direction costs `0`; changing direction for a move costs `1`. Find the minimum total cost needed so there is at least one valid path from the top-left cell to the bottom-right cell.

### Function Contract
**Inputs**

- `grid`: an `m x n` matrix whose values encode directions: right, left, down, and up.

**Return value**

The minimum number of direction changes needed to make a path reach the destination.

### Examples
**Example 1**

- Input: `grid = [[1,1,3],[3,2,2],[1,1,4]]`
- Output: `0`

**Example 2**

- Input: `grid = [[1,1,1],[2,2,2],[1,1,1]]`
- Output: `1`

**Example 3**

- Input: `grid = [[4]]`
- Output: `0`

---

## Underlying Base Algorithm(s)
0-1 BFS on the grid graph. Edges that follow the cell arrow have weight `0`; the other three outgoing directions have weight `1`, so a deque-based shortest path search gives the minimum change count.

---

## Complexity Analysis
- **Time Complexity**: `O(mn)`
- **Space Complexity**: `O(mn)`
