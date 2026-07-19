# Find Eventual Safe States

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 802 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-eventual-safe-states/) |

## Problem Description

### Goal

A directed graph has nodes labeled `0` through $n - 1$. A terminal node has no outgoing edges, and a node is eventually safe when every possible path starting from it ultimately reaches a terminal node or another safe node rather than continuing around a cycle forever.

Return all safe node labels sorted in ascending order. The requirement covers every possible outgoing choice, so a node is unsafe if even one reachable path can enter a directed cycle, regardless of whether another path reaches a terminal node.

### Function Contract

**Inputs**

- `graph`: a directed graph represented by adjacency lists, where `graph[i]` contains every destination of an edge leaving node `i`.

**Return value**

- All eventual safe node numbers in increasing order.

### Examples

**Example 1**

- Input: `graph = [[1,2],[2,3],[5],[0],[5],[],[]]`
- Output: `[2,4,5,6]`
- Explanation: Nodes `0`, `1`, and `3` can enter a cycle; every route from the other nodes terminates.

**Example 2**

- Input: `graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]`
- Output: `[4]`
- Explanation: Node `4` is terminal, while each other node is in or can reach a cycle.

**Example 3**

- Input: `graph = [[],[],[]]`
- Output: `[0,1,2]`
- Explanation: Every node is already terminal and therefore safe.
