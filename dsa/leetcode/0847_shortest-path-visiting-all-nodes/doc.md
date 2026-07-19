# Shortest Path Visiting All Nodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 847 |
| Difficulty | Hard |
| Topics | Dynamic Programming, Bit Manipulation, Breadth-First Search, Graph Theory, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) |

## Problem Description
### Goal
You are given a connected, undirected graph with $n$ nodes labeled from $0$ through $n-1$. The adjacency list `graph[i]` contains every node joined to node `i` by an edge. It contains no self-loop, and every undirected edge is represented in both endpoints' lists.

Find the minimum number of edges in a path that visits every node at least once. The path may begin and end at any nodes, may revisit a node any number of times, and may traverse the same edge more than once; only its total edge count is minimized.

### Function Contract
**Inputs**

- `graph`: the adjacency list of a connected undirected graph with $n$ nodes, where $1 \leq n \leq 12$, `graph[i]` excludes `i`, and $0 \leq \lvert\texttt{graph[i]}\rvert < n$.

**Return value**

Return the length, measured in traversed edges, of the shortest path that visits all $n$ nodes.

### Examples
**Example 1**

- Input: `graph = [[1,2,3],[0],[0],[0]]`
- Output: `4`

One shortest path is `[1,0,2,0,3]`; revisiting the center is necessary.

**Example 2**

- Input: `graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]`
- Output: `4`

The path `[0,1,4,2,3]` visits every node in four edge traversals.

**Example 3**

- Input: `graph = [[]]`
- Output: `0`

The only node is already visited when the path starts.
