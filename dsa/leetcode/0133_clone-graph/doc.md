# Clone Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 133 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Depth-First Search, Breadth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/clone-graph/) |

## Problem Description
### Goal
Given a reference to a node in a connected undirected graph, create a deep copy of the entire reachable graph. Every node has a unique value and must correspond to exactly one newly allocated clone with that same value, even when cycles or several paths lead back to it.

Preserve every neighbor relationship and its listed order in the copied structure, including self-links when present, but do not reuse any original node object. Mutating the clone must therefore have no effect on the source graph. The app contract represents the graph as a one-based adjacency list and returns independent adjacency data; the native artifact performs the equivalent operation on linked `Node` objects.

### Function Contract
**Inputs**

- `adj_list`: the app encoding of the graph, where row `i` lists the 1-based neighbors of node $i + 1$; `[]` encodes a null root

**Return value**

A structurally independent deep copy of the adjacency data. The native LeetCode artifact clones `Node` objects directly.

### Examples
**Example 1**

- Input: `adj_list = [[2,4],[1,3],[2,4],[1,3]]`
- Output: `[[2,4],[1,3],[2,4],[1,3]]`

**Example 2**

- Input: `adj_list = [[]]`
- Output: `[[]]`

**Example 3**

- Input: `adj_list = []`
- Output: `[]`
