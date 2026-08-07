## Description

You are given an integer array `nums` and an integer `k`.

In one operation, you can **increase or decrease **any element of `nums` by **exactly** `k`.

You are also given a 2D integer array `queries`, where each `queries[i] = [l_i, r_i]`.

For each query, find the **minimum** number of operations required to make **all** elements in the **<span data-keyword="subarray-nonempty">subarray</span>** `nums[l_i..r_i]` **equal**. If it is impossible, the answer for that query is `-1`.

Return an array `ans`, where `ans[i]` is the answer for the `i^th` query.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,4,7], k = 3, queries = [[0,1],[0,2]]</span>

**Output:** <span class="example-io">[1,2]</span>

**Explanation:**

One optimal set of operations:

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">`[l_i, r_i]`</th>
			<th style="border: 1px solid black;">`nums[l_i..r_i]`</th>
			<th style="border: 1px solid black;">Possibility</th>
			<th style="border: 1px solid black;">Operations</th>
			<th style="border: 1px solid black;">Final

			`nums[l_i..r_i]`</th>
			<th style="border: 1px solid black;">`ans[i]`</th>
		</tr>
	</tbody>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">[0, 1]</td>
			<td style="border: 1px solid black;">[1, 4]</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">`nums[0] + k = 1 + 3 = 4 = nums[1]`</td>
			<td style="border: 1px solid black;">[4, 4]</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[0, 2]</td>
			<td style="border: 1px solid black;">[1, 4, 7]</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">`nums[0] + k = 1 + 3 = 4 = nums[1]

			nums[2] - k = 7 - 3 = 4 = nums[1]`</td>
			<td style="border: 1px solid black;">[4, 4, 4]</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
	</tbody>
</table>

Thus, `ans = [1, 2]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,4], k = 2, queries = [[0,2],[0,0],[1,2]]</span>

**Output:** <span class="example-io">[-1,0,1]</span>

**Explanation:**

One optimal set of operations:

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">`[l_i, r_i]`</th>
			<th style="border: 1px solid black;">`nums[l_i..r_i]`</th>
			<th style="border: 1px solid black;">Possibility</th>
			<th style="border: 1px solid black;">Operations</th>
			<th style="border: 1px solid black;">Final

			`nums[l_i..r_i]`</th>
			<th style="border: 1px solid black;">`ans[i]`</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">[0, 2]</td>
			<td style="border: 1px solid black;">[1, 2, 4]</td>
			<td style="border: 1px solid black;">No</td>
			<td style="border: 1px solid black;">-</td>
			<td style="border: 1px solid black;">[1, 2, 4]</td>
			<td style="border: 1px solid black;">-1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[0, 0]</td>
			<td style="border: 1px solid black;">[1]</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">Already equal</td>
			<td style="border: 1px solid black;">[1]</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">[1, 2]</td>
			<td style="border: 1px solid black;">[2, 4]</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">`nums[1] + k = 2 + 2 = 4 = nums[2]`</td>
			<td style="border: 1px solid black;">[4, 4]</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
	</tbody>
</table>

Thus, `ans = [-1, 0, 1]`.

</div>

**Constraints:**

	- `1 <= n == nums.length <= 4 × 10^4`

	- `1 <= nums[i] <= 10^9`​​​​​​​

	- `1 <= k <= 10^9`

	- `1 <= queries.length <= 4 × 10^4`

	- `^​​​​​​​queries[i] = [l_i, r_i]`

	- `0 <= l_i <= r_i <= n - 1`
