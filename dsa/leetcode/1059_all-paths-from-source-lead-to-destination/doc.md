# All Paths from Source Lead to Destination

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1059 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Graph Theory, Topological Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [all-paths-from-source-lead-to-destination](https://leetcode.com/problems/all-paths-from-source-lead-to-destination/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/all-paths-from-source-lead-to-destination/).

### Goal
Given a directed graph, determine whether every path that starts at `source` eventually ends at `destination`. A valid graph must not allow a reachable cycle, must not lead to a dead end other than `destination`, and `destination` itself must not have outgoing edges.

### Function Contract
**Inputs**

- `n`: Number of nodes labeled `0` through `n - 1`.
- `edges`: Directed edges `[from, to]`.
- `source`: Starting node.
- `destination`: Required terminal node.

**Return value**

Boolean indicating whether all paths from `source` lead to `destination`.

### Examples
**Example 1**

- Input: `n = 3, edges = [[0, 1], [0, 2]], source = 0, destination = 2`
- Output: `false`

**Example 2**

- Input: `n = 4, edges = [[0, 1], [0, 3], [1, 2], [2, 1]], source = 0, destination = 3`
- Output: `false`

**Example 3**

- Input: `n = 4, edges = [[0, 1], [0, 2], [1, 3], [2, 3]], source = 0, destination = 3`
- Output: `true`

---

## Solution
### Approach
Run DFS with three states: unvisited, visiting, and safe. A node is safe if every outgoing edge leads to another safe node. If DFS reaches a node currently in the visiting state, there is a reachable cycle, so the answer is false.

A node with no outgoing edges is valid only if it is the destination. This single rule catches dead ends and also rejects a destination that has outgoing edges.

### Complexity Analysis
- **Time Complexity**: `O(n + e)`, where `e` is the number of edges.
- **Space Complexity**: `O(n + e)` for the graph plus DFS state.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
