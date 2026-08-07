## Description

You are given an integer `n` and an undirected tree with `n` nodes numbered from 0 to `n - 1`. The tree is represented by a 2D array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i]` indicates an undirected edge between `u_i` and `v_i`.

You are also given three **distinct** target nodes `x`, `y`, and `z`.

For any node `u` in the tree:

	- Let `dx` be the distance from `u` to node `x`

	- Let `dy` be the distance from `u` to node `y`

	- Let `dz` be the distance from `u` to node `z`

The node `u` is called **special** if the three distances form a **Pythagorean Triplet**.

Return an integer denoting the number of special nodes in the tree.

A **Pythagorean triplet** consists of three integers `a`, `b`, and `c` which, when sorted in **ascending** order, satisfy `a^2 + b^2 = c^2`.

The **distance** between two nodes in a tree is the number of edges on the unique path between them.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 4, edges = [[0,1],[0,2],[0,3]], x = 1, y = 2, z = 3</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

For each node, we compute its distances to nodes `x = 1`, `y = 2`, and `z = 3`.

	- Node 0 has distances 1, 1, and 1. After sorting, the distances are 1, 1, and 1, which do not satisfy the Pythagorean condition.

	- Node 1 has distances 0, 2, and 2. After sorting, the distances are 0, 2, and 2. Since `0^2 + 2^2 = 2^2`, node 1 is special.

	- Node 2 has distances 2, 0, and 2. After sorting, the distances are 0, 2, and 2. Since `0^2 + 2^2 = 2^2`, node 2 is special.

	- Node 3 has distances 2, 2, and 0. After sorting, the distances are 0, 2, and 2. This also satisfies the Pythagorean condition.

Therefore, nodes 1, 2, and 3 are special, and the answer is 3.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 4, edges = [[0,1],[1,2],[2,3]], x = 0, y = 3, z = 2</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

For each node, we compute its distances to nodes `x = 0`, `y = 3`, and `z = 2`.

	- Node 0 has distances 0, 3, and 2. After sorting, the distances are 0, 2, and 3, which do not satisfy the Pythagorean condition.

	- Node 1 has distances 1, 2, and 1. After sorting, the distances are 1, 1, and 2, which do not satisfy the Pythagorean condition.

	- Node 2 has distances 2, 1, and 0. After sorting, the distances are 0, 1, and 2, which do not satisfy the Pythagorean condition.

	- Node 3 has distances 3, 0, and 1. After sorting, the distances are 0, 1, and 3, which do not satisfy the Pythagorean condition.

No node satisfies the Pythagorean condition. Therefore, the answer is 0.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">n = 4, edges = [[0,1],[1,2],[1,3]], x = 1, y = 3, z = 0</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

For each node, we compute its distances to nodes `x = 1`, `y = 3`, and `z = 0`.

	- Node 0 has distances 1, 2, and 0. After sorting, the distances are 0, 1, and 2, which do not satisfy the Pythagorean condition.

	- Node 1 has distances 0, 1, and 1. After sorting, the distances are 0, 1, and 1. Since `0^2 + 1^2 = 1^2`, node 1 is special.

	- Node 2 has distances 1, 2, and 2. After sorting, the distances are 1, 2, and 2, which do not satisfy the Pythagorean condition.

	- Node 3 has distances 1, 0, and 2. After sorting, the distances are 0, 1, and 2, which do not satisfy the Pythagorean condition.

Therefore, the answer is 1.

</div>

**Constraints:**

	- `4 <= n <= 10^5`

	- `edges.length == n - 1`

	- `edges[i] = [u_i, v_i]`

	- `0 <= u_i, v_i, x, y, z <= n - 1`

	- `x`, `y`, and `z` are pairwise **distinct**.

	- The input is generated such that `edges` represent a valid tree.
