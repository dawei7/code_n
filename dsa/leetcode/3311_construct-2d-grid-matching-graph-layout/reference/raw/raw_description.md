## Description

You are given a 2D integer array `edges` representing an **undirected** graph having `n` nodes, where `edges[i] = [u_i, v_i]` denotes an edge between nodes `u_i` and `v_i`.

Construct a 2D grid that satisfies these conditions:

	- The grid contains **all nodes** from `0` to `n - 1` in its cells, with each node appearing exactly **once**.

	- Two nodes should be in adjacent grid cells (**horizontally** or **vertically**) **if and only if** there is an edge between them in `edges`.

It is guaranteed that `edges` can form a 2D grid that satisfies the conditions.

Return a 2D integer array satisfying the conditions above. If there are multiple solutions, return *any* of them.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 4, edges = [[0,1],[0,2],[1,3],[2,3]]</span>

**Output:** <span class="example-io">[[3,1],[2,0]]</span>

**Explanation:**

![](images/screenshot-from-2024-08-11-14-07-59.png)

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 5, edges = [[0,1],[1,3],[2,3],[2,4]]</span>

**Output:** <span class="example-io">[[4,2,3,1,0]]</span>

**Explanation:**

![](images/screenshot-from-2024-08-11-14-06-02.png)

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">n = 9, edges = [[0,1],[0,4],[0,5],[1,7],[2,3],[2,4],[2,5],[3,6],[4,6],[4,7],[6,8],[7,8]]</span>

**Output:** <span class="example-io">[[8,6,3],[7,4,2],[1,0,5]]</span>

**Explanation:**

![](images/screenshot-from-2024-08-11-14-06-38.png)

</div>

**Constraints:**

	- `2 <= n <= 5 * 10^4`

	- `1 <= edges.length <= 10^5`

	- `edges[i] = [u_i, v_i]`

	- `0 <= u_i < v_i < n`

	- All the edges are distinct.

	- The input is generated such that `edges` can form a 2D grid that satisfies the conditions.
