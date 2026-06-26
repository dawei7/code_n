# Min Cost to Connect All Points

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_167` |
| Frontend ID | 1584 |
| Difficulty | Medium |
| Topics | Array, Union-Find, Graph Theory, Minimum Spanning Tree |
| Official Link | [min-cost-to-connect-all-points](https://leetcode.com/problems/min-cost-to-connect-all-points/) |

## Problem Description & Examples
### Goal
You are given an array `points` representing the coordinates of some points on a 2D-plane, where `points[i] = [xi, yi]`.

The cost of connecting two points `[xi, yi]` and `[xj, yj]` is the Manhattan distance between them: `abs(xi - xj) + abs(yi - yj)`.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

### Function Contract
**Inputs**

- `points`: List[List[int]]

**Return value**

int - minimum connecting cost

### Examples
**Example 1**

- Input: `points = [[0, 0], [2, 2]]`
- Output: `4`

**Example 2**

- Input: `points = [[0, 0], [1, 1], [1, 0]]`
- Output: `2`

**Example 3**

- Input: `points = [[0, 0], [2, 0], [2, 2]]`
- Output: `4`

---

## Underlying Base Algorithm(s)
- [Dijkstra shortest path](graph_04_dijkstra.md)
- [Kruskal minimum spanning tree](graph_08_kruskal-s-mst.md)
- [Prim minimum spanning tree](graph_10_prim-s-mst.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
