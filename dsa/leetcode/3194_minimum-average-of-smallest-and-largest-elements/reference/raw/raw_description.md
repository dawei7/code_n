## Description

You have an array of floating point numbers `averages` which is initially empty. You are given an array `nums` of `n` integers where `n` is even.

You repeat the following procedure `n / 2` times:

	- Remove the **smallest** element, `minElement`, and the **largest** element `maxElement`, from `nums`.

	- Add `(minElement + maxElement) / 2` to `averages`.

Return the **minimum** element in `averages`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [7,8,3,4,15,13,4,1]</span>

**Output:** <span class="example-io">5.5</span>

**Explanation:**

<table>
	<tbody>
		<tr>
			<th>step</th>
			<th>nums</th>
			<th>averages</th>
		</tr>
		<tr>
			<td>0</td>
			<td>[7,8,3,4,15,13,4,1]</td>
			<td>[]</td>
		</tr>
		<tr>
			<td>1</td>
			<td>[7,8,3,4,13,4]</td>
			<td>[8]</td>
		</tr>
		<tr>
			<td>2</td>
			<td>[7,8,4,4]</td>
			<td>[8,8]</td>
		</tr>
		<tr>
			<td>3</td>
			<td>[7,4]</td>
			<td>[8,8,6]</td>
		</tr>
		<tr>
			<td>4</td>
			<td>[]</td>
			<td>[8,8,6,5.5]</td>
		</tr>
	</tbody>
</table>
The smallest element of averages, 5.5, is returned.</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,9,8,3,10,5]</span>

**Output:** <span class="example-io">5.5</span>

**Explanation:**

<table>
	<tbody>
		<tr>
			<th>step</th>
			<th>nums</th>
			<th>averages</th>
		</tr>
		<tr>
			<td>0</td>
			<td><span class="example-io">[1,9,8,3,10,5]</span></td>
			<td>[]</td>
		</tr>
		<tr>
			<td>1</td>
			<td><span class="example-io">[9,8,3,5]</span></td>
			<td>[5.5]</td>
		</tr>
		<tr>
			<td>2</td>
			<td><span class="example-io">[8,5]</span></td>
			<td>[5.5,6]</td>
		</tr>
		<tr>
			<td>3</td>
			<td>[]</td>
			<td>[5.5,6,6.5]</td>
		</tr>
	</tbody>
</table>
</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,7,8,9]</span>

**Output:** <span class="example-io">5.0</span>

**Explanation:**

<table>
	<tbody>
		<tr>
			<th>step</th>
			<th>nums</th>
			<th>averages</th>
		</tr>
		<tr>
			<td>0</td>
			<td><span class="example-io">[1,2,3,7,8,9]</span></td>
			<td>[]</td>
		</tr>
		<tr>
			<td>1</td>
			<td><span class="example-io">[2,3,7,8]</span></td>
			<td>[5]</td>
		</tr>
		<tr>
			<td>2</td>
			<td><span class="example-io">[3,7]</span></td>
			<td>[5,5]</td>
		</tr>
		<tr>
			<td>3</td>
			<td><span class="example-io">[]</span></td>
			<td>[5,5,5]</td>
		</tr>
	</tbody>
</table>
</div>

**Constraints:**

	- `2 <= n == nums.length <= 50`

	- `n` is even.

	- `1 <= nums[i] <= 50`
