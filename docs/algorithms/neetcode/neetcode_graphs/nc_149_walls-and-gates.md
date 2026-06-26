## Problem Description & Examples
### Goal
You are given an `m x n` grid `rooms` initialized with three possible values:
- `-1`: A wall or an obstacle.
- `0`: A gate.
- `2147483647` (INF): An empty room.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with `INF`.

### Function Contract
**Inputs**

- `rooms`: List[List[int]]

**Return value**

List[List[int]] - grid with shortest distances filled

### Examples
**Example 1**

- Input: `rooms = [[2147483647, -1, 0]]`
- Output: `[[2, -1, 0]]`

**Example 2**

- Input: `rooms = [[-1, -1], [2147483647, 2147483647]]`
- Output: `[[-1, -1], [2147483647, 2147483647]]`

**Example 3**

- Input: `rooms = [[2147483647, 0], [2147483647, 2147483647]]`
- Output: `[[1, 0], [2, 1]]`

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
