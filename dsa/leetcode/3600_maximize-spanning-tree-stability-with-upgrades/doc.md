# Maximize Spanning Tree Stability with Upgrades

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3600 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Binary Search, Greedy, Union-Find, Graph Theory, Minimum Spanning Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/) |

## Problem Description

### Goal

An undirected graph has `n` vertices numbered from `0` through `n - 1`. Each entry `edges[i] = [u_i, v_i, s_i, must_i]` describes an edge between `u_i` and `v_i` with strength `s_i`. When `must_i` is `1`, that edge is mandatory: every valid spanning tree must contain it, and it cannot be upgraded. When `must_i` is `0`, the edge is optional.

You may upgrade at most `k` optional edges that are selected for the tree. An edge can be upgraded no more than once, and doing so doubles its strength. The stability of a spanning tree is the minimum effective strength among all of its selected edges after the upgrades.

Choose a spanning tree and its upgrades so that this minimum is as large as possible. Return the resulting maximum stability. If the mandatory edges already contain a cycle, or if no spanning tree can include all of them, return `-1`.

### Function Contract

**Inputs**

- `n`: the number of graph vertices, labeled from `0` through `n - 1`
- `edges`: the undirected edges, each represented as `[u, v, strength, must]`
- `k`: the maximum number of selected optional edges that may be upgraded

The graph has at most $10^5$ vertices and at most $10^5$ edges. Every strength is between $1$ and $10^5$. The flag `must` is either `0` or `1`, and $0 \le k \le n$.

**Return value**

The greatest possible minimum effective edge strength among valid spanning trees, or `-1` when no valid spanning tree exists.

### Examples

#### Example 1

- **Input:** `n = 3, edges = [[0,1,2,1],[1,2,3,0]], k = 1`
- **Output:** `2`

Both edges are required to connect the graph. Upgrading the optional edge changes its strength from `3` to `6`, but the mandatory edge still limits stability to `2`.

#### Example 2

- **Input:** `n = 3, edges = [[0,1,4,0],[1,2,3,0],[0,2,1,0]], k = 2`
- **Output:** `6`

Select the edges of strengths `4` and `3`, then upgrade both. Their effective strengths become `8` and `6`.

#### Example 3

- **Input:** `n = 3, edges = [[0,1,1,1],[1,2,1,1],[2,0,1,1]], k = 0`
- **Output:** `-1`

The three mandatory edges form a cycle, so no spanning tree can contain all of them.
