# Largest Color Value in a Directed Graph

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/largest-color-value-in-a-directed-graph/) |
| Frontend ID | 1857 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, String, Dynamic Programming, Graph Theory, Topological Sort, Memoization, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A directed graph has nodes numbered from 0 through $n-1$. The character `colors[i]` is the lowercase English letter assigned to node `i`, and each pair `[a, b]` in `edges` creates a directed edge from `a` to `b`.

A valid path follows directed edges and may contain one or more nodes. Its color value is the greatest frequency of any single color among the nodes on that path. Return the largest color value achieved by any valid path in the graph. If the graph contains any directed cycle, including one in a disconnected component, return `-1` instead.

### Function Contract

**Inputs**

- `colors`: a lowercase string of length $n$, one color per node.
- `edges`: a list of $m$ directed pairs `[source, target]`.
- $1\le n\le10^5$ and $0\le m\le10^5$.
- Every edge endpoint lies between 0 and $n-1$.

**Return value**

- For an acyclic graph, return the maximum number of occurrences of one color along any directed path.
- Return `-1` if any directed cycle exists.

### Examples

**Example 1**

- Input: `colors = "abaca"`, `edges = [[0, 1], [0, 2], [2, 3], [3, 4]]`
- Output: `3`

Path `0 -> 2 -> 3 -> 4` contains three nodes colored `a`.

**Example 2**

- Input: `colors = "a"`, `edges = [[0, 0]]`
- Output: `-1`

**Example 3**

- Input: `colors = "abc"`, `edges = []`
- Output: `1`
