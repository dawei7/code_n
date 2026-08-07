## Description

You are given an integer `n` and an undirected tree rooted at node 0 with `n` nodes numbered from 0 to `n - 1`. This is represented by a 2D array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i]` indicates an undirected edge between nodes `u_i` and `v_i`.

You are also given an integer array `nums`, where `nums[i]` is the positive integer assigned to node `i`.

Define a value `t_i` as the number of **ancestors** of node `i` such that the product `nums[i] * nums[ancestor]` is a **<span data-keyword="perfect-square">perfect square</span>**.

Return the sum of all `t_i` values for all nodes `i` in range `[1, n - 1]`.

**Note**:

	- In a rooted tree, the **ancestors** of node `i` are all nodes on the path from node `i` to the root node 0, **excluding** `i` itself.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 3, edges = [[0,1],[1,2]], nums = [2,8,2]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`**i**`</th>
			<th style="border: 1px solid black;">**Ancestors**</th>
			<th style="border: 1px solid black;">`**nums[i] * nums[ancestor]**`</th>
			<th style="border: 1px solid black;">Square Check</th>
			<th style="border: 1px solid black;">`**t_i**`</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[0]</td>
			<td style="border: 1px solid black;">`nums[1] * nums[0] = 8 * 2 = 16`</td>
			<td style="border: 1px solid black;">16 is a perfect square</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">[1, 0]</td>
			<td style="border: 1px solid black;">`nums[2] * nums[1] = 2 * 8 = 16`

			`nums[2] * nums[0] = 2 * 2 = 4`</td>
			<td style="border: 1px solid black;">Both 4 and 16 are perfect squares</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
	</tbody>
</table>

Thus, the total number of valid ancestor pairs across all non-root nodes is `1 + 2 = 3`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 3, edges = [[0,1],[0,2]], nums = [1,2,4]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`**i**`</th>
			<th style="border: 1px solid black;">**Ancestors**</th>
			<th style="border: 1px solid black;">`**nums[i] * nums[ancestor]**`</th>
			<th style="border: 1px solid black;">Square Check</th>
			<th style="border: 1px solid black;">`**t_i**`</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[0]</td>
			<td style="border: 1px solid black;">`nums[1] * nums[0] = 2 * 1 = 2`</td>
			<td style="border: 1px solid black;">2 is **not** a perfect square</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">[0]</td>
			<td style="border: 1px solid black;">`nums[2] * nums[0] = 4 * 1 = 4`</td>
			<td style="border: 1px solid black;">4 is a perfect square</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
	</tbody>
</table>

Thus, the total number of valid ancestor pairs across all non-root nodes is 1.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">n = 4, edges = [[0,1],[0,2],[1,3]], nums = [1,2,9,4]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">**Ancestors**</th>
			<th style="border: 1px solid black;">`**nums[i] * nums[ancestor]**`</th>
			<th style="border: 1px solid black;">Square Check</th>
			<th style="border: 1px solid black;">`**t_i**`</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[0]</td>
			<td style="border: 1px solid black;">`nums[1] * nums[0] = 2 * 1 = 2`</td>
			<td style="border: 1px solid black;">2 is **not** a perfect square</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">[0]</td>
			<td style="border: 1px solid black;">`nums[2] * nums[0] = 9 * 1 = 9`</td>
			<td style="border: 1px solid black;">9 is a perfect square</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">[1, 0]</td>
			<td style="border: 1px solid black;">`nums[3] * nums[1] = 4 * 2 = 8`

			`nums[3] * nums[0] = 4 * 1 = 4`</td>
			<td style="border: 1px solid black;">Only 4 is a perfect square</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
	</tbody>
</table>

Thus, the total number of valid ancestor pairs across all non-root nodes is `0 + 1 + 1 = 2`.

</div>

**Constraints:**

	- `1 <= n <= 10^5`

	- `edges.length == n - 1`

	- `edges[i] = [u_i, v_i]`

	- `0 <= u_i, v_i <= n - 1`

	- `nums.length == n`

	- `1 <= nums[i] <= 10^5`

	- The input is generated such that `edges` represents a valid tree.
