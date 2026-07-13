# Critical Connections in a Network

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1192 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Depth-First Search, Graph Theory, Biconnected Component |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [critical-connections-in-a-network](https://leetcode.com/problems/critical-connections-in-a-network/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/critical-connections-in-a-network/).

### Goal
Given an undirected connected network, return all edges whose removal would disconnect the network. These edges are also called bridges or critical connections.

### Function Contract
**Inputs**

- `n`: Number of servers labeled `0` through `n - 1`.
- `connections`: Undirected edges between servers.

**Return value**

List of critical edges, in any order.

### Examples
**Example 1**

- Input: `n = 4`, `connections = [[0,1],[1,2],[2,0],[1,3]]`
- Output: `[[1,3]]`

**Example 2**

- Input: `n = 2`, `connections = [[0,1]]`
- Output: `[[0,1]]`

**Example 3**

- Input: `n = 3`, `connections = [[0,1],[1,2]]`
- Output: `[[0,1],[1,2]]`

---

## Solution
### Approach
Run Tarjan's bridge-finding DFS. Assign each node a discovery time and compute `low[node]`, the earliest discovery time reachable from that node through DFS tree edges plus at most one back edge.

For a DFS tree edge `node -> child`, if `low[child] > discovery[node]`, then the child subtree has no alternate connection back to `node` or an ancestor, so that edge is critical.

### Complexity Analysis
- **Time Complexity**: `O(n + e)`, where `e` is the number of connections.
- **Space Complexity**: `O(n + e)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
