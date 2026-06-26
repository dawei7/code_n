## Problem Description & Examples
### Goal
You are given `grid` an `row x col` grid representing a map where `1` represents land and `0` represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

Return the perimeter of the island.

### Function Contract
**Inputs**

- `grid`: List[List[int]]

**Return value**

int - perimeter of the island

### Examples
**Example 1**

- Input: `grid = [[0, 1], [1, 1]]`
- Output: `8`

**Example 2**

- Input: `grid = [[0, 0], [1, 1]]`
- Output: `6`

**Example 3**

- Input: `grid = [[1, 1], [0, 0]]`
- Output: `6`

---

## Underlying Base Algorithm(s)
- [Breadth-first search](graph_02_bfs.md)
- [Depth-first search](graph_03_dfs.md)
- [Topological sort](graph_07_topological-sort.md)
- [Union-find](graph_09_union-find.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
