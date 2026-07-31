# Minimum Edge Reversals So Every Node Is Reachable

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2858 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Dynamic Programming, Depth-First Search, Breadth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/) |

## Problem Description

### Goal

A simple directed graph contains `n` nodes labeled from `0` through `n - 1`. If every edge were treated as bidirectional, the graph would be a tree. Each row `edges[i] = [u_i, v_i]` gives a directed edge from `u_i` to `v_i`.

One edge reversal changes an edge `u -> v` into `v -> u`. For each possible starting node `i`, independently determine the minimum number of reversals needed so that every other node is reachable from `i` by following directed edges.

Return an array `answer` with one result per starting node. Reversals chosen for one `answer[i]` do not carry over to any other starting node's calculation.

### Function Contract

**Inputs**

- `n`: The number of nodes.
- `edges`: Exactly `n - 1` directed edges `[u, v]` whose undirected form is a tree.

The constraints guarantee $2 \le n \le 10^5$, $0 \le u,v < n$, and $u \ne v$.

**Return value**

An integer array of length `n`, where `answer[i]` is the minimum number of edge reversals that makes every node reachable from `i`.

### Examples

**Example 1**

- Input: `n = 4, edges = [[2, 0], [2, 1], [1, 3]]`
- Output: `[1, 1, 0, 2]`

Node `2` already reaches the whole tree, while starting at node `3` requires reversing two edges on the route outward.

**Example 2**

- Input: `n = 3, edges = [[1, 2], [2, 0]]`
- Output: `[2, 0, 1]`

The original directions form a path outward from node `1`.

**Example 3**

- Input: `n = 5, edges = [[0, 1], [0, 2], [0, 3], [0, 4]]`
- Output: `[0, 1, 1, 1, 1]`

The center reaches every leaf already; a leaf needs only its incident edge reversed to reach the center and then all other leaves.
