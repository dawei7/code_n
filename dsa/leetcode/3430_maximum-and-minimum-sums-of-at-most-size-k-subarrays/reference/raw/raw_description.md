## Description

You are given an integer array `nums` and a **positive** integer `k`. Return the sum of the **maximum** and **minimum** elements of all <span data-keyword="subarray-nonempty">subarrays</span> with **at most** `k` elements.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3], k = 2</span>

**Output:** <span class="example-io">20</span>

**Explanation:**

The subarrays of `nums` with at most 2 elements are:

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">**Subarray**</th>
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
			<td style="border: 1px solid black;">`[2, 3]`</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">5</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">**Final Total**</td>
			<td style="border: 1px solid black;"> </td>
			<td style="border: 1px solid black;"> </td>
			<td style="border: 1px solid black;">20</td>
		</tr>
	</tbody>
</table>

The output would be 20.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,-3,1], k = 2</span>

**Output:** <span class="example-io">-6</span>

**Explanation:**

The subarrays of `nums` with at most 2 elements are:

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">**Subarray**</th>
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
			<td style="border: 1px solid black;">`[-3]`</td>
			<td style="border: 1px solid black;">-3</td>
			<td style="border: 1px solid black;">-3</td>
			<td style="border: 1px solid black;">-6</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[1]`</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[1, -3]`</td>
			<td style="border: 1px solid black;">-3</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">-2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[-3, 1]`</td>
			<td style="border: 1px solid black;">-3</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">-2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">**Final Total**</td>
			<td style="border: 1px solid black;"> </td>
			<td style="border: 1px solid black;"> </td>
			<td style="border: 1px solid black;">-6</td>
		</tr>
	</tbody>
</table>

The output would be -6.

</div>

**Constraints:**

	- `1 <= nums.length <= 80000`

	- `1 <= k <= nums.length`

	- `-10^6 <= nums[i] <= 10^6`
