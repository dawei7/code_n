## Problem Description & Examples
### Goal
You are a hiker preparing for an upcoming hike. You are given `heights`, a 2D array of size `rows x columns`, where `heights[row][col]` represents the height of cell `(row, col)`. You are situated in the top-left cell, `(0, 0)`, and you hope to travel to the bottom-right cell, `(rows-1, columns-1)` (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from `(0, 0)` to `(rows-1, columns-1)`.

### Function Contract
**Inputs**

- `heights`: List[List[int]]

**Return value**

int - minimum effort

### Examples
**Example 1**

- Input: `heights = [[1, 2], [3, 4]]`
- Output: `1`

**Example 2**

- Input: `heights = [[50, 98], [54, 6]]`
- Output: `48`

**Example 3**

- Input: `heights = [[18, 73], [98, 9]]`
- Output: `64`

---

## Underlying Base Algorithm(s)
- [Dijkstra shortest path](graph_04_dijkstra.md)
- [Kruskal minimum spanning tree](graph_08_kruskal-s-mst.md)
- [Prim minimum spanning tree](graph_10_prim-s-mst.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
