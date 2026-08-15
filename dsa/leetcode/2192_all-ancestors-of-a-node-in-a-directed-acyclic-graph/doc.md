# All Ancestors of a Node in a Directed Acyclic Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2192 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Depth-First Search, Breadth-First Search, Graph, Topological Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/) |

## Problem Description

### Goal

A directed acyclic graph has `n` nodes numbered from $0$ through $n-1$.
Each pair `[from, to]` in `edges` is a unidirectional edge from `from` to
`to`; edges are distinct, contain no self-loops, and together cannot form a
directed cycle.

Node $u$ is an ancestor of node $v$ when some directed path leads from $u$ to
$v$. For every node, report all of its ancestors in ascending numeric order.
Nodes unreachable from every other node receive an empty ancestor list.

### Function Contract

**Inputs**

- `n`: the node count, with $1\le n\le1000$.
- `edges`: the $m$ directed edges, where
  $0\le m\le\min(2000,n(n-1)/2)$ and every endpoint lies in $[0,n-1]$.

**Return value**

Return an array `answer` of length $n$ where `answer[v]` contains every
ancestor of node $v$ exactly once, sorted in ascending order.

### Examples

#### Example 1

- **Input:** `n = 8`, `edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]`
- **Output:** `[[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]`

#### Example 2

- **Input:** `n = 5`, `edges = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]`
- **Output:** `[[],[0],[0,1],[0,1,2],[0,1,2,3]]`

#### Example 3

- **Input:** `n = 1`, `edges = []`
- **Output:** `[[]]`
