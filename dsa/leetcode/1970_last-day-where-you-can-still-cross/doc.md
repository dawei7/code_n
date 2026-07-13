# Last Day Where You Can Still Cross

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1970 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [last-day-where-you-can-still-cross](https://leetcode.com/problems/last-day-where-you-can-still-cross/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/last-day-where-you-can-still-cross/).

### Goal
Cells in a grid flood one per day. Find the latest day when there is still a path of dry cells from the top row to the bottom row.

### Function Contract
**Inputs**

- `row`: number of rows.
- `col`: number of columns.
- `cells`: flooding order using 1-based coordinates.

**Return value**

Return the last day index on which crossing is possible.

### Examples
**Example 1**

- Input: `row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]`
- Output: `2`

**Example 2**

- Input: `row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]`
- Output: `1`

**Example 3**

- Input: `row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]`
- Output: `3`

---

## Solution
### Approach
Binary search the day. For a candidate day, mark the first `day` flooded cells and run BFS/DFS from all dry top-row cells to see whether any bottom-row cell is reachable. A reverse-time union-find solution is also common.

### Complexity Analysis
- **Time Complexity**: `O(row * col * log(row * col))` with binary search and BFS.
- **Space Complexity**: `O(row * col)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
