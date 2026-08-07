## Description

You are given an integer array `nums` of length `n` and an integer `k`.

For each index `i`, define the **delayed count** as the number of indices `j` such that:

	- `i + k < j <= n - 1`, and

	- `nums[j] == nums[i]`

Return an array `ans` where `ans[i]` is the **delayed count** of index `i`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,1,1], k = 1</span>

**Output:** <span class="example-io">[2,0,0,0]</span>

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">`nums[i]`</th>
			<th style="border: 1px solid black;">possible `j`</th>
			<th style="border: 1px solid black;">`nums[j]`</th>
			<th style="border: 1px solid black;">satisfying

			`nums[j] == nums[i]`</th>
			<th style="border: 1px solid black;">`ans[i]`</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[2, 3]</td>
			<td style="border: 1px solid black;">[1, 1]</td>
			<td style="border: 1px solid black;">[2, 3]</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">[3]</td>
			<td style="border: 1px solid black;">[1]</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
	</tbody>
</table>

Thus, `ans = [2, 0, 0, 0]`​​​​​​​.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,1,3,1], k = 0</span>

**Output:** <span class="example-io">[1,1,0,0]</span>

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">`nums[i]`</th>
			<th style="border: 1px solid black;">possible `j`</th>
			<th style="border: 1px solid black;">`nums[j]`</th>
			<th style="border: 1px solid black;">satisfying

			`nums[j] == nums[i]`</th>
			<th style="border: 1px solid black;">`ans[i]`</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">[1, 2, 3]</td>
			<td style="border: 1px solid black;">[1, 3, 1]</td>
			<td style="border: 1px solid black;">[2]</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[2, 3]</td>
			<td style="border: 1px solid black;">[3, 1]</td>
			<td style="border: 1px solid black;">[3]</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">[3]</td>
			<td style="border: 1px solid black;">[1]</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
	</tbody>
</table>

Thus, `ans = [1, 1, 0, 0]`​​​​​​​.

</div>

**Constraints:**

	- `1 <= n == nums.length <= 10^5`

	- `1 <= nums[i] <= 10^5`

	- `0 <= k <= n - 1`
