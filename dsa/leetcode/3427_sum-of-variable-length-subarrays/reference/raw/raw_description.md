## Description

You are given an integer array `nums` of size `n`. For **each** index `i` where `0 <= i < n`, define a <span data-keyword="subarray-nonempty">subarray</span> `nums[start ... i]` where `start = max(0, i - nums[i])`.

Return the total sum of all elements from the subarray defined for each index in the array.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,3,1]</span>

**Output:** <span class="example-io">11</span>

**Explanation:**

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">i</th>
			<th style="border: 1px solid black;">Subarray</th>
			<th style="border: 1px solid black;">Sum</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">`nums[0] = [2]`</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">`nums[0 ... 1] = [2, 3]`</td>
			<td style="border: 1px solid black;">5</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">`nums[1 ... 2] = [3, 1]`</td>
			<td style="border: 1px solid black;">4</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">**Total Sum**</td>
			<td style="border: 1px solid black;"> </td>
			<td style="border: 1px solid black;">11</td>
		</tr>
	</tbody>
</table>

The total sum is 11. Hence, 11 is the output.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,1,1,2]</span>

**Output:** <span class="example-io">13</span>

**Explanation:**

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">i</th>
			<th style="border: 1px solid black;">Subarray</th>
			<th style="border: 1px solid black;">Sum</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">`nums[0] = [3]`</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">`nums[0 ... 1] = [3, 1]`</td>
			<td style="border: 1px solid black;">4</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">`nums[1 ... 2] = [1, 1]`</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">`nums[1 ... 3] = [1, 1, 2]`</td>
			<td style="border: 1px solid black;">4</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">**Total Sum**</td>
			<td style="border: 1px solid black;"> </td>
			<td style="border: 1px solid black;">13</td>
		</tr>
	</tbody>
</table>

The total sum is 13. Hence, 13 is the output.

</div>

**Constraints:**

	- `1 <= n == nums.length <= 100`

	- `1 <= nums[i] <= 1000`
