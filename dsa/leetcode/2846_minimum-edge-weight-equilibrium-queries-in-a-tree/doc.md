# Minimum Edge Weight Equilibrium Queries in a Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2846 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Tree, Depth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/) |

## Problem Description

### Goal

An undirected tree has `n` nodes numbered from `0` through `n - 1`. Each entry `edges[i] = [u_i, v_i, w_i]` joins two nodes with an edge whose weight is `w_i`. The array contains exactly `n - 1` edges and is guaranteed to describe a valid tree.

For every query `queries[i] = [a_i, b_i]`, consider the unique simple path from `a_i` to `b_i`. One operation may select any tree edge and replace its weight with any value. Determine the minimum number of operations needed to make every edge on that query's path have the same weight.

Queries are independent: any changes considered for one query do not carry into another, and each query starts from the original weighted tree. Return the answers in query order. A path is the sequence of distinct nodes from one endpoint to the other in which consecutive nodes share an edge.

### Function Contract

**Inputs**

- `n`: The number of nodes in the tree.
- `edges`: The `n - 1` entries `[u, v, w]` describing undirected weighted edges.
- `queries`: The `m` endpoint pairs `[a, b]` whose paths must be evaluated.

The constraints are $1\le n\le10^4$, $1\le w\le26$, and $1\le m\le2\cdot10^4$. Every node index in `edges` and `queries` lies from `0` through `n - 1`, and `edges` represents a valid tree.

**Return value**

- An array of length $m$ whose $i$th entry is the minimum number of edge-weight changes for `queries[i]`.

### Examples

#### Example 1

- **Input:** `n = 7, edges = [[0,1,1],[1,2,1],[2,3,1],[3,4,2],[4,5,2],[5,6,2]], queries = [[0,3],[3,6],[2,6],[0,6]]`
- **Output:** `[0,0,1,3]`
- **Explanation:** The first two paths already have uniform weights. The third changes its one weight-`1` edge to `2`, while the full path needs three of its six edges changed.

#### Example 2

- **Input:** `n = 8, edges = [[1,2,6],[1,3,4],[2,4,6],[2,5,3],[3,6,6],[3,0,8],[7,0,2]], queries = [[4,6],[0,4],[6,5],[7,4]]`
- **Output:** `[1,2,2,3]`
- **Explanation:** For each path, retaining its most frequent existing weight minimizes how many other edges must be changed.
