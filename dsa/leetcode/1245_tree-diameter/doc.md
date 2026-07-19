# Tree Diameter

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1245 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/tree-diameter/) |

## Problem Description

### Goal

You are given `edges`, the undirected edges of a tree whose vertices are labeled with consecutive integers. A tree is connected and has no cycle, so exactly one simple path connects every pair of vertices.

Return the tree's diameter: the number of edges in its longest simple path. Either endpoint may appear anywhere in the input, and edge order has no significance. A tree consisting of one vertex has no edges and therefore has diameter zero.

### Function Contract

**Inputs**

- `edges`: A list of $n-1$ undirected pairs `[u, v]` forming one tree on $n$ vertices, with up to $10^4$ edges.

**Return value**

- The number of edges in the longest simple path between any two vertices.

### Examples

**Example 1**

- Input: `edges = [[0,1],[0,2]]`
- Output: `2`

The path from vertex `1` through `0` to `2` has two edges.

**Example 2**

- Input: `edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]`
- Output: `4`

One longest path runs from `3` through `2`, `1`, and `4` to `5`.

**Example 3**

- Input: `edges = []`
- Output: `0`

The single-vertex tree has no path edge.
