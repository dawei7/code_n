# Find if Path Exists in Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1971 |
| Difficulty | Easy |
| Topics | Depth-First Search, Breadth-First Search, Union-Find, Graph Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/find-if-path-exists-in-graph/) |

## Problem Description
### Goal
An undirected graph has `n` vertices labeled from `0` through `n - 1`.
Each pair in `edges` connects its two endpoint vertices in both directions.
No edge connects a vertex to itself, and no unordered vertex pair appears more
than once.

Given vertices `source` and `destination`, determine whether some valid path
connects them. A path may contain any number of edges, including zero edges
when the two designated vertices are the same.

### Function Contract
**Inputs**

- `n`: the number of vertices $V$, where $1 \le V \le 2\cdot10^5$.
- `edges`: a list of $E$ unique undirected edges, where
  $0 \le E \le 2\cdot10^5$ and every endpoint is a valid vertex label.
- `source`: the starting vertex.
- `destination`: the target vertex.

**Return value**

- `true` if `destination` is reachable from `source`; otherwise `false`.

### Examples
**Example 1**

- Input: `n = 3, edges = [[0, 1], [1, 2], [2, 0]], source = 0, destination = 2`
- Output: `true`

**Example 2**

- Input: `n = 6, edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source = 0, destination = 5`
- Output: `false`

**Example 3**

- Input: `n = 1, edges = [], source = 0, destination = 0`
- Output: `true`
