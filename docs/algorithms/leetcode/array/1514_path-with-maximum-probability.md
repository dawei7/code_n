# Path with Maximum Probability

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1514 |
| Difficulty | Medium |
| Topics | Array, Graph Theory, Heap (Priority Queue), Shortest Path |
| Official Link | [path-with-maximum-probability](https://leetcode.com/problems/path-with-maximum-probability/) |

## Problem Description & Examples
### Goal
In an undirected graph whose edges have success probabilities, find the path
from `start` to `end` with the largest product of edge probabilities.

### Function Contract
**Inputs**

- `n`: the number of nodes labeled from `0` to `n - 1`.
- `edges`: undirected edges.
- `succProb`: success probability for each corresponding edge.
- `start`: the starting node.
- `end`: the destination node.

**Return value**

The maximum success probability, or `0.0` if no path exists.

### Examples
**Example 1**

- Input: `n = 3, edges = [[0, 1], [1, 2], [0, 2]], succProb = [0.5, 0.5, 0.2], start = 0, end = 2`
- Output: `0.25`

**Example 2**

- Input: `n = 3, edges = [[0, 1], [1, 2], [0, 2]], succProb = [0.5, 0.5, 0.3], start = 0, end = 2`
- Output: `0.3`

**Example 3**

- Input: `n = 3, edges = [[0, 1]], succProb = [0.5], start = 0, end = 2`
- Output: `0.0`

---

## Underlying Base Algorithm(s)
Build an adjacency list and run a Dijkstra-style search with a max-heap ordered
by current path probability. When visiting an edge, multiply the current
probability by the edge probability and relax the neighbor if that product is
better than its best known value.

---

## Complexity Analysis
- **Time Complexity**: `O((n + e) log n)`, where `e` is the number of edges.
- **Space Complexity**: `O(n + e)`.
