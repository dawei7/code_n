# Distance to a Cycle in Undirected Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2204 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/distance-to-a-cycle-in-undirected-graph/) |

## Problem Description

### Goal

An undirected connected graph has `n` nodes numbered from `0` through `n - 1` and exactly one cycle. Each pair in `edges` represents one bidirectional edge, with no self-loops or duplicate vertex pairs.

The distance between two nodes is the minimum number of edges on a route between them. For every node, find its minimum distance to any node belonging to the unique cycle. Cycle nodes themselves have distance zero.

### Function Contract

**Inputs**

- `n`: the node count, where $3 \le n \le 10^5$.
- `edges`: exactly $n$ undirected edges forming one connected unicyclic graph.

**Return value**

Return a length-$n$ list whose entry at index $i$ is the minimum number of edges from node $i$ to any cycle node.

### Examples

**Example 1**

- Input: `n = 7`, `edges = [[1,2],[2,4],[4,3],[3,1],[0,1],[5,2],[6,5]]`
- Output: `[1,0,0,0,0,1,2]`

Nodes `1`, `2`, `3`, and `4` form the cycle; the other nodes lie on attached trees.

**Example 2**

- Input: `n = 9`, `edges = [[0,1],[1,2],[0,2],[2,6],[6,7],[6,8],[0,3],[3,4],[3,5]]`
- Output: `[0,0,0,1,2,2,1,2,2]`

The triangle on nodes `0`, `1`, and `2` is the unique cycle.
