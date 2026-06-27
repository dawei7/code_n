# Find a Safe Walk Through a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3286 |
| Difficulty | Medium |
| Topics | Array, Breadth-First Search, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path |
| Official Link | [find-a-safe-walk-through-a-grid](https://leetcode.com/problems/find-a-safe-walk-through-a-grid/) |

## Problem Description & Examples
### Goal
Determine if there exists a path from the top-left cell (0, 0) to the bottom-right cell (m-1, n-1) of a grid such that the total sum of the values of the cells visited is strictly less than a given health threshold `health`. Cells containing a `1` reduce your health by 1, while cells containing a `0` do not. You can only move in the four cardinal directions.

### Function Contract
**Inputs**

- `grid`: A 2D list of integers where 0 represents a safe cell and 1 represents a hazardous cell.
- `health`: An integer representing the initial health points.

**Return value**

- A boolean: `True` if a path exists where the total health cost is less than the initial `health`, otherwise `False`.

### Examples
**Example 1**

- Input: `grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1`
- Output: `True`

**Example 2**

- Input: `grid = [[0,1,1],[1,1,1],[1,1,0]], health = 3`
- Output: `False`

**Example 3**

- Input: `grid = [[1,1,1],[1,0,1],[1,1,1]], health = 5`
- Output: `True`

---

## Underlying Base Algorithm(s)
This problem is a shortest-path problem on a weighted graph where edge weights are either 0 or 1. Dijkstra's algorithm or 0-1 Breadth-First Search (using a deque) are optimal. Since we want to minimize the total cost (sum of 1s encountered), 0-1 BFS is preferred for its O(V + E) efficiency.

---

## Complexity Analysis
- **Time Complexity**: O(m * n), where m is the number of rows and n is the number of columns, as each cell is visited at most once.
- **Space Complexity**: O(m * n) to store the distance matrix and the queue.
