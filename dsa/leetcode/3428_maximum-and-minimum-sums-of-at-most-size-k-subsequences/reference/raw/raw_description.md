## Description

You are given an integer array `nums` and a positive integer `k`. Return the sum of the **maximum** and **minimum** elements of all **<span data-keyword="subsequence-sequence-nonempty">subsequences</span>** of `nums` with **at most** `k` elements.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3], k = 2</span>

**Output:** 24

**Explanation:**

The subsequences of `nums` with at most 2 elements are:

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">**Subsequence **</th>
			<th style="border: 1px solid black;">Minimum</th>
			<th style="border: 1px solid black;">Maximum</th>
			<th style="border: 1px solid black;">Sum</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[1]`</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[2]`</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">4</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[3]`</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">6</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[1, 2]`</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[1, 3]`</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">4</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[2, 3]`</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">5</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">**Final Total**</td>
			<td style="border: 1px solid black;"> </td>
			<td style="border: 1px solid black;"> </td>
			<td style="border: 1px solid black;">24</td>
		</tr>
	</tbody>
</table>

The output would be 24.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,0,6], k = 1</span>

**Output:** 2<span class="example-io">2</span>

**Explanation: **

For subsequences with exactly 1 element, the minimum and maximum values are the element itself. Therefore, the total is `5 + 5 + 0 + 0 + 6 + 6 = 22`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,1,1], k = 2</span>

**Output:** 12

**Explanation:**

The subsequences `[1, 1]` and `[1]` each appear 3 times. For all of them, the minimum and maximum are both 1. Thus, the total is 12.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `0 <= nums[i] <= 10^9`

	- `<font face="monospace">1 <= k <= min(70, nums.length)</font>`
