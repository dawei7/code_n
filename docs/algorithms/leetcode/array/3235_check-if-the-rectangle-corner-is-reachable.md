# Check if the Rectangle Corner Is Reachable

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3235 |
| Difficulty | Hard |
| Topics | Array, Math, Depth-First Search, Breadth-First Search, Union-Find, Geometry |
| Official Link | [check-if-the-rectangle-corner-is-reachable](https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/) |

## Problem Description & Examples
### Goal
Determine if there exists a path from the bottom-left corner (0, 0) to the top-right corner (X, Y) of a rectangle without passing through any of the given circular obstacles. The path must stay within the bounds of the rectangle [0, X] x [0, Y].

### Function Contract
**Inputs**

- `X`: An integer representing the width of the rectangle.
- `Y`: An integer representing the height of the rectangle.
- `circles`: A list of lists, where each inner list `[xi, yi, ri]` represents a circle centered at `(xi, yi)` with radius `ri`.

**Return value**

- A boolean: `True` if a path exists from (0, 0) to (X, Y), `False` otherwise.

### Examples
**Example 1**

- Input: `X = 3, Y = 4, circles = [[2, 1, 1]]`
- Output: `True`

**Example 2**

- Input: `X = 3, Y = 3, circles = [[1, 1, 2]]`
- Output: `False`

**Example 3**

- Input: `X = 3, Y = 3, circles = [[2, 1, 1], [1, 2, 1]]`
- Output: `False`

---

## Underlying Base Algorithm(s)
The problem is equivalent to checking if the circular obstacles form a "chain" that blocks the path from the bottom-left to the top-right. A path is blocked if there is a sequence of overlapping circles that connects the left/top boundary of the rectangle to the right/bottom boundary. This can be solved using Disjoint Set Union (DSU) or Graph Traversal (DFS/BFS) to identify connected components of circles and their intersections with the rectangle boundaries.

---

## Complexity Analysis
- **Time Complexity**: O(N^2), where N is the number of circles, due to checking intersections between every pair of circles.
- **Space Complexity**: O(N) to store the DSU structure or the adjacency list for graph traversal.
