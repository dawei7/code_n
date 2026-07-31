# Longest Cycle in a Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2360 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Depth-First Search, Graph, Topological Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-cycle-in-a-graph/) |

## Problem Description

### Goal

A directed graph has $n$ nodes numbered from 0 through $n-1$, with at most one
outgoing edge from each node. In the array `edges`, a non-negative `edges[i]`
is the destination of the edge leaving $i$, while `-1` indicates that $i$ has
no outgoing edge.

Find the largest number of nodes in any directed cycle. A cycle follows
directed edges and eventually returns to its starting node. Return `-1` if the
graph contains no cycle.

### Function Contract

**Inputs**

- `edges`: A length-$n$ list encoding each node's optional outgoing edge.

The constraints are $2 \le n \le 10^5$,
$-1 \le \texttt{edges[i]} < n$, and `edges[i] != i`.

**Return value**

Return the length of the longest directed cycle, or `-1` when no cycle exists.

### Examples

**Example 1**

- Input: `edges = [3,3,4,2,3]`
- Output: `3`

Nodes 2, 4, and 3 form a directed cycle of length 3.

**Example 2**

- Input: `edges = [2,-1,3,1]`
- Output: `-1`

Every forward path terminates, so the graph has no cycle.
