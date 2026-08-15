# Closest Node to Path in Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2277 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Tree, Depth-First Search, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/closest-node-to-path-in-tree/) |

## Problem Description

### Goal

You are given a tree with `n` nodes numbered from 0 through `n - 1`.
Each pair `[u, v]` in `edges` is a bidirectional connection. Because the graph
is a tree, exactly one simple path connects any two nodes.

Every query has the form `[start, end, node]`. Consider all vertices on the
unique path from `start` to `end`, including both endpoints. Find the vertex
on that path whose tree distance from `node` is smallest.

Return one selected vertex for every query in the original query order. The
closest vertex is the unique projection of `node` onto the specified tree
path.

### Function Contract

**Inputs**

- `n`: the number of nodes, with $1\le n\le1000$
- `edges`: exactly $n-1$ distinct bidirectional edges forming a tree on nodes
  0 through `n - 1`
- `query`: between 1 and 1000 triples `[start, end, node]`, whose values are
  valid node indices

Let $m=\lvert\texttt{query}\rvert$.

**Return value**

A list of length $m$ whose $i$-th value is the node on the requested
`start`-to-`end` path closest to the third node of query $i$.

### Examples

#### Example 1

- **Input:** `n = 7, edges = [[0,1],[0,2],[0,3],[1,4],[2,5],[2,6]], query = [[5,3,4],[5,3,6]]`
- **Output:** `[0,2]`

The path from 5 to 3 is `[5,2,0,3]`; nodes 0 and 2 are respectively closest
to query nodes 4 and 6.

#### Example 2

- **Input:** `n = 3, edges = [[0,1],[1,2]], query = [[0,1,2]]`
- **Output:** `[1]`

#### Example 3

- **Input:** `n = 3, edges = [[0,1],[1,2]], query = [[0,0,0]]`
- **Output:** `[0]`

The path from a node to itself contains only that node.
