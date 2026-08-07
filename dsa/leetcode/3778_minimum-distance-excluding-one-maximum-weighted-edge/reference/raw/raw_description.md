## Description

You are given a positive integer `n` and a 2D integer array `edges`, where `edges[i] = [u_i, v_i, w_i]`.

There is a **weighted** **connected** simple undirected graph with `n` nodes labeled from 0 to `n - 1`. Each `[u_i, v_i, w_i]` in `edges` represents an edge between node `u_i` and node `v_i` with **positive** weight `w_i`.

The **cost** of a path is the **sum** of weights of the edges in the path, **excluding** the edge with the **maximum** weight. If there are multiple edges in the path with the maximum weight, **only** the **first** such edge is excluded.

Return an integer representing the **minimum** **cost** of a path going from node 0 to node `n - 1`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 5, edges = [[0,1,2],[1,2,7],[2,3,7],[3,4,4]]</span>

**Output:** <span class="example-io">13</span>

**Explanation:**

There is only one path going from node 0 to node 4: `0 -> 1 -> 2 -> 3 -> 4`.

The edge weights on this path are 2, 7, 7, and 4.

Excluding the first edge with maximum weight, which is `1 -> 2`, the cost of this path is `2 + 7 + 4 = 13`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 3, edges = [[0,1,1],[1,2,1],[0,2,50000]]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

There are two paths going from node 0 to node 2:

	- `0 -> 1 -> 2`

The edge weights on this path are 1 and 1.

Excluding the first edge with maximum weight, which is `0 -> 1`, the cost of this path is 1.

	- `0 -> 2`

The only edge weight on this path is 1.

Excluding the first edge with maximum weight, which is `0 -> 2`, the cost of this path is 0.

The minimum cost is `min(1, 0) = 0`.

</div>

**Constraints:**

	- `2 <= n <= 5 * 10^4`

	- `n - 1 <= edges.length <= 10^9`

	- `edges[i] = [u_i, v_i, w_i]`

	- `0 <= u_i < v_i < n`

	- `[u_i, v_i] != [u_j, v_j]`

	- `1 <= w_i <= 5 * 10^4`

	- The graph is connected.
