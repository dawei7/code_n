## Description

You are given an integer array `nums`, an integer `k`, and an integer `multiplier`.

You need to perform `k` operations on `nums`. In each operation:

	- Find the **minimum** value `x` in `nums`. If there are multiple occurrences of the minimum value, select the one that appears **first**.

	- Replace the selected minimum value `x` with `x * multiplier`.

After the `k` operations, apply **modulo** `10^9 + 7` to every value in `nums`.

Return an integer array denoting the *final state* of `nums` after performing all `k` operations and then applying the modulo.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,1,3,5,6], k = 5, multiplier = 2</span>

**Output:** <span class="example-io">[8,4,6,5,6]</span>

**Explanation:**

<table>
	<tbody>
		<tr>
			<th>Operation</th>
			<th>Result</th>
		</tr>
		<tr>
			<td>After operation 1</td>
			<td>[2, 2, 3, 5, 6]</td>
		</tr>
		<tr>
			<td>After operation 2</td>
			<td>[4, 2, 3, 5, 6]</td>
		</tr>
		<tr>
			<td>After operation 3</td>
			<td>[4, 4, 3, 5, 6]</td>
		</tr>
		<tr>
			<td>After operation 4</td>
			<td>[4, 4, 6, 5, 6]</td>
		</tr>
		<tr>
			<td>After operation 5</td>
			<td>[8, 4, 6, 5, 6]</td>
		</tr>
		<tr>
			<td>After applying modulo</td>
			<td>[8, 4, 6, 5, 6]</td>
		</tr>
	</tbody>
</table>
</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [100000,2000], k = 2, multiplier = 1000000</span>

**Output:** <span class="example-io">[999999307,999999993]</span>

**Explanation:**

<table>
	<tbody>
		<tr>
			<th>Operation</th>
			<th>Result</th>
		</tr>
		<tr>
			<td>After operation 1</td>
			<td>[100000, 2000000000]</td>
		</tr>
		<tr>
			<td>After operation 2</td>
			<td>[100000000000, 2000000000]</td>
		</tr>
		<tr>
			<td>After applying modulo</td>
			<td>[999999307, 999999993]</td>
		</tr>
	</tbody>
</table>
</div>

**Constraints:**

	- `1 <= nums.length <= 10^4`

	- `1 <= nums[i] <= 10^9`

	- `1 <= k <= 10^9`

	- `1 <= multiplier <= 10^6`
