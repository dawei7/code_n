# Count Unreachable Pairs of Nodes in an Undirected Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2316 |
| Difficulty | Medium |
| Topics | Depth-First Search, Breadth-First Search, Union Find, Graph |
| Official Link | [LeetCode](https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/) |

## Problem Description
### Goal
An undirected graph has `n` nodes numbered from $0$ through $n-1`. Each entry
`[a, b]` in `edges` connects two different nodes in both directions. Edges are
not repeated, but the graph need not be connected: it may contain several
components and isolated nodes.

Count unordered pairs of distinct nodes for which no path connects one node to
the other. Each pair must be counted once regardless of order. Nodes within
the same connected component are reachable, whereas every choice of one node
from each of two different components contributes an unreachable pair.

### Function Contract
**Inputs**

- `n`: The number of graph nodes.
- `edges`: Distinct undirected edges `[a, b]` with $0\le a,b<n$ and $a\ne b$.

The graph has from 1 through $10^5$ nodes and at most $2\cdot10^5$ edges.

**Return value**

The number of unordered node pairs whose endpoints belong to different
connected components.

### Examples
**Example 1**

- Input: `n = 3`, `edges = [[0,1],[0,2],[1,2]]`
- Output: `0`
- Explanation: All three nodes belong to one component.

**Example 2**

- Input: `n = 7`, `edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]`
- Output: `14`
