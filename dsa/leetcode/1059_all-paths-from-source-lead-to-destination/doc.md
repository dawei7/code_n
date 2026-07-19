# All Paths from Source Lead to Destination

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1059 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Graph Theory, Topological Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/all-paths-from-source-lead-to-destination/) |

## Problem Description

### Goal

An array `edges` describes a directed graph: each pair `[a, b]` is an edge from node `a` to node `b`. Given nodes `source` and `destination`, decide whether all paths beginning at `source` eventually end at `destination`.

This condition requires at least one path from `source` to `destination`. Every terminal node reachable from `source` must be `destination`, and the number of possible paths from `source` to `destination` must be finite. Thus, a reachable dead end other than `destination` or a reachable cycle makes the answer false. Return true if and only if all paths satisfy these requirements.

### Function Contract

**Inputs**

- `n`: the number of nodes, labeled from `0` through `n - 1`, where $1 \le n \le 10^4$.
- `edges`: at most $10^4$ directed pairs `[a, b]`; self-loops and parallel edges are allowed.
- `source`: the node at which every considered path starts.
- `destination`: the node at which every path must terminate.
- Let $V=n$ and let $E$ be the number of edges.

**Return value**

- `true` exactly when every path from `source` eventually ends at `destination`; otherwise `false`.

### Examples

**Example 1**

- Input: `n = 3, edges = [[0, 1], [0, 2]], source = 0, destination = 2`
- Output: `false`
- Explanation: Node 1 is a reachable terminal node different from the destination.

**Example 2**

- Input: `n = 4, edges = [[0, 1], [0, 3], [1, 2], [2, 1]], source = 0, destination = 3`
- Output: `false`
- Explanation: One route reaches node 3, but another can loop forever between nodes 1 and 2.

**Example 3**

- Input: `n = 4, edges = [[0, 1], [0, 2], [1, 3], [2, 3]], source = 0, destination = 3`
- Output: `true`
