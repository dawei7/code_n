## Description

You are given an integer array `nums`, and an integer `k`.

Start with an initial value `val = 1` and process `nums` from left to right. At each index `i`, you must choose **exactly one** of the following actions:

	- Multiply `val` by `nums[i]`.

	- Divide `val` by `nums[i]`.

	- Leave `val` unchanged.

After processing all elements, `val` is considered **equal** to `k` only if its final rational value **exactly** equals `k`.

Return the count of **distinct** sequences of choices that result in `val == k`.

**Note:** Division is rational (exact), not integer division. For example, `2 / 4 = 1 / 2`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,3,2], k = 6</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The following 2 distinct sequences of choices result in `val == k`:

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Sequence</th>
			<th style="border: 1px solid black;">Operation on `nums[0]`</th>
			<th style="border: 1px solid black;">Operation on `nums[1]`</th>
			<th style="border: 1px solid black;">Operation on `nums[2]`</th>
			<th style="border: 1px solid black;">Final `val`</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">Multiply: `val = 1 * 2 = 2`</td>
			<td style="border: 1px solid black;">Multiply: `val = 2 * 3 = 6`</td>
			<td style="border: 1px solid black;">Leave `val` unchanged</td>
			<td style="border: 1px solid black;">6</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">Leave `val` unchanged</td>
			<td style="border: 1px solid black;">Multiply: `val = 1 * 3 = 3`</td>
			<td style="border: 1px solid black;">Multiply: `val = 3 * 2 = 6`</td>
			<td style="border: 1px solid black;">6</td>
		</tr>
	</tbody>
</table>
</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,6,3], k = 2</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The following 2 distinct sequences of choices result in `val == k`:

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Sequence</th>
			<th style="border: 1px solid black;">Operation on `nums[0]`</th>
			<th style="border: 1px solid black;">Operation on `nums[1]`</th>
			<th style="border: 1px solid black;">Operation on `nums[2]`</th>
			<th style="border: 1px solid black;">Final `val`</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">Multiply: `val = 1 * 4 = 4`</td>
			<td style="border: 1px solid black;">Divide: `val = 4 / 6 = 2 / 3`</td>
			<td style="border: 1px solid black;">Multiply: `val = (2 / 3) * 3 = 2`</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">Leave `val` unchanged</td>
			<td style="border: 1px solid black;">Multiply: `val = 1 * 6 = 6`</td>
			<td style="border: 1px solid black;">Divide: `val = 6 / 3 = 2`</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
	</tbody>
</table>
</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,5], k = 1</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

The following 3 distinct sequences of choices result in `val == k`:

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Sequence</th>
			<th style="border: 1px solid black;">Operation on `nums[0]`</th>
			<th style="border: 1px solid black;">Operation on `nums[1]`</th>
			<th style="border: 1px solid black;">Final `val`</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">Multiply: `val = 1 * 1 = 1`</td>
			<td style="border: 1px solid black;">Leave `val` unchanged</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">Divide: `val = 1 / 1 = 1`</td>
			<td style="border: 1px solid black;">Leave `val` unchanged</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">Leave `val` unchanged</td>
			<td style="border: 1px solid black;">Leave `val` unchanged</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
	</tbody>
</table>
</div>

**Constraints:**

	- `1 <= nums.length <= 19`

	- `1 <= nums[i] <= 6`

	- `1 <= k <= 10^15`
