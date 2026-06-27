# Path Existence Queries in a Graph II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3534 |
| Difficulty | Hard |
| Topics | Array, Two Pointers, Binary Search, Dynamic Programming, Greedy, Bit Manipulation, Graph Theory, Sorting |
| Official Link | [path-existence-queries-in-a-graph-ii](https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/) |

## Problem Description & Examples
### Goal
Given a directed graph with $n$ nodes and a set of weighted edges, determine if there exists a path between two nodes $u$ and $v$ such that the bitwise AND of all edge weights along the path equals a specific target value. You are provided with multiple queries, each specifying a start node, an end node, and a target bitwise AND value.

### Function Contract
**Inputs**

- `n`: An integer representing the number of nodes.
- `edges`: A list of lists, where each inner list `[u, v, w]` represents a directed edge from `u` to `v` with weight `w`.
- `queries`: A list of lists, where each inner list `[start, end, target]` represents a query.

**Return value**

- A list of booleans where the $i$-th element is `True` if a path exists for the $i$-th query satisfying the bitwise AND condition, and `False` otherwise.

### Examples
**Example 1**

- Input: `n = 3, edges = [[0, 1, 7], [1, 2, 3]], queries = [[0, 2, 3]]`
- Output: `[True]`

**Example 2**

- Input: `n = 3, edges = [[0, 1, 7], [1, 2, 3]], queries = [[0, 2, 7]]`
- Output: `[False]`

**Example 3**

- Input: `n = 4, edges = [[0, 1, 15], [1, 2, 7], [0, 2, 7]], queries = [[0, 2, 7]]`
- Output: `[True]`

---

## Underlying Base Algorithm(s)
The problem is solved using a combination of **Bitwise Property Analysis** and **Graph Reachability**. Since the bitwise AND operation is monotonic (adding an edge can only decrease or keep the AND value the same), we can precompute reachable bitwise AND values for each node. We use a set of reachable AND values for each node and propagate them using a modified BFS or Dijkstra-like approach, or by iterating through bits to determine reachability.

## Complexity Analysis
- **Time Complexity**: $O(Q + E \cdot \log(\max(W)))$, where $Q$ is the number of queries, $E$ is the number of edges, and $W$ is the maximum edge weight.
- **Space Complexity**: $O(N \cdot \log(\max(W)) + E)$, where $N$ is the number of nodes, to store the reachable AND values for each node.
