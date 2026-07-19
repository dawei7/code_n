# Reachable Nodes In Subdivided Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 882 |
| Difficulty | Hard |
| Topics | Graph Theory, Heap (Priority Queue), Shortest Path |
| Official Link | [LeetCode](https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/) |

## Problem Description
### Goal
An undirected original graph has `n` nodes labeled from `0` through `n - 1`. Each entry `[u, v, cnt]` replaces the original edge between `u` and `v` with a chain containing `cnt` new nodes and `cnt + 1` unit-length edges. When `cnt == 0`, the original endpoints remain directly adjacent.

In this subdivided graph, a node is reachable when its shortest distance from node `0` is at most `maxMoves`. Count all reachable original nodes and all reachable new subdivision nodes.

### Function Contract
**Inputs**

- `edges`: $m$ distinct undirected edges `[u, v, cnt]`, where $0 \leq m \leq \min(n(n-1)/2,10^4)$, $0 \leq u < v < n$, and $0 \leq \texttt{cnt} \leq 10^4$.
- `maxMoves`: the maximum allowed distance from node `0`, between $0$ and $10^9$.
- `n`: the number of original nodes, where $1 \leq n \leq 3000$.

**Return value**

Return the number of original and subdivided nodes whose shortest distance from node `0` is at most `maxMoves`.

### Examples
**Example 1**

- Input: `edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3`
- Output: `13`

**Example 2**

- Input: `edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], maxMoves = 10, n = 4`
- Output: `23`

**Example 3**

- Input: `edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], maxMoves = 17, n = 5`
- Output: `1`

Node `0` is disconnected, so only the starting node is reachable.
