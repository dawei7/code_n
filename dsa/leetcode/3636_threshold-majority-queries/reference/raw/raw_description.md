## Description

You are given an integer array `nums` of length `n` and an array `queries`, where `queries[i] = [l_i, r_i, threshold_i]`.

Return an array of integers `ans` where `ans[i]` is equal to the element in the subarray `nums[l_i...r_i]` that appears **at least** `threshold_i` times, selecting the element with the **highest** frequency (choosing the **smallest** in case of a tie), or -1 if no such element *exists*.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,1,2,2,1,1], queries = [[0,5,4],[0,3,3],[2,3,2]]</span>

**Output:** <span class="example-io">[1,-1,2]</span>

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th align="left" style="border: 1px solid black;">Query</th>
			<th align="left" style="border: 1px solid black;">Sub-array</th>
			<th align="left" style="border: 1px solid black;">Threshold</th>
			<th align="left" style="border: 1px solid black;">Frequency table</th>
			<th align="left" style="border: 1px solid black;">Answer</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="left" style="border: 1px solid black;">[0, 5, 4]</td>
			<td align="left" style="border: 1px solid black;">[1, 1, 2, 2, 1, 1]</td>
			<td align="left" style="border: 1px solid black;">4</td>
			<td align="left" style="border: 1px solid black;">1 → 4, 2 → 2</td>
			<td align="left" style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td align="left" style="border: 1px solid black;">[0, 3, 3]</td>
			<td align="left" style="border: 1px solid black;">[1, 1, 2, 2]</td>
			<td align="left" style="border: 1px solid black;">3</td>
			<td align="left" style="border: 1px solid black;">1 → 2, 2 → 2</td>
			<td align="left" style="border: 1px solid black;">-1</td>
		</tr>
		<tr>
			<td align="left" style="border: 1px solid black;">[2, 3, 2]</td>
			<td align="left" style="border: 1px solid black;">[2, 2]</td>
			<td align="left" style="border: 1px solid black;">2</td>
			<td align="left" style="border: 1px solid black;">2 → 2</td>
			<td align="left" style="border: 1px solid black;">2</td>
		</tr>
	</tbody>
</table>
</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,2,3,2,3,2,3], queries = [[0,6,4],[1,5,2],[2,4,1],[3,3,1]]</span>

**Output:** <span class="example-io">[3,2,3,2]</span>

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th align="left" style="border: 1px solid black;">Query</th>
			<th align="left" style="border: 1px solid black;">Sub-array</th>
			<th align="left" style="border: 1px solid black;">Threshold</th>
			<th align="left" style="border: 1px solid black;">Frequency table</th>
			<th align="left" style="border: 1px solid black;">Answer</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="left" style="border: 1px solid black;">[0, 6, 4]</td>
			<td align="left" style="border: 1px solid black;">[3, 2, 3, 2, 3, 2, 3]</td>
			<td align="left" style="border: 1px solid black;">4</td>
			<td align="left" style="border: 1px solid black;">3 → 4, 2 → 3</td>
			<td align="left" style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td align="left" style="border: 1px solid black;">[1, 5, 2]</td>
			<td align="left" style="border: 1px solid black;">[2, 3, 2, 3, 2]</td>
			<td align="left" style="border: 1px solid black;">2</td>
			<td align="left" style="border: 1px solid black;">2 → 3, 3 → 2</td>
			<td align="left" style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td align="left" style="border: 1px solid black;">[2, 4, 1]</td>
			<td align="left" style="border: 1px solid black;">[3, 2, 3]</td>
			<td align="left" style="border: 1px solid black;">1</td>
			<td align="left" style="border: 1px solid black;">3 → 2, 2 → 1</td>
			<td align="left" style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td align="left" style="border: 1px solid black;">[3, 3, 1]</td>
			<td align="left" style="border: 1px solid black;">[2]</td>
			<td align="left" style="border: 1px solid black;">1</td>
			<td align="left" style="border: 1px solid black;">2 → 1</td>
			<td align="left" style="border: 1px solid black;">2</td>
		</tr>
	</tbody>
</table>
</div>

**Constraints:**

	- `1 <= nums.length == n <= 10^4`

	- `1 <= nums[i] <= 10^9`

	- `1 <= queries.length <= 5 * 10^4`

	- `queries[i] = [l_i, r_i, threshold_i]`

	- `0 <= l_i <= r_i < n`

	- `1 <= threshold_i <= r_i - l_i + 1`
