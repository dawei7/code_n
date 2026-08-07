## Description

You are given an undirected graph with `n` nodes labeled from 0 to `n - 1`. Node `i` has a **value** of `nums[i]`, which is either 0 or 1. The edges of the graph are given by a 2D array `edges` where `edges[i] = [u_i, v_i]` represents an edge between node `u_i` and node `v_i`.

For a **non-empty subset** `s` of nodes in the graph, we consider the **induced subgraph** of `s` generated as follows:

	- We keep only the nodes in `s`.

	- We keep only the edges whose two endpoints are both in `s`.

Return an integer representing the number of **non-empty** subsets `s` of nodes in the graph such that:

	- The **induced subgraph** of `s` is **connected**.

	- The **sum** of node **values** in `s` is **even**.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,0,1], edges = [[0,1],[1,2]]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`s`</th>
			<th style="border: 1px solid black;">connected?</th>
			<th style="border: 1px solid black;">sum of node values</th>
			<th style="border: 1px solid black;">counted?</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">`[0]`</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">No</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[1]`</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">Yes</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[2]`</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">No</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[0,1]`</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">No</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[0,2]`</td>
			<td style="border: 1px solid black;">No, node 0 and node 2 are disconnected.</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">No</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[1,2]`</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">No</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[0,1,2]`</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">Yes</td>
		</tr>
	</tbody>
</table>
</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1], edges = []</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`s`</th>
			<th style="border: 1px solid black;">connected?</th>
			<th style="border: 1px solid black;">sum of node values</th>
			<th style="border: 1px solid black;">counted?</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">`[0]`</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">No</td>
		</tr>
	</tbody>
</table>
</div>

**Constraints:**

	- `1 <= n == nums.length <= 13`

	- `nums[i]` is 0 or 1.

	- `0 <= edges.length <= n * (n - 1) / 2`

	- `edges[i] = [u_i, v_i]`

	- `0 <= u_i < v_i < n`

	- All edges are **distinct**.
