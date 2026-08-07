## Description

You are given an integer array `nums`.

Split the array into **exactly** two <span data-keyword="subarray-nonempty">subarrays</span>, `left` and `right`, such that `left` is **<span data-keyword="strictly-increasing-array">strictly increasing</span> ** and `right` is **<span data-keyword="strictly-decreasing-array">strictly decreasing</span>**.

Return the **minimum possible absolute difference** between the sums of `left` and `right`. If no valid split exists, return `-1`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,3,2]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">`left`</th>
			<th style="border: 1px solid black;">`right`</th>
			<th style="border: 1px solid black;">Validity</th>
			<th style="border: 1px solid black;">`left` sum</th>
			<th style="border: 1px solid black;">`right` sum</th>
			<th style="border: 1px solid black;">Absolute difference</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">[1]</td>
			<td style="border: 1px solid black;">[3, 2]</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">5</td>
			<td style="border: 1px solid black;">`|1 - 5| = 4`</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[1, 3]</td>
			<td style="border: 1px solid black;">[2]</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">`|4 - 2| = 2`</td>
		</tr>
	</tbody>
</table>

Thus, the minimum absolute difference is 2.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,4,3]</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">`left`</th>
			<th style="border: 1px solid black;">`right`</th>
			<th style="border: 1px solid black;">Validity</th>
			<th style="border: 1px solid black;">`left` sum</th>
			<th style="border: 1px solid black;">`right` sum</th>
			<th style="border: 1px solid black;">Absolute difference</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">[1]</td>
			<td style="border: 1px solid black;">[2, 4, 3]</td>
			<td style="border: 1px solid black;">No</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">9</td>
			<td style="border: 1px solid black;">-</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[1, 2]</td>
			<td style="border: 1px solid black;">[4, 3]</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">7</td>
			<td style="border: 1px solid black;">`|3 - 7| = 4`</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">[1, 2, 4]</td>
			<td style="border: 1px solid black;">[3]</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">7</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">`|7 - 3| = 4`</td>
		</tr>
	</tbody>
</table>

Thus, the minimum absolute difference is 4.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,1,2]</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

No valid split exists, so the answer is -1.

</div>

**Constraints:**

	- `2 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^5`
