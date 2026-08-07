## Description

You are given an integer array `nums`.

For any positive integer `x`, define the following sequence:

	- `p_0 = x`

	- `p_i+1 = popcount(p_i)` for all `i >= 0`, where `popcount(y)` is the number of set bits (1's) in the binary representation of `y`.

This sequence will eventually reach the value 1.

The **popcount-depth** of `x` is defined as the **smallest** integer `d >= 0` such that `p_d = 1`.

For example, if `x = 7` (binary representation `"111"`). Then, the sequence is: `7 → 3 → 2 → 1`, so the popcount-depth of 7 is 3.

You are also given a 2D integer array `queries`, where each `queries[i]` is either:

	- `[1, l, r, k]` - **Determine** the number of indices `j` such that `l <= j <= r` and the **popcount-depth** of `nums[j]` is equal to `k`.

	- `[2, idx, val]` - **Update** `nums[idx]` to `val`.

Return an integer array `answer`, where `answer[i]` is the number of indices for the `i^th` query of type `[1, l, r, k]`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,4], queries = [[1,0,1,1],[2,1,1],[1,0,1,0]]</span>

**Output:** <span class="example-io">[2,1]</span>

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">`queries[i]`</th>
			<th style="border: 1px solid black;">`nums`</th>
			<th style="border: 1px solid black;">binary(`nums`)</th>
			<th style="border: 1px solid black;">popcount-

			depth</th>
			<th style="border: 1px solid black;">`[l, r]`</th>
			<th style="border: 1px solid black;">`k`</th>
			<th style="border: 1px solid black;">Valid

			`nums[j]`</th>
			<th style="border: 1px solid black;">updated

			`nums`</th>
			<th style="border: 1px solid black;">Answer</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">[1,0,1,1]</td>
			<td style="border: 1px solid black;">[2,4]</td>
			<td style="border: 1px solid black;">[10, 100]</td>
			<td style="border: 1px solid black;">[1, 1]</td>
			<td style="border: 1px solid black;">[0, 1]</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[0, 1]</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[2,1,1]</td>
			<td style="border: 1px solid black;">[2,4]</td>
			<td style="border: 1px solid black;">[10, 100]</td>
			<td style="border: 1px solid black;">[1, 1]</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">[2,1]</td>
			<td style="border: 1px solid black;">—</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">[1,0,1,0]</td>
			<td style="border: 1px solid black;">[2,1]</td>
			<td style="border: 1px solid black;">[10, 1]</td>
			<td style="border: 1px solid black;">[1, 0]</td>
			<td style="border: 1px solid black;">[0, 1]</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">[1]</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
	</tbody>
</table>

Thus, the final `answer` is `[2, 1]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,5,6], queries = [[1,0,2,2],[2,1,4],[1,1,2,1],[1,0,1,0]]</span>

**Output:** <span class="example-io">[3,1,0]</span>

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">`queries[i]`</th>
			<th style="border: 1px solid black;">`nums`</th>
			<th style="border: 1px solid black;">binary(`nums`)</th>
			<th style="border: 1px solid black;">popcount-

			depth</th>
			<th style="border: 1px solid black;">`[l, r]`</th>
			<th style="border: 1px solid black;">`k`</th>
			<th style="border: 1px solid black;">Valid

			`nums[j]`</th>
			<th style="border: 1px solid black;">updated

			`nums`</th>
			<th style="border: 1px solid black;">Answer</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">[1,0,2,2]</td>
			<td style="border: 1px solid black;">[3, 5, 6]</td>
			<td style="border: 1px solid black;">[11, 101, 110]</td>
			<td style="border: 1px solid black;">[2, 2, 2]</td>
			<td style="border: 1px solid black;">[0, 2]</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">[0, 1, 2]</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[2,1,4]</td>
			<td style="border: 1px solid black;">[3, 5, 6]</td>
			<td style="border: 1px solid black;">[11, 101, 110]</td>
			<td style="border: 1px solid black;">[2, 2, 2]</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">[3, 4, 6]</td>
			<td style="border: 1px solid black;">—</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">[1,1,2,1]</td>
			<td style="border: 1px solid black;">[3, 4, 6]</td>
			<td style="border: 1px solid black;">[11, 100, 110]</td>
			<td style="border: 1px solid black;">[2, 1, 2]</td>
			<td style="border: 1px solid black;">[1, 2]</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[1]</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">[1,0,1,0]</td>
			<td style="border: 1px solid black;">[3, 4, 6]</td>
			<td style="border: 1px solid black;">[11, 100, 110]</td>
			<td style="border: 1px solid black;">[2, 1, 2]</td>
			<td style="border: 1px solid black;">[0, 1]</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
	</tbody>
</table>

Thus, the final `answer` is `[3, 1, 0]`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2], queries = [[1,0,1,1],[2,0,3],[1,0,0,1],[1,0,0,2]]</span>

**Output:** <span class="example-io">[1,0,1]</span>

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">`queries[i]`</th>
			<th style="border: 1px solid black;">`nums`</th>
			<th style="border: 1px solid black;">binary(`nums`)</th>
			<th style="border: 1px solid black;">popcount-

			depth</th>
			<th style="border: 1px solid black;">`[l, r]`</th>
			<th style="border: 1px solid black;">`k`</th>
			<th style="border: 1px solid black;">Valid

			`nums[j]`</th>
			<th style="border: 1px solid black;">updated

			`nums`</th>
			<th style="border: 1px solid black;">Answer</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">[1,0,1,1]</td>
			<td style="border: 1px solid black;">[1, 2]</td>
			<td style="border: 1px solid black;">[1, 10]</td>
			<td style="border: 1px solid black;">[0, 1]</td>
			<td style="border: 1px solid black;">[0, 1]</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[1]</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[2,0,3]</td>
			<td style="border: 1px solid black;">[1, 2]</td>
			<td style="border: 1px solid black;">[1, 10]</td>
			<td style="border: 1px solid black;">[0, 1]</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">[3, 2]</td>
			<td style="border: 1px solid black;"> </td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">[1,0,0,1]</td>
			<td style="border: 1px solid black;">[3, 2]</td>
			<td style="border: 1px solid black;">[11, 10]</td>
			<td style="border: 1px solid black;">[2, 1]</td>
			<td style="border: 1px solid black;">[0, 0]</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">[1,0,0,2]</td>
			<td style="border: 1px solid black;">[3, 2]</td>
			<td style="border: 1px solid black;">[11, 10]</td>
			<td style="border: 1px solid black;">[2, 1]</td>
			<td style="border: 1px solid black;">[0, 0]</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">[0]</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
	</tbody>
</table>

Thus, the final `answer` is `[1, 0, 1]`.

</div>

**Constraints:**

	- `1 <= n == nums.length <= 10^5`

	- `1 <= nums[i] <= 10^15`

	- `1 <= queries.length <= 10^5`

	- `queries[i].length == 3` or `4`

		<li>`queries[i] == [1, l, r, k]` or,

		- `queries[i] == [2, idx, val]`

		- `0 <= l <= r <= n - 1`

		- `0 <= k <= 5`

		- `0 <= idx <= n - 1`

		- `1 <= val <= 10^15`

	</li>
