## Description

You are given an integer array `nums` of length `n` and an integer `p`.

A **non-empty <span data-keyword="subsequence-sequence">subsequence</span>** of `nums` is called **good** if:

	- Its length is **strictly less** than `n`.

	- The **greatest common divisor (GCD)** of its elements is **exactly** `p`.

You are also given a 2D integer array `queries` of length `q`, where each `queries[i] = [ind_i, val_i]` indicates that you should update `nums[ind_i]` to `val_i`.

After each query, determine whether there exists **any good subsequence** in the current array.

Return the **number** of queries for which a **good subsequence** exists.

The term `gcd(a, b)` denotes the **greatest common divisor** of `a` and `b`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,8,12,16], p = 2, queries = [[0,3],[2,6]]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">i</th>
			<th style="border: 1px solid black;">`[ind_i, val_i]`</th>
			<th style="border: 1px solid black;">Operation</th>
			<th style="border: 1px solid black;">Updated `nums`</th>
			<th style="border: 1px solid black;">Any good Subsequence</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">`[0, 3]`</td>
			<td style="border: 1px solid black;">Update `nums[0]` to `3`</td>
			<td style="border: 1px solid black;">`[3, 8, 12, 16]`</td>
			<td style="border: 1px solid black;">No, as no subsequence has GCD exactly `p = 2`</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">`[2, 6]`</td>
			<td style="border: 1px solid black;">Update `nums[2]` to `6`</td>
			<td style="border: 1px solid black;">`[3, 8, 6, 16]`</td>
			<td style="border: 1px solid black;">Yes, subsequence `[8, 6]` has GCD exactly `p = 2`</td>
		</tr>
	</tbody>
</table>

Thus, the answer is 1.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,5,7,8], p = 3, queries = [[0,6],[1,9],[2,3]]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">i</th>
			<th style="border: 1px solid black;">`[ind_i, val_i]`</th>
			<th style="border: 1px solid black;">Operation</th>
			<th style="border: 1px solid black;">Updated `nums`</th>
			<th style="border: 1px solid black;">Any good Subsequence</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">`[0, 6]`</td>
			<td style="border: 1px solid black;">Update `nums[0]` to `6`</td>
			<td style="border: 1px solid black;">`[6, 5, 7, 8]`</td>
			<td style="border: 1px solid black;">No, as no subsequence has GCD exactly `p = 3`</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">`[1, 9]`</td>
			<td style="border: 1px solid black;">Update `nums[1]` to `9`</td>
			<td style="border: 1px solid black;">`[6, 9, 7, 8]`</td>
			<td style="border: 1px solid black;">Yes, subsequence `[6, 9]` has GCD exactly `p = 3`</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">`[2, 3]`</td>
			<td style="border: 1px solid black;">Update `nums[2]` to `3`</td>
			<td style="border: 1px solid black;">`[6, 9, 3, 8]`</td>
			<td style="border: 1px solid black;">Yes, subsequence `[6, 9, 3]` has GCD exactly `p = 3`</td>
		</tr>
	</tbody>
</table>

Thus, the answer is 2.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,7,9], p = 2, queries = [[1,4],[2,8]]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">i</th>
			<th style="border: 1px solid black;">`[ind_i, val_i]`</th>
			<th style="border: 1px solid black;">Operation</th>
			<th style="border: 1px solid black;">Updated `nums`</th>
			<th style="border: 1px solid black;">Any good Subsequence</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">`[1, 4]`</td>
			<td style="border: 1px solid black;">Update `nums[1]` to `4`</td>
			<td style="border: 1px solid black;">`[5, 4, 9]`</td>
			<td style="border: 1px solid black;">No, as no subsequence has GCD exactly `p = 2`</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">`[2, 8]`</td>
			<td style="border: 1px solid black;">Update `nums[2]` to `8`</td>
			<td style="border: 1px solid black;">`[5, 4, 8]`</td>
			<td style="border: 1px solid black;">No, as no subsequence has GCD exactly `p = 2`</td>
		</tr>
	</tbody>
</table>

Thus, the answer is 0.

</div>

**Constraints:**

	- `2 <= n == nums.length <= 5 * 10^4`

	- `1 <= nums[i] <= 5 * 10^4`

	- `1 <= queries.length <= 5 * 10^4`

	- `queries[i] = [ind_i, val_i]`

	- `1 <= val_i, p <= 5 * 10^4`

	- `0 <= ind_i <= n - 1`
