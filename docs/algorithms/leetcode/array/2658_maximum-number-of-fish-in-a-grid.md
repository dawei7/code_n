# Maximum Number of Fish in a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2658 |
| Difficulty | Medium |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Official Link | [maximum-number-of-fish-in-a-grid](https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/) |

## Problem Description & Examples
### Goal
Given a 2D grid representing a map, where each cell `grid[r][c]` contains an integer. A value of `0` indicates a land cell, while any positive integer `x` indicates a water cell containing `x` fish. Fish can only be caught from water cells. Two water cells are considered connected if they are horizontally or vertically adjacent. The objective is to find the maximum total number of fish that can be collected from any single connected component of water cells. If no fish are present in the grid, the result should be 0.

### Function Contract
**Inputs**

- `grid`: `List[List[int]]` - A 2D list of integers representing the map. `grid[r][c]` is the number of fish in cell `(r, c)`, or 0 if it's land.
  - `1 <= grid.length, grid[i].length <= 100`
  - `0 <= grid[i][j] <= 100`

**Return value**

- `int` - The maximum total number of fish found in any single connected component of water cells.

### Examples
**Example 1**

- Input: `[[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]`
- Output: `7`
  - Explanation: There are several connected components of fish.
    - (0,1)=2, (0,2)=1 -> Sum = 3
    - (1,0)=4 -> Sum = 4
    - (1,3)=3, (2,3)=4 -> Sum = 7 (This is the maximum)
    - (2,0)=1 -> Sum = 1
    - (3,1)=3, (3,2)=2 -> Sum = 5

**Example 2**

- Input: `[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]`
- Output: `16`
  - Explanation: All cells are water cells with 1 fish, forming one large connected component. The total fish is 4 * 4 * 1 = 16.

**Example 3**

- Input: `[[0,0,0],[0,0,0],[0,0,0]]`
- Output: `0`
  - Explanation: The grid contains only land cells (0 fish), so no fish can be caught.

---

## Underlying Base Algorithm(s)
The problem can be solved using graph traversal algorithms to identify and sum values within connected components.
1.  **Depth-First Search (DFS):** Iterate through each cell of the grid. If a cell contains fish and has not been visited, initiate a DFS traversal from that cell. The DFS will explore all connected water cells, summing their fish counts, and marking them as visited. The sum for each component is then compared to a running maximum.
2.  **Breadth-First Search (BFS):** Similar to DFS, iterate through the grid. When an unvisited water cell is found, start a BFS. The BFS will use a queue to explore all connected water cells level by level, summing their fish counts, and marking them as visited. The sum for each component is then compared to a running maximum.

Both DFS and BFS are suitable for this problem. DFS is often simpler to implement recursively, while BFS is iterative and can be preferred to avoid deep recursion limits.

---

## Complexity Analysis
- **Time Complexity**: `O(M * N)`
  - Where `M` is the number of rows and `N` is the number of columns in the grid.
  - Each cell in the grid is visited at most a constant number of times (once by the outer loop, and once by the DFS/BFS traversal). Marking cells as visited prevents redundant processing.
- **Space Complexity**: `O(M * N)`
  - This is primarily due to the `visited` set (or 2D array) which stores the state for each cell.
  - In the case of DFS, the recursion stack can go up to `O(M * N)` in the worst-case scenario (e.g., a grid entirely filled with water, forming a single long path).
  - In the case of BFS, the queue can hold up to `O(M * N)` elements in the worst-case (e.g., a grid entirely filled with water, where all cells are added to the queue before being processed).
