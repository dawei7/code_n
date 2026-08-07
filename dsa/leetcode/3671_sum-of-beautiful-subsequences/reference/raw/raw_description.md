## Description

You are given an integer array `nums` of length `n`.

For every **positive** integer `g`, we define the **beauty** of `g` as the **product** of `g` and the number of **strictly increasing** **<span data-keyword="subsequence-array-nonempty">subsequences</span>** of `nums` whose greatest common divisor (GCD) is exactly `g`.

Return the **sum** of **beauty** values for all positive integers `g`.

Since the answer could be very large, return it modulo `10^9 + 7`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3]</span>

**Output:** <span class="example-io">10</span>

**Explanation:**

All strictly increasing subsequences and their GCDs are:

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Subsequence</th>
			<th style="border: 1px solid black;">GCD</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">[1]</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">[2]</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">[3]</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">[1,2]</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">[1,3]</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">[2,3]</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">[1,2,3]</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
	</tbody>
</table>

Calculating beauty for each GCD:

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">GCD</th>
			<th style="border: 1px solid black;">Count of subsequences</th>
			<th style="border: 1px solid black;">Beauty (GCD × Count)</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">5</td>
			<td style="border: 1px solid black;">1 × 5 = 5</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">2 × 1 = 2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">3 × 1 = 3</td>
		</tr>
	</tbody>
</table>

Total beauty is `5 + 2 + 3 = 10`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,6]</span>

**Output:** <span class="example-io">12</span>

**Explanation:**

All strictly increasing subsequences and their GCDs are:

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Subsequence</th>
			<th style="border: 1px solid black;">GCD</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">[4]</td>
			<td style="border: 1px solid black;">4</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">[6]</td>
			<td style="border: 1px solid black;">6</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">[4,6]</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
	</tbody>
</table>

Calculating beauty for each GCD:

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">GCD</th>
			<th style="border: 1px solid black;">Count of subsequences</th>
			<th style="border: 1px solid black;">Beauty (GCD × Count)</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">2 × 1 = 2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">4 × 1 = 4</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">6</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">6 × 1 = 6</td>
		</tr>
	</tbody>
</table>

Total beauty is `2 + 4 + 6 = 12`.

</div>

**Constraints:**

	- `1 <= n == nums.length <= 10^4`

	- `1 <= nums[i] <= 7 * 10^4`
