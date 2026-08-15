# Maximum Weighted K-Edge Path

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3543 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Dynamic Programming, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-weighted-k-edge-path/) |

## Problem Description

### Goal

Consider a directed acyclic graph with `n` nodes numbered from `0` through `n - 1`. Each entry `[u, v, w]` in `edges` is a directed edge from `u` to `v` with positive weight `w`. The graph contains no duplicate edges.

Among every directed path containing exactly `k` edges, find the greatest total edge weight that is strictly less than `t`. A path may begin at any node. Return `-1` when no path satisfies both the exact edge-count requirement and the strict weight bound.

### Function Contract

**Inputs**

- `n`: The number of graph nodes.
- `edges`: A list of directed weighted edges `[u, v, w]`.
- `k`: The exact number of edges the selected path must contain.
- `t`: An exclusive upper bound on the path's total weight.

The constraints are $1 \le n \le 300$, $0 \le \lvert\texttt{edges}\rvert \le 300$, $0 \le k \le 300$, and $1 \le t \le 600$. Every edge weight is between $1$ and $10$, both endpoints are valid and distinct, and the input graph is a DAG.

**Return value**

Return the maximum total weight below `t` among paths with exactly `k` edges, or `-1` if no such path exists.

### Examples

#### Example 1

- **Input:** `n = 3, edges = [[0, 1, 1], [1, 2, 2]], k = 2, t = 4`
- **Output:** `3`
- **Explanation:** The only two-edge path has total weight $1 + 2 = 3$, which is below `t`.

#### Example 2

- **Input:** `n = 3, edges = [[0, 1, 2], [0, 2, 3]], k = 1, t = 3`
- **Output:** `2`
- **Explanation:** Weight $3$ equals the exclusive bound, leaving weight $2$ as the best valid choice.

#### Example 3

- **Input:** `n = 3, edges = [[0, 1, 6], [1, 2, 8]], k = 1, t = 6`
- **Output:** `-1`
- **Explanation:** Neither one-edge path has total weight strictly below `6`.

---
