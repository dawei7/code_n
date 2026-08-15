# Shortest Path in a Weighted Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3515 |
| Difficulty | Hard |
| Topics | Array, Tree, Depth-First Search, Binary Indexed Tree, Segment Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-path-in-a-weighted-tree/) |

## Problem Description

### Goal

You are given an undirected weighted tree with $n$ nodes numbered from $1$ through $n$ and rooted at node $1$. Each entry `[u, v, w]` in `edges` describes one tree edge between `u` and `v` whose initial weight is `w`.

Process `queries` in order. An update `[1, u, v, w]` replaces the current weight of the existing edge between `u` and `v` with `w`; later queries observe that replacement. A request `[2, x]` asks for the current shortest-path distance from root `1` to node `x`. Because the graph remains a tree, that distance is the sum of the current weights on the unique root-to-`x` path.

Return the requested distances in their original order. Update queries do not add entries to the returned list.

### Function Contract

**Inputs**

- `n`: The number of nodes, where $1 \le n \le 10^5$.
- `edges`: The $n-1$ undirected tree edges `[u, v, w]`, with endpoints from $1$ through $n$ and $1 \le w \le 10^4$.
- `queries`: A list of $q$ operations, where $1 \le q \le 10^5$. Each operation is either `[1, u, v, w]` for a guaranteed existing edge and a replacement weight $1 \le w \le 10^4$, or `[2, x]` for a root-distance request.

**Return value**

Return one integer for every type-2 query: the current distance from node `1` to its requested node.

### Examples

#### Example 1

- **Input:** `n = 2, edges = [[1, 2, 7]], queries = [[2, 2], [1, 1, 2, 4], [2, 2]]`
- **Output:** `[7, 4]`
- **Explanation:** Replacing the only edge weight changes the root-to-`2` distance from `7` to `4`.

#### Example 2

- **Input:** `n = 3, edges = [[1, 2, 2], [1, 3, 4]], queries = [[2, 1], [2, 3], [1, 1, 3, 7], [2, 2], [2, 3]]`
- **Output:** `[0, 4, 2, 7]`
- **Explanation:** The update affects node `3` but not the other root branch.

#### Example 3

- **Input:** `n = 4, edges = [[1, 2, 2], [2, 3, 1], [3, 4, 5]], queries = [[2, 4], [2, 3], [1, 2, 3, 3], [2, 2], [2, 3]]`
- **Output:** `[8, 3, 2, 5]`
- **Explanation:** Updating the middle edge shifts distances for nodes `3` and `4`, while node `2` remains unchanged.
