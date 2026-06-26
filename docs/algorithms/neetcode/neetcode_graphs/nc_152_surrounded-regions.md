## Problem Description & Examples
### Goal
Given an `m x n` matrix `board` containing `'X'` and `'O'`, capture all regions that are 4-directionally surrounded by `'X'`.

A region is captured by flipping all `'O'`s into `'X'`s in that surrounded region.

### Function Contract
**Inputs**

- `board`: List[List[str]]

**Return value**

List[List[str]] - modified board

### Examples
**Example 1**

- Input: `board = [["X", "X"], ["X", "O"]]`
- Output: `[["X", "X"], ["X", "O"]]`

**Example 2**

- Input: `board = [['O', 'O'], ['X', 'O']]`
- Output: `[['O', 'O'], ['X', 'O']]`

**Example 3**

- Input: `board = [['X', 'X'], ['O', 'X']]`
- Output: `[['X', 'X'], ['O', 'X']]`

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
