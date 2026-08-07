## Description

You are given an integer `n` representing the number of nodes in a graph, labeled from 0 to `n - 1`.

You are also given an integer array `nums` of length `n` and an integer `maxDiff`.

An **undirected **edge exists between nodes `i` and `j` if the **absolute** difference between `nums[i]` and `nums[j]` is **at most** `maxDiff` (i.e., `|nums[i] - nums[j]| <= maxDiff`).

You are also given a 2D integer array `queries`. For each `queries[i] = [u_i, v_i]`, find the **minimum** distance between nodes `u_i` and `v_i`_. If no path exists between the two nodes, return -1 for that query.

Return an array `answer`, where `answer[i]` is the result of the `i^th` query.

**Note:** The edges between the nodes are unweighted.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 5, nums = [1,8,3,4,2], maxDiff = 3, queries = [[0,3],[2,4]]</span>

**Output:** <span class="example-io">[1,1]</span>

**Explanation:**

The resulting graph is:

![](images/4149example1drawio.png)

<table>
	<tbody>
		<tr>
			<th>Query</th>
			<th>Shortest Path</th>
			<th>Minimum Distance</th>
		</tr>
		<tr>
			<td>[0, 3]</td>
			<td>0 → 3</td>
			<td>1</td>
		</tr>
		<tr>
			<td>[2, 4]</td>
			<td>2 → 4</td>
			<td>1</td>
		</tr>
	</tbody>
</table>

Thus, the output is `[1, 1]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 5, nums = [5,3,1,9,10], maxDiff = 2, queries = [[0,1],[0,2],[2,3],[4,3]]</span>

**Output:** <span class="example-io">[1,2,-1,1]</span>

**Explanation:**

The resulting graph is:

![](images/4149example2drawio.png)

</div>

<table>
	<tbody>
		<tr>
			<th>Query</th>
			<th>Shortest Path</th>
			<th>Minimum Distance</th>
		</tr>
		<tr>
			<td>[0, 1]</td>
			<td>0 → 1</td>
			<td>1</td>
		</tr>
		<tr>
			<td>[0, 2]</td>
			<td>0 → 1 → 2</td>
			<td>2</td>
		</tr>
		<tr>
			<td>[2, 3]</td>
			<td>None</td>
			<td>-1</td>
		</tr>
		<tr>
			<td>[4, 3]</td>
			<td>3 → 4</td>
			<td>1</td>
		</tr>
	</tbody>
</table>

Thus, the output is `[1, 2, -1, 1]`.

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">n = 3, nums = [3,6,1], maxDiff = 1, queries = [[0,0],[0,1],[1,2]]</span>

**Output:** <span class="example-io">[0,-1,-1]</span>

**Explanation:**

There are no edges between any two nodes because:

	- Nodes 0 and 1: `|nums[0] - nums[1]| = |3 - 6| = 3 > 1`

	- Nodes 0 and 2: `|nums[0] - nums[2]| = |3 - 1| = 2 > 1`

	- Nodes 1 and 2: `|nums[1] - nums[2]| = |6 - 1| = 5 > 1`

Thus, no node can reach any other node, and the output is `[0, -1, -1]`.

</div>

**Constraints:**

	- `1 <= n == nums.length <= 10^5`

	- `0 <= nums[i] <= 10^5`

	- `0 <= maxDiff <= 10^5`

	- `1 <= queries.length <= 10^5`

	- `queries[i] == [u_i, v_i]`

	- `0 <= u_i, v_i < n`
