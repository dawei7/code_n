# Path With Maximum Minimum Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1102 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Depth-First Search, Breadth-First Search, Union-Find, Heap (Priority Queue), Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [path-with-maximum-minimum-value](https://leetcode.com/problems/path-with-maximum-minimum-value/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/path-with-maximum-minimum-value/).

### Goal
Move from the top-left cell of a grid to the bottom-right cell using four-directional steps. The score of a path is the minimum value on that path. Return the maximum possible path score.

### Function Contract
**Inputs**

- `grid`: Matrix of integer cell values.

**Return value**

Largest achievable minimum cell value along any valid path.

### Examples
**Example 1**

- Input: `grid = [[5,4,5],[1,2,6],[7,4,6]]`
- Output: `4`

**Example 2**

- Input: `grid = [[2,2,1,2,2,2],[1,2,2,2,1,2]]`
- Output: `2`

**Example 3**

- Input: `grid = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]`
- Output: `3`

---

## Solution
### Approach
Use a max-heap variant of Dijkstra's algorithm. Start at `(0, 0)` with score `grid[0][0]`. Always expand the reachable cell with the highest current path score, where moving into a neighbor updates the score to `min(current_score, neighbor_value)`.

The first time the bottom-right cell is popped from the heap, its score is optimal because no remaining frontier path can have a higher minimum value.

### Complexity Analysis
- **Time Complexity**: `O(mn log(mn))` for an `m x n` grid.
- **Space Complexity**: `O(mn)` for the heap and visited state.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
