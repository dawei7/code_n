## Problem Description & Examples
### Goal
You are given an `n x n` integer matrix `grid` where each value `grid[i][j]` represents the elevation at that point `(i, j)`.

Rain starts to fall. At time `t`, the depth of the water everywhere is `t`. You can swim from a square to another 4-directionally adjacent square if and only if both elevations are at most `t`. You can swim infinite distances zero time. Of course, you must start at the top left square `(0, 0)` at time `0`.

Return the least time until you can reach the bottom right square `(n-1, n-1)`.

### Function Contract
**Inputs**

- `grid`: List[List[int]]

**Return value**

int - minimum time

### Examples
**Example 1**

- Input: `grid = [[0, 2], [1, 3]]`
- Output: `3`

**Example 2**

- Input: `grid = [[2, 0], [1, 3]]`
- Output: `3`

**Example 3**

- Input: `grid = [[3, 0], [2, 1]]`
- Output: `3`

---

## Underlying Base Algorithm(s)
- [Dijkstra shortest path](graph_04_dijkstra.md)
- [Kruskal minimum spanning tree](graph_08_kruskal-s-mst.md)
- [Prim minimum spanning tree](graph_10_prim-s-mst.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
