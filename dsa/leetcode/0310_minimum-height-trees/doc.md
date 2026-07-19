# Minimum Height Trees

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 310 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-height-trees/) |

## Problem Description
### Goal
Given an undirected tree with `n` labeled nodes and $n - 1$ edges, choose any node as its root. The resulting height is the maximum number of edges on a downward route from that root to any other node.

Return every root label that produces the minimum possible height, in any order. A tree has one or two such central nodes; include both when they tie. Re-rooting does not change the undirected edges, only parent-child orientation and measured depth. For a one-node tree, return its sole label. The task returns centers rather than the minimum height itself.

### Function Contract
**Inputs**

- `n`: the number of nodes labelled `0` through $n - 1$
- `edges`: the tree's $n - 1$ undirected edges

**Return value**

The one or two minimum-height root labels, in any order.

### Examples
**Example 1**

- Input: `n = 4, edges = [[1,0],[1,2],[1,3]]`
- Output: `[1]`

**Example 2**

- Input: `n = 6, edges = [[0,3],[1,3],[2,3],[4,3],[5,4]]`
- Output: `[3,4]`

**Example 3**

- Input: `n = 1, edges = []`
- Output: `[0]`
