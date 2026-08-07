## Description

You are given a positive integer `n` and a 2D integer array `edges`, where $\text{edges}[i] = [u_{i}, v_{i}, w_{i}]$.

There is a **weighted** **connected** simple undirected graph with `n` nodes labeled from 0 to $n - 1$. Each $[u_{i}, v_{i}, w_{i}]$ in `edges` represents an edge between node $u_{i}$ and node $v_{i}$ with **positive** weight $w_{i}$.

The **cost** of a path is the **sum** of weights of the edges in the path, **excluding** the edge with the **maximum** weight. If there are multiple edges in the path with the maximum weight, **only** the **first** such edge is excluded.

Return an integer representing the **minimum** **cost** of a path going from node 0 to node $n - 1$.
### Function Contract

**Inputs**

- `n`: The number of graph nodes.
- `edges`: The graph's unique undirected edges, each encoded as `[u_i, v_i, w_i]`.

Let $N=n$ and $E=\lvert\texttt{edges}\rvert$. Each listed pair satisfies $u_i<v_i$; this ordering is part of the input representation and does not give the undirected edge a direction. A path's excluded edge is chosen from that path, not from the graph as a whole.

**Return value**

Return the least path-weight sum from node `0` to node `n - 1` after omitting exactly the first occurrence of that path's maximum edge weight.

### Examples
#### Example 1

<div class="example-block">
**Input:** n = 5, edges = [[0,1,2],[1,2,7],[2,3,7],[3,4,4]]

**Output:** 13

**Explanation:**

There is only one path going from node 0 to node 4: `0 -> 1 -> 2 -> 3 -> 4`.

The edge weights on this path are 2, 7, 7, and 4.

Excluding the first edge with maximum weight, which is `1 -> 2`, the cost of this path is $2 + 7 + 4 = 13$.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 3, edges = [[0,1,1],[1,2,1],[0,2,50000]]

**Output:** 0

**Explanation:**

There are two paths going from node 0 to node 2:

- `0 -> 1 -> 2`

The edge weights on this path are 1 and 1.

Excluding the first edge with maximum weight, which is `0 -> 1`, the cost of this path is 1.

- `0 -> 2`

The only edge weight on this path is 1.

Excluding the first edge with maximum weight, which is `0 -> 2`, the cost of this path is 0.

The minimum cost is $min(1, 0) = 0$.

</div>
### Constraints

- $2 \le n \le 5 * 10^{4}$

- $n - 1 \le \text{edges.length} \le 10^{9}$

- $\text{edges}[i] = [u_{i}, v_{i}, w_{i}]$

- $0 \le u_{i} < v_{i} < n$

- $[u_{i}, v_{i}] \neq [u_{j}, v_{j}]$

- $1 \le w_{i} \le 5 * 10^{4}$

- The graph is connected.