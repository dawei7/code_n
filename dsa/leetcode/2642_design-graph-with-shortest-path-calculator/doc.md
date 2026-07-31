# Design Graph With Shortest Path Calculator

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2642 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Graph Theory, Design, Heap (Priority Queue), Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/design-graph-with-shortest-path-calculator/) |

## Problem Description

### Goal

Maintain a directed, weighted graph whose $n$ nodes are numbered from $0$ through $n-1$. Each edge is represented by `[from, to, cost]` and contributes its positive cost only when traversed in that direction. The graph begins with a supplied set of distinct, non-self-loop edges.

Support adding a previously absent directed edge and finding the minimum total cost of any directed path between two requested nodes. A path's cost is the sum of its edge costs. Return $-1$ when the destination is unreachable. The structure receives at most 100 additions and at most 100 shortest-path queries.

### Function Contract

**Inputs**

- `operations`: A sequence beginning with `Graph`, followed by `addEdge` and `shortestPath` calls.
- `arguments`: Constructor or method arguments aligned with `operations`. The constructor receives $1 \le n \le 100$ and the initial edges; each edge cost is between $1$ and $10^6$.

There are no duplicate edges or self-loops at any time.

**Return value**

- Return one output per operation: `null` for construction and edge additions, and the minimum path cost or $-1$ for each shortest-path query.

### Examples

**Example 1**

- Input: `operations = ["Graph", "shortestPath", "shortestPath", "addEdge", "shortestPath"]`, `arguments = [[4, [[0,2,5],[0,1,2],[1,2,1],[3,0,3]]], [3,2], [0,3], [[1,3,4]], [0,3]]`
- Output: `[null, 6, -1, null, 6]`
- Explanation: Initially, the cheapest route from 3 to 2 costs 6 and node 3 is unreachable from 0. Adding `1 -> 3` creates a route `0 -> 1 -> 3` costing 6.
