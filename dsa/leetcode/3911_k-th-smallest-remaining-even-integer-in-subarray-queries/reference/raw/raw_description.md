## Description

You are given an integer array `nums` where `nums` is **<span data-keyword="strictly-increasing-array">strictly increasing</span>**.

You are also given a 2D integer array `queries`, where `queries[i] = [l_i, r_i, k_i]`.

For each query `[l_i, r_i, k_i]`:

	- Consider the **<span data-keyword="subarray-nonempty">subarray</span>** `nums[l_i..r_i]`

	- From the **infinite** sequence of all **positive even integers**: `2, 4, 6, 8, 10, 12, 14, ...`

	- **Remove** all elements that appear in the **subarray** `nums[l_i..r_i]`.

	- Find the `k_i^th` **smallest integer** remaining in the sequence after the removals.

Return an integer array `ans`, where `ans[i]` is the result for the `i^th` query.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,4,7], queries = [[0,2,1],[1,1,2],[0,0,3]]</span>

**Output:** <span class="example-io">[2,6,6]</span>

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">`queries[i]`</th>
			<th style="border: 1px solid black;">`nums[l_i..r_i]`</th>
			<th style="border: 1px solid black;">Removed

			Evens</th>
			<th style="border: 1px solid black;">Remaining

			Evens</th>
			<th style="border: 1px solid black;">`k_i`</th>
			<th style="border: 1px solid black;">`ans[i]`</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">[0, 2, 1]</td>
			<td style="border: 1px solid black;">[1, 4, 7]</td>
			<td style="border: 1px solid black;">[4]</td>
			<td style="border: 1px solid black;">2, 6, 8, ...</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[1, 1, 2]</td>
			<td style="border: 1px solid black;">[4]</td>
			<td style="border: 1px solid black;">[4]</td>
			<td style="border: 1px solid black;">2, 6, 8, ...</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">6</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">[0, 0, 3]</td>
			<td style="border: 1px solid black;">[1]</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">2, 4, 6, ...</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">6</td>
		</tr>
	</tbody>
</table>

Thus, `ans = [2, 6, 6]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,5,8], queries = [[0,1,2],[1,2,1],[0,2,4]]</span>

**Output:** <span class="example-io">[6,2,12]</span>

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">`queries[i]`</th>
			<th style="border: 1px solid black;">`nums[l_i..r_i]`</th>
			<th style="border: 1px solid black;">Removed

			Evens</th>
			<th style="border: 1px solid black;">Remaining

			Evens</th>
			<th style="border: 1px solid black;">`k_i`</th>
			<th style="border: 1px solid black;">`ans[i]`</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">[0, 1, 2]</td>
			<td style="border: 1px solid black;">[2, 5]</td>
			<td style="border: 1px solid black;">[2]</td>
			<td style="border: 1px solid black;">4, 6, 8, ...</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">6</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[1, 2, 1]</td>
			<td style="border: 1px solid black;">[5, 8]</td>
			<td style="border: 1px solid black;">[8]</td>
			<td style="border: 1px solid black;">2, 4, 6, ...</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">[0, 2, 4]</td>
			<td style="border: 1px solid black;">[2, 5, 8]</td>
			<td style="border: 1px solid black;">[2, 8]</td>
			<td style="border: 1px solid black;">4, 6, 10, 12, ...</td>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">12</td>
		</tr>
	</tbody>
</table>

Thus, `ans = [6, 2, 12]`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,6], queries = [[0,1,1],[1,1,3]]</span>

**Output:** <span class="example-io">[2,8]</span>

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">`queries[i]`</th>
			<th style="border: 1px solid black;">`nums[l_i..r_i]`</th>
			<th style="border: 1px solid black;">Removed

			Evens</th>
			<th style="border: 1px solid black;">Remaining

			Evens</th>
			<th style="border: 1px solid black;">`k_i`</th>
			<th style="border: 1px solid black;">`ans[i]`</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">[0, 1, 1]</td>
			<td style="border: 1px solid black;">[3, 6]</td>
			<td style="border: 1px solid black;">[6]</td>
			<td style="border: 1px solid black;">2, 4, 8, ...</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[1, 1, 3]</td>
			<td style="border: 1px solid black;">[6]</td>
			<td style="border: 1px solid black;">[6]</td>
			<td style="border: 1px solid black;">2, 4, 8, ...</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">8</td>
		</tr>
	</tbody>
</table>

Thus, `ans = [2, 8]`.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`

	- `nums` is strictly increasing

	- `1 <= queries.length <= 10^5`

	- `queries[i] = [l_i, r_i, k_i]`

	- `0 <= l_i <= r_i < nums.length`

	- `1 <= k_i <= 10^9`​​​​​​​
