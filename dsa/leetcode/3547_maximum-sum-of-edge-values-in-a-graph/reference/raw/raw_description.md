## Description

You are given an **undirected connected** graph of `n` nodes, numbered from `0` to `n - 1`. Each node is connected to **at most** 2 other nodes.

The graph consists of `m` edges, represented by a 2D array `edges`, where `edges[i] = [a_i, b_i]` indicates that there is an edge between nodes `a_i` and `b_i`.

You have to assign a **unique** value from `1` to `n` to each node. The value of an edge will be the **product** of the values assigned to the two nodes it connects.

Your score is the sum of the values of all edges in the graph.

Return the **maximum** score you can achieve.

**Example 1:**

![](images/screenshot-from-2025-05-13-01-27-52.png)

<div class="example-block">
**Input:** <span class="example-io">n = 4, edges = </span>[[0,1],[1,2],[2,3]]

**Output:** 23

**Explanation:**

The diagram above illustrates an optimal assignment of values to nodes. The sum of the values of the edges is: `(1 * 3) + (3 * 4) + (4 * 2) = 23`.

</div>

**Example 2:**

![](images/graphproblemex2drawio.png)

<div class="example-block">
**Input:** <span class="example-io">n = 6, edges = [[0,3],[4,5],[2,0],[1,3],[2,4],[1,5]]</span>

**Output:** <span class="example-io">82</span>

**Explanation:**

The diagram above illustrates an optimal assignment of values to nodes. The sum of the values of the edges is: `(1 * 2) + (2 * 4) + (4 * 6) + (6 * 5) + (5 * 3) + (3 * 1) = 82`.

</div>

**Constraints:**

	- `1 <= n <= 5 * 10^4`

	- `m == edges.length`

	- `1 <= m <= n`

	- `edges[i].length == 2`

	- `0 <= a_i, b_i < n`

	- `a_i != b_i`

	- There are no repeated edges.

	- The graph is connected.

	- Each node is connected to at most 2 other nodes.
