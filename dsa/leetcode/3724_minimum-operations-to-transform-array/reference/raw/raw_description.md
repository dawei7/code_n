## Description

You are given two integer arrays `nums1` of length `n` and `nums2` of length `n + 1`.

You want to transform `nums1` into `nums2` using the **minimum** number of operations.

You may perform the following operations **any** number of times, each time choosing an index `i`:

	- **Increase** `nums1[i]` by 1.

	- **Decrease** `nums1[i]` by 1.

	- **Append** `nums1[i]` to the **end** of the array.

Return the **minimum** number of operations required to transform `nums1` into `nums2`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums1 = [2,8], nums2 = [1,7,3]</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th align="center" style="border: 1px solid black;">Step</th>
			<th align="center" style="border: 1px solid black;">`i`</th>
			<th align="center" style="border: 1px solid black;">Operation</th>
			<th align="center" style="border: 1px solid black;">`nums1[i]`</th>
			<th align="center" style="border: 1px solid black;">Updated `nums1`</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">0</td>
			<td align="center" style="border: 1px solid black;">Append</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">[2, 8, 2]</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">0</td>
			<td align="center" style="border: 1px solid black;">Decrement</td>
			<td align="center" style="border: 1px solid black;">Decreases to 1</td>
			<td align="center" style="border: 1px solid black;">[1, 8, 2]</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">3</td>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">Decrement</td>
			<td align="center" style="border: 1px solid black;">Decreases to 7</td>
			<td align="center" style="border: 1px solid black;">[1, 7, 2]</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">4</td>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">Increment</td>
			<td align="center" style="border: 1px solid black;">Increases to 3</td>
			<td align="center" style="border: 1px solid black;">[1, 7, 3]</td>
		</tr>
	</tbody>
</table>

Thus, after 4 operations `nums1` is transformed into `nums2`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums1 = [1,3,6], nums2 = [2,4,5,3]</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th align="center" style="border: 1px solid black;">Step</th>
			<th align="center" style="border: 1px solid black;">`i`</th>
			<th align="center" style="border: 1px solid black;">Operation</th>
			<th align="center" style="border: 1px solid black;">`nums1[i]`</th>
			<th align="center" style="border: 1px solid black;">Updated `nums1`</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">Append</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">[1, 3, 6, 3]</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">0</td>
			<td align="center" style="border: 1px solid black;">Increment</td>
			<td align="center" style="border: 1px solid black;">Increases to 2</td>
			<td align="center" style="border: 1px solid black;">[2, 3, 6, 3]</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">3</td>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">Increment</td>
			<td align="center" style="border: 1px solid black;">Increases to 4</td>
			<td align="center" style="border: 1px solid black;">[2, 4, 6, 3]</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">4</td>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">Decrement</td>
			<td align="center" style="border: 1px solid black;">Decreases to 5</td>
			<td align="center" style="border: 1px solid black;">[2, 4, 5, 3]</td>
		</tr>
	</tbody>
</table>

Thus, after 4 operations `nums1` is transformed into `nums2`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums1 = [2], nums2 = [3,4]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th align="center" style="border: 1px solid black;">Step</th>
			<th align="center" style="border: 1px solid black;">`i`</th>
			<th align="center" style="border: 1px solid black;">Operation</th>
			<th align="center" style="border: 1px solid black;">`nums1[i]`</th>
			<th align="center" style="border: 1px solid black;">Updated `nums1`</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">0</td>
			<td align="center" style="border: 1px solid black;">Increment</td>
			<td align="center" style="border: 1px solid black;">Increases to 3</td>
			<td align="center" style="border: 1px solid black;">[3]</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">0</td>
			<td align="center" style="border: 1px solid black;">Append</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">[3, 3]</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">3</td>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">Increment</td>
			<td align="center" style="border: 1px solid black;">Increases to 4</td>
			<td align="center" style="border: 1px solid black;">[3, 4]</td>
		</tr>
	</tbody>
</table>

Thus, after 3 operations `nums1` is transformed into `nums2`.

</div>

**Constraints:**

	- `1 <= n == nums1.length <= 10^5`

	- `nums2.length == n + 1`

	- `1 <= nums1[i], nums2[i] <= 10^5`
