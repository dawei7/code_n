# Count Sub Islands

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1905 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-sub-islands](https://leetcode.com/problems/count-sub-islands/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-sub-islands/).

### Goal
An island in `grid2` is a sub-island if every one of its land cells is also land in `grid1`. Count sub-islands in `grid2`.

### Function Contract
**Inputs**

- `grid1`: the reference land-water grid.
- `grid2`: the grid whose islands are checked.

**Return value**

Return the number of islands in `grid2` fully contained in land cells of `grid1`.

### Examples
**Example 1**

- Input: `grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]`
- Output: `3`

**Example 2**

- Input: `grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]`
- Output: `2`

**Example 3**

- Input: `grid1 = [[1]], grid2 = [[1]]`
- Output: `1`

---

## Solution
### Approach
Run DFS or BFS over each unvisited land component in `grid2`. While traversing the component, track whether every visited cell is land in `grid1`. Count the component only if that flag remains true.

### Complexity Analysis
- **Time Complexity**: `O(m * n)`
- **Space Complexity**: `O(m * n)` worst case recursion or queue

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
