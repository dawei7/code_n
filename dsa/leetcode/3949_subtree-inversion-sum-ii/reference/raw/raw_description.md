## Description

You are given an undirected tree rooted at node 0, with `n` nodes numbered from 0 to `n - 1`. The tree is represented by a 2D integer array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i]` indicates an edge between nodes `u_i` and `v_i`.

You are also given an integer array `nums` of length `n`, where `nums[i]` represents the value at node `i`, and an integer `k`.

You may perform **inversion operations** on a <span data-keyword="subset">subset</span> of nodes subject to the following rules:

	- **Subtree Inversion Operation:**

		<li data-end="887" data-start="802">
		When you invert a node, every value in the <span data-keyword="subtree-of-node">subtree</span> rooted at that node is multiplied by -1.

	</li>
	- **Distance Constraint on Inversions:**

		<li data-end="1020" data-start="934">
		You may only invert a node if it is “sufficiently far” from any other inverted node.

		- If you invert two nodes `a` and `b`, the **distance** (the number of edges on the unique path between them) must be **at least** `k`.

	</li>

Return the **maximum** possible **sum** of the tree’s node values after applying **inversion operations**.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">edges = [[0,1],[0,2],[0,3],[1,4],[1,5]], nums = [1,0,-10,3,4,5], k = 2</span>

**Output:** <span class="example-io">23</span>

**Explanation:**

![](images/4183example1drawio.png)

After inverting the subtree rooted at node 2, the maximum sum becomes `1 + 0 + 10 + 3 + 4 + 5 = 23`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">edges = [[0,1],[1,2]], nums = [5,-10,-10], k = 1</span>

**Output:** <span class="example-io">25</span>

**Explanation:**

**

![](images/4183example2drawio.png)

**

After inverting the subtree rooted at node 1, the maximum sum becomes `5 + 10 + 10 = 25`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">edges = [[0,1],[0,2]], nums = [1,-5,-6], k = 2</span>

**Output:** <span class="example-io">12</span>

**Explanation:**

![](images/4183example3drawio.png)

	- After inverting the subtrees rooted at nodes 1 and 2, `nums = [1, 5, 6]`.

	- This is valid because nodes 1 and 2 are two edges apart (`1 → 0` and `0 → 2`), which is at least `k`.

	- The maximum sum is `1 + 5 + 6 = 12`.

</div>

**Example 4:**

<div class="example-block">
**Input:** <span class="example-io">edges = [[0,1],[0,2]], nums = [1,-5,-6], k = 3</span>

**Output:** <span class="example-io">10</span>

**Explanation:**

![](images/4183example4drawio.png)

	- After inverting the subtree rooted at nodes 0, `nums = [-1, 5, 6]`.

	- The maximum sum is `(-1) + 5 + 6 = 10`.

	- Note that we cannot invert nodes 1 and 2 because their distance is `2 < k = 3`.

</div>

**Constraints:**

	- `nums.length == n`

	- `edges.length == n - 1`

	- `2 <= n <= 5 * 10^4`

	- `edges[i].length == 2`

	- `0 <= edges[i][0], edges[i][1] < n`

	- `-4 * 10^4 <= nums[i] <= 4 * 10^4`

	- `1 <= k <= 50`

	- It is guaranteed that `edges` forms a tree.
