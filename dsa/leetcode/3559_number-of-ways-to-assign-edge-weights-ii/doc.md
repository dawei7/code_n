# Number of Ways to Assign Edge Weights II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3559 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Bit Manipulation, Tree, Depth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/) |

## Problem Description

### Goal

An undirected tree contains nodes labeled from `1` through `n` and is rooted at node `1`. The array `edges` contains its `n - 1` connections. Each edge on a queried path may independently receive weight `1` or `2`.

For every query `[u, v]`, consider only the edges on the unique path between `u` and `v`; all other tree edges are ignored. Count how many weight assignments make the sum along that path odd. Queries are evaluated independently, so an assignment for one query has no effect on another.

Return all counts in query order, applying modulo $10^9+7$ to every value. When `u == v`, the path has no edges and its cost is zero, so its answer is zero.

### Function Contract

**Inputs**

- `edges`: The `n - 1` undirected edges `[u, v]` of a valid tree on nodes `1` through `n`.
- `queries`: An array of node pairs `[u, v]` whose unique tree paths are evaluated independently.

The constraints are $2 \le n \le 10^5$, $1 \le \lvert\texttt{queries}\rvert \le 10^5$, and every edge and query endpoint is a valid node label.

**Return value**

Return an integer array whose value for query `[u, v]` is the number of assignments of weights `1` and `2` to that path's edges that produce an odd sum, modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `edges = [[1,2]], queries = [[1,1],[1,2]]`
- **Output:** `[0,1]`
- **Explanation:** The empty path has even cost zero. On the one-edge path, only weight `1` gives an odd cost.

#### Example 2

- **Input:** `edges = [[1,2],[1,3],[3,4],[3,5]], queries = [[1,4],[3,4],[2,5]]`
- **Output:** `[2,1,4]`
- **Explanation:** The path lengths are two, one, and three. Exactly half of the assignments on each nonempty path have odd total weight.

---
