## Problem Description & Examples
### Goal
Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

### Function Contract
**Inputs**

- `grid`: List[List[str]]

**Return value**

int - count of islands

### Examples
**Example 1**

- Input: `grid = [["1", "0"], ["0", "1"]]`
- Output: `2`

**Example 2**

- Input: `grid = [['1', '1'], ['0', '1']]`
- Output: `1`

**Example 3**

- Input: `grid = [['0', '0'], ['1', '0']]`
- Output: `1`

---

## Underlying Base Algorithm(s)
- [Breadth-first search](graph_02_bfs.md)
- [Depth-first search](graph_03_dfs.md)
- [Topological sort](graph_07_topological-sort.md)
- [Union-find](graph_09_union-find.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
