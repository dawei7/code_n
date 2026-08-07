## Description

You are given an integer array `nums` and an integer `k`.

For every **subarray** of length `k`:

	- The **mode** is defined as the element with the **highest frequency**. If there are multiple choices for a mode, the **smallest** such element is taken.

	- The **weight** is defined as `mode * frequency(mode)`.

Return the **sum** of the weights of all **subarrays** of length `k`.

**Note:**

	- A **subarray** is a contiguous **non-empty** sequence of elements within an array.

	- The **frequency** of an element `x` is the number of times it occurs in the array.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,2,3], k = 3</span>

**Output:** <span class="example-io">8</span>

**Explanation:**

Subarrays of length `k = 3` are:

<table border="1" bordercolor="#ccc" cellpadding="5" cellspacing="0" style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Subarray</th>
			<th style="border: 1px solid black;">Frequencies</th>
			<th style="border: 1px solid black;">Mode</th>
			<th style="border: 1px solid black;">Mode

			​​​​​​​Frequency</th>
			<th style="border: 1px solid black;">Weight</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">[1, 2, 2]</td>
			<td style="border: 1px solid black;">1: 1, 2: 2</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2 × 2 = 4</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">[2, 2, 3]</td>
			<td style="border: 1px solid black;">2: 2, 3: 1</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2 × 2 = 4</td>
		</tr>
	</tbody>
</table>

Thus, the sum of weights is `4 + 4 = 8`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,1,2], k = 2</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

Subarrays of length `k = 2` are:

<table border="1" bordercolor="#ccc" cellpadding="5" cellspacing="0" style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Subarray</th>
			<th style="border: 1px solid black;">Frequencies</th>
			<th style="border: 1px solid black;">Mode</th>
			<th style="border: 1px solid black;">Mode

			Frequency</th>
			<th style="border: 1px solid black;">Weight</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">[1, 2]</td>
			<td style="border: 1px solid black;">1: 1, 2: 1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1 × 1 = 1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">[2, 1]</td>
			<td style="border: 1px solid black;">2: 1, 1: 1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1 × 1 = 1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">[1, 2]</td>
			<td style="border: 1px solid black;">1: 1, 2: 1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1 × 1 = 1</td>
		</tr>
	</tbody>
</table>

Thus, the sum of weights is `1 + 1 + 1 = 3`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,3,4,3], k = 3</span>

**Output:** <span class="example-io">14</span>

**Explanation:**

Subarrays of length `k = 3` are:

<table border="1" bordercolor="#ccc" cellpadding="5" cellspacing="0" style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Subarray</th>
			<th style="border: 1px solid black;">Frequencies</th>
			<th style="border: 1px solid black;">Mode</th>
			<th style="border: 1px solid black;">Mode

			Frequency</th>
			<th style="border: 1px solid black;">Weight</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">[4, 3, 4]</td>
			<td style="border: 1px solid black;">4: 2, 3: 1</td>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2 × 4 = 8</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">[3, 4, 3]</td>
			<td style="border: 1px solid black;">3: 2, 4: 1</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2 × 3 = 6</td>
		</tr>
	</tbody>
</table>

Thus, the sum of weights is `8 + 6 = 14`.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^5`

	- `1 <= k <= nums.length`
