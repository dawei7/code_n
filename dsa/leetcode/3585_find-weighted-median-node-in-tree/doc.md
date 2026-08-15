# Find Weighted Median Node in Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3585 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Dynamic Programming, Bit Manipulation, Tree, Depth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-weighted-median-node-in-tree/) |

## Problem Description

### Goal

An undirected weighted tree contains `n` nodes numbered from 0 through `n - 1` and is rooted at node 0. Each entry `[a, b, w]` in `edges` connects nodes `a` and `b` with an edge of positive weight `w`.

For an ordered query `[u, v]`, walk along the unique path from `u` toward `v`. Its weighted median is the first node `x` for which the accumulated edge weight from `u` through `x` is at least half of the path's total weight. The direction matters: reversing a query can change which node is encountered first at the threshold.

Return the weighted median node for every query in the supplied order.

### Function Contract

**Inputs**

- `n`: The number of nodes, where $2\le n\le10^5$.
- `edges`: Exactly $n-1$ triples `[a, b, w]` describing a valid tree, with $0\le a,b<n$ and $1\le w\le10^9$.
- `queries`: An array of $q$ ordered node pairs `[u, v]`, where $1\le q\le10^5$ and $0\le u,v<n$.

**Return value**

Return an integer array whose $j$-th value is the first node reaching at least half of the total path weight when walking from `queries[j][0]` to `queries[j][1]`.

### Examples

#### Example 1

- **Input:** `n = 2, edges = [[0, 1, 7]], queries = [[1, 0], [0, 1]]`
- **Output:** `[0, 1]`
- **Explanation:** Either direction crosses the only edge immediately, so the destination is the median.

#### Example 2

- **Input:** `n = 3, edges = [[0, 1, 2], [2, 0, 4]], queries = [[0, 1], [2, 0], [1, 2]]`
- **Output:** `[1, 0, 2]`
- **Explanation:** For `[1, 2]`, reaching node 0 accumulates only 2 of the total weight 6; the following edge reaches node 2 and passes the halfway threshold.

#### Example 3

- **Input:** `n = 5, edges = [[0, 1, 2], [0, 2, 5], [1, 3, 1], [2, 4, 3]], queries = [[3, 4], [1, 2]]`
- **Output:** `[2, 2]`
- **Explanation:** Both directed paths first reach at least half of their total weight at node 2.

---
