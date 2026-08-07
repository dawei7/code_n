## Description

You are given a directed, weighted graph with `n` nodes labeled from 0 to `n - 1`, and an array `edges` where `edges[i] = [u_i, v_i, w_i]` represents a directed edge from node `u_i` to node `v_i` with cost `w_i`.

Each node `u_i` has a switch that can be used **at most once**: when you arrive at `u_i` and have not yet used its switch, you may activate it on one of its incoming edges `v_i → u_i` reverse that edge to `u_i → v_i` and **immediately** traverse it.

The reversal is only valid for that single move, and using a reversed edge costs `2 * w_i`.

Return the **minimum** total cost to travel from node 0 to node `n - 1`. If it is not possible, return -1.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 4, edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]</span>

**Output:** <span class="example-io">5</span>

**Explanation: **

**

![](images/e1drawio.png)

**

	- Use the path `0 → 1` (cost 3).

	- At node 1 reverse the original edge `3 → 1` into `1 → 3` and traverse it at cost `2 * 1 = 2`.

	- Total cost is `3 + 2 = 5`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 4, edges = [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

	- No reversal is needed. Take the path `0 → 2` (cost 1), then `2 → 1` (cost 1), then `1 → 3` (cost 1).

	- Total cost is `1 + 1 + 1 = 3`.

</div>

**Constraints:**

	- `2 <= n <= 5 * 10^4`

	- `1 <= edges.length <= 10^5`

	- `edges[i] = [u_i, v_i, w_i]`

	- `0 <= u_i, v_i <= n - 1`

	- `1 <= w_i <= 1000`
