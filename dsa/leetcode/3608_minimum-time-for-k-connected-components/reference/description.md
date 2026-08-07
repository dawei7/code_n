## Description

You are given an integer `n` and an undirected graph with `n` nodes labeled from 0 to $n - 1$. This is represented by a 2D array `edges`, where $\text{edges}[i] = [u_{i}, v_{i}, \text{time}_{i}]$ indicates an undirected edge between nodes $u_{i}$ and $v_{i}$ that can be removed at $\text{time}_{i}$.

You are also given an integer `k`.

Initially, the graph may be connected or disconnected. Your task is to find the **minimum** time `t` such that after removing all edges with $time \le t$, the graph contains **at least** `k` connected components.

Return the **minimum** time `t`.

A **connected component** is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** n = 2, edges = [[0,1,3]], k = 2

**Output:** 3

**Explanation:**

![](images/screenshot-2025-06-01-at-022724.png)

- Initially, there is one connected component `{0, 1}`.

- At $time = 1$ or `2`, the graph remains unchanged.

- At $time = 3$, edge `[0, 1]` is removed, resulting in $k = 2$ connected components `{0}`, `{1}`. Thus, the answer is 3.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 3, edges = [[0,1,2],[1,2,4]], k = 3

**Output:** 4

**Explanation:**

![](images/screenshot-2025-06-01-at-022812.png)

- Initially, there is one connected component `{0, 1, 2}`.

- At $time = 2$, edge `[0, 1]` is removed, resulting in two connected components `{0}`, `{1, 2}`.

- At $time = 4$, edge `[1, 2]` is removed, resulting in $k = 3$ connected components `{0}`, `{1}`, `{2}`. Thus, the answer is 4.

</div>
#### Example 3

<div class="example-block">
**Input:** n = 3, edges = [[0,2,5]], k = 2

**Output:** 0

**Explanation:**

![](images/screenshot-2025-06-01-at-022930.png)

- Since there are already $k = 2$ disconnected components `{1}`, `{0, 2}`, no edge removal is needed. Thus, the answer is 0.

</div>
### Constraints

- $1 \le n \le 10^{5}$

- $0 \le \text{edges.length} \le 10^{5}$

- $\text{edges}[i] = [u_{i}, v_{i}, \text{time}_{i}]$

- $0 \le u_{i}, v_{i} < n$

- $u_{i} \neq v_{i}$

- $1 \le \text{time}_{i} \le 10^{9}$

- $1 \le k \le n$

- There are no duplicate edges.