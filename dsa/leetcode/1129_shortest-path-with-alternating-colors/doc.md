# Shortest Path with Alternating Colors

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1129 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Breadth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [shortest-path-with-alternating-colors](https://leetcode.com/problems/shortest-path-with-alternating-colors/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/shortest-path-with-alternating-colors/).

### Goal
In a directed graph with red and blue edges, find the shortest path length from node `0` to every node such that consecutive edges in the path alternate colors. Return `-1` for unreachable nodes.

### Function Contract
**Inputs**

- `n`: Number of nodes labeled `0` through `n - 1`.
- `redEdges`: Directed red edges.
- `blueEdges`: Directed blue edges.

**Return value**

List where index `i` is the shortest alternating path length from `0` to `i`, or `-1`.

### Examples
**Example 1**

- Input: `n = 3, redEdges = [[0, 1], [1, 2]], blueEdges = []`
- Output: `[0, 1, -1]`

**Example 2**

- Input: `n = 3, redEdges = [[0, 1]], blueEdges = [[1, 2]]`
- Output: `[0, 1, 2]`

**Example 3**

- Input: `n = 3, redEdges = [[0, 1]], blueEdges = [[2, 1]]`
- Output: `[0, 1, -1]`

---

## Solution
### Approach
Run BFS over states `(node, last_edge_color)`, not just nodes. From a state, only traverse edges of the opposite color. Start with two states at node `0`, one pretending the previous edge was red and one pretending it was blue, so either color may be used first.

The first time a node is reached at any color state gives its shortest alternating distance.

### Complexity Analysis
- **Time Complexity**: `O(n + r + b)`, where `r` and `b` are red and blue edge counts.
- **Space Complexity**: `O(n + r + b)` for adjacency lists, visited states, and BFS queue.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
