## Description

There is an undirected weighted graph with `n` nodes labeled from 0 to `n - 1`.

The graph is represented by a 2D integer array `edges`, where each edge `edges[i] = [u_i, v_i, w_​​​​​​​i]` indicates that there is an undirected edge between nodes `u_i` and `v_i` with weight `w_​​​​​​​i`.

You are also given integers `source`, `target` and `k`.

A `threshold` value determines whether an edge is considered **light** or **heavy**:

	- An edge is **light** if its weight is **less than** or **equal** to `threshold`.

	- An edge is **heavy** if its weight is **greater than** `threshold`.

A path from `source` to `target` is **valid** if it contains **at most** `k` heavy edges.

Return the **minimum integer **`threshold` such that **at least** one **valid** path exists from `source` to `target`. If no such path exists, return -1.

**Example 1:**​​​​​​​​​​​​​​

​​​​​​​

![](images/g6.png)

<div class="example-block">
**Input:** <span class="example-io">n = 6, edges = [[0,1,5],[1,2,3],[3,4,4],[4,5,1],[1,4,2]], source = 0, target = 3, k = 1</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

The minimum `threshold` such that a path from node 0 to node 3 uses at most 1 heavy edge is 4.

	- Light edges: `[1, 2, 3]`, `[3, 4, 4]`, `[4, 5, 1]`, `[1, 4, 2]`

	- Heavy edges: `[0, 1, 5]`

A valid path is `0 → 1 → 4 → 3`. It uses only 1 heavy edge (`[0, 1, 5]`), which satisfies the limit `k = 1`.

Any smaller `threshold` would make it impossible to reach node 3 without exceeding 1 heavy edge.

</div>

**Example 2:**

![](images/g3_f.png)

<div class="example-block">
**Input:** <span class="example-io">n = 6, edges = [[0,1,3],[1,2,4],[3,4,5],[4,5,6]], source = 0, target = 4, k = 1</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

There is no path from node 0 to node 4. Since the target cannot be reached, the output is -1.

</div>

**Example 3:**

**

![](images/g5.png)

**

<div class="example-block">
**Input:** <span class="example-io">n = 4, edges = [[0,1,2],[1,2,2],[2,3,2],[3,0,2]], source = 0, target = 0, k = 0</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

The source and target are the same node. No edges need to be traversed, so the minimum `threshold` is 0.

</div>

**Constraints:**

	- `1 <= n <= 10^3​​​​​​​`

	- `0 <= edges.length <= 10^3​​​​​​​`

	- `edges[i] = [u_i, v_i, w_i]`

	- `0 <= u_i, v_i​​​​​​​ <= n - 1`

	- `1 <= w_i​​​​​​​ <= 10^9`

	- `0 <= source, target <= n - 1`

	- `0 <= k <= edges.length`
