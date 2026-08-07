## Description

You are given a rooted tree with `n` nodes labeled from 0 to `n - 1`, represented by an integer array `parent` of length `n`, where:

	- `parent[0] = -1` (node 0 is the root).

	- For each `1 <= i < n`, `parent[i]` is the parent of node `i` (`0 <= parent[i] < i`).

You are also given an integer array <font face="monospace">nums</font> of length `n`, where `<font face="monospace">nums[i]</font>` is the value of node `i`, and an integer `k`.

A non-empty subset of nodes is called **valid** if:

	- The **sum** of the values of the selected nodes is **divisible** by `k`.

	- No **two** selected nodes are **adjacent** in the tree (no node and its direct parent are both included in the subset).

Return the number of valid subsets modulo `10^9 + 7`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">parent = [-1,0,1], nums = [1,2,3], k = 3</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

**

![](images/image1.png)

​​​​​​​**

The only valid subset is `{2}`. It contains node 2 with value 3, which is divisible by 3.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">parent = [-1,0,0,0], nums = [2,1,2,1], k = 3</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

**

![](images/image2.png)

​​​​​​​**​​​​​​​

The valid subsets are:

	- `{1, 2}`: Nodes 1 and 2 are both children of node 0 and not directly connected to each other. Their values sum to `1 + 2 = 3`, which is divisible by 3.

	- `{2, 3}`: Nodes 2 and 3 are also non-adjacent. Their values sum to `2 + 1 = 3`, which is divisible by 3.

No other subset satisfies both conditions. Therefore, the answer is 2.

</div>

**Constraints:**

	- `n == parent.length == nums.length`

	- `1 <= n <= 1000`

	- `parent[0] == -1`

	- For all `1 <= i < n`:

		<li data-end="147" data-start="103">`0 <= parent[i] < i`

	</li>
	- `1 <= nums[i] <= 10^9`

	- `1 <= k <= 100`​​​​​​​​​​​​​​`​​​​​​​`

	- `parent` describes a valid rooted tree.
