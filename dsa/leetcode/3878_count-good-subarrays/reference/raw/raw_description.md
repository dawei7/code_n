## Description

You are given an integer array `nums`.

A **<span data-keyword="subarray-nonempty">subarray</span>** is called **good** if the **bitwise OR** of all its elements is equal to **at least one** element present in that subarray.

Return the number of good subarrays in `nums`.

Here, the bitwise OR of two integers `a` and `b` is denoted by `a | b`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,2,3]</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

The subarrays of `nums` are:

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Subarray</th>
			<th style="border: 1px solid black;">Bitwise OR</th>
			<th style="border: 1px solid black;">Present in Subarray</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[4]`</td>
			<td style="border: 1px solid black;">`4 = 4`</td>
			<td style="border: 1px solid black;">Yes</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[2]`</td>
			<td style="border: 1px solid black;">`2 = 2`</td>
			<td style="border: 1px solid black;">Yes</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[3]`</td>
			<td style="border: 1px solid black;">`3 = 3`</td>
			<td style="border: 1px solid black;">Yes</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[4, 2]`</td>
			<td style="border: 1px solid black;">`4 | 2 = 6`</td>
			<td style="border: 1px solid black;">No</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[2, 3]`</td>
			<td style="border: 1px solid black;">`2 | 3 = 3`</td>
			<td style="border: 1px solid black;">Yes</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[4, 2, 3]`</td>
			<td style="border: 1px solid black;">`4 | 2 | 3 = 7`</td>
			<td style="border: 1px solid black;">No</td>
		</tr>
	</tbody>
</table>

Thus, the good subarrays of `nums` are `[4]`, `[2]`, `[3]` and `[2, 3]`. Thus, the answer is 4.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,3,1]</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

Any subarray of `nums` containing 3 has bitwise OR equal to 3, and subarrays containing only 1 have bitwise OR equal to 1.

In both cases, the result is present in the subarray, so all subarrays are good, and the answer is 6.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `0 <= nums[i] <= 10^9`
