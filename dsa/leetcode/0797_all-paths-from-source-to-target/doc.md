# All Paths From Source to Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 797 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Backtracking, Depth-First Search, Breadth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/all-paths-from-source-to-target/) |

## Problem Description

### Goal

Given a directed acyclic graph as an adjacency list, nodes are numbered from `0` through $n - 1$, and `graph[i]` lists every node reachable by one outgoing edge from `i`.

Return every directed path from source node `0` to target node $n - 1$, with each path represented by its complete sequence of node numbers including both endpoints. Paths may be returned in any order, and the acyclic guarantee prevents a path from looping indefinitely.

### Function Contract

**Inputs**

- `graph`: an adjacency list in which `graph[i]` contains every node reachable by one outgoing edge from node `i`.

**Return value**

- A list of all source-to-target paths, with each path represented by its sequence of node numbers. The paths may be returned in any order.

### Examples

**Example 1**

- Input: `graph = [[1,2],[3],[3],[]]`
- Output: `[[0,1,3],[0,2,3]]`
- Explanation: The source has two branches, and each reaches the target.

**Example 2**

- Input: `graph = [[1],[]]`
- Output: `[[0,1]]`
- Explanation: The only edge is also the only complete path.

**Example 3**

- Input: `graph = [[4,3,1],[3,2,4],[3],[4],[]]`
- Output: `[[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]`
- Explanation: A path may go directly to node `4` or follow any directed branch that eventually reaches it.
