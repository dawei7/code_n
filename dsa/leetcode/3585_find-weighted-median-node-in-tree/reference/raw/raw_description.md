## Description

You are given an integer `n` and an **undirected, weighted** tree rooted at node 0 with `n` nodes numbered from 0 to `n - 1`. This is represented by a 2D array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i, w_i]` indicates an edge from node `u_i` to `v_i` with weight `w_i`.

The **weighted median node** is defined as the **first** node `x` on the path from `u_i` to `v_i` such that the sum of edge weights from `u_i` to `x` is **greater than or equal to half** of the total path weight.

You are given a 2D integer array `queries`. For each `queries[j] = [u_j, v_j]`, determine the weighted median node along the path from `u_j` to `v_j`.

Return an array `ans`, where `ans[j]` is the node index of the weighted median for `queries[j]`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 2, edges = [[0,1,7]], queries = [[1,0],[0,1]]</span>

**Output:** <span class="example-io">[0,1]</span>

**Explanation:**

![](images/screenshot-2025-05-26-at-193447.png)

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Query</th>
			<th style="border: 1px solid black;">Path</th>
			<th style="border: 1px solid black;">Edge

			Weights</th>
			<th style="border: 1px solid black;">Total

			Path

			Weight</th>
			<th style="border: 1px solid black;">Half</th>
			<th style="border: 1px solid black;">Explanation</th>
			<th style="border: 1px solid black;">Answer</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">`[1, 0]`</td>
			<td style="border: 1px solid black;">`1 → 0`</td>
			<td style="border: 1px solid black;">`[7]`</td>
			<td style="border: 1px solid black;">7</td>
			<td style="border: 1px solid black;">3.5</td>
			<td style="border: 1px solid black;">Sum from `1 → 0 = 7 >= 3.5`, median is node 0.</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[0, 1]`</td>
			<td style="border: 1px solid black;">`0 → 1`</td>
			<td style="border: 1px solid black;">`[7]`</td>
			<td style="border: 1px solid black;">7</td>
			<td style="border: 1px solid black;">3.5</td>
			<td style="border: 1px solid black;">Sum from `0 → 1 = 7 >= 3.5`, median is node 1.</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
	</tbody>
</table>
</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 3, edges = [[0,1,2],[2,0,4]], queries = [[0,1],[2,0],[1,2]]</span>

**Output:** <span class="example-io">[1,0,2]</span>

**E****xplanation:**

![](images/screenshot-2025-05-26-at-193610.png)

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Query</th>
			<th style="border: 1px solid black;">Path</th>
			<th style="border: 1px solid black;">Edge

			Weights</th>
			<th style="border: 1px solid black;">Total

			Path

			Weight</th>
			<th style="border: 1px solid black;">Half</th>
			<th style="border: 1px solid black;">Explanation</th>
			<th style="border: 1px solid black;">Answer</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">`[0, 1]`</td>
			<td style="border: 1px solid black;">`0 → 1`</td>
			<td style="border: 1px solid black;">`[2]`</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">Sum from `0 → 1 = 2 >= 1`, median is node 1.</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[2, 0]`</td>
			<td style="border: 1px solid black;">`2 → 0`</td>
			<td style="border: 1px solid black;">`[4]`</td>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">Sum from `2 → 0 = 4 >= 2`, median is node 0.</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[1, 2]`</td>
			<td style="border: 1px solid black;">`1 → 0 → 2`</td>
			<td style="border: 1px solid black;">`[2, 4]`</td>
			<td style="border: 1px solid black;">6</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">Sum from `1 → 0 = 2 < 3`.

			Sum from `1 → 2 = 2 + 4 = 6 >= 3`, median is node 2.</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
	</tbody>
</table>
</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">n = 5, edges = [[0,1,2],[0,2,5],[1,3,1],[2,4,3]], queries = [[3,4],[1,2]]</span>

**Output:** <span class="example-io">[2,2]</span>

**Explanation:**

![](images/screenshot-2025-05-26-at-193857.png)

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Query</th>
			<th style="border: 1px solid black;">Path</th>
			<th style="border: 1px solid black;">Edge

			Weights</th>
			<th style="border: 1px solid black;">Total

			Path

			Weight</th>
			<th style="border: 1px solid black;">Half</th>
			<th style="border: 1px solid black;">Explanation</th>
			<th style="border: 1px solid black;">Answer</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">`[3, 4]`</td>
			<td style="border: 1px solid black;">`3 → 1 → 0 → 2 → 4`</td>
			<td style="border: 1px solid black;">`[1, 2, 5, 3]`</td>
			<td style="border: 1px solid black;">11</td>
			<td style="border: 1px solid black;">5.5</td>
			<td style="border: 1px solid black;">Sum from `3 → 1 = 1 < 5.5`.

			Sum from `3 → 0 = 1 + 2 = 3 < 5.5`.

			Sum from `3 → 2 = 1 + 2 + 5 = 8 >= 5.5`, median is node 2.</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[1, 2]`</td>
			<td style="border: 1px solid black;">`1 → 0 → 2`</td>
			<td style="border: 1px solid black;">`[2, 5]`</td>
			<td style="border: 1px solid black;">7</td>
			<td style="border: 1px solid black;">3.5</td>
			<td style="border: 1px solid black;">
			Sum from `1 → 0 = 2 < 3.5`.

			Sum from `1 → 2 = 2 + 5 = 7 >= 3.5`, median is node 2.

			</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
	</tbody>
</table>
</div>

**Constraints:**

	- `2 <= n <= 10^5`

	- `edges.length == n - 1`

	- `edges[i] == [u_i, v_i, w_i]`

	- `0 <= u_i, v_i < n`

	- `1 <= w_i <= 10^9`

	- `1 <= queries.length <= 10^5`

	- `queries[j] == [u_j, v_j]`

	- `0 <= u_j, v_j < n`

	- The input is generated such that `edges` represents a valid tree.
