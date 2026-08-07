## Description

You are given a `m x n` matrix `mat` of positive integers.

Return an integer denoting the number of ways to choose **exactly one** integer from each row of `mat` such that the **greatest common divisor** of all chosen integers is 1.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">mat = [[1,2],[3,4]]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th align="center" style="border: 1px solid black;">Chosen integer in the first row</th>
			<th align="center" style="border: 1px solid black;">Chosen integer in the second row</th>
			<th align="center" style="border: 1px solid black;">Greatest common divisor of chosen integers</th>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">3</td>
			<td align="center" style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">4</td>
			<td align="center" style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">3</td>
			<td align="center" style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">4</td>
			<td align="center" style="border: 1px solid black;">2</td>
		</tr>
	</tbody>
</table>

3 of these combinations have a greatest common divisor of 1. Therefore, the answer is 3.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">mat = [[2,2],[2,2]]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

Every combination has a greatest common divisor of 2. Therefore, the answer is 0.

</div>

**Constraints:**

	- `1 <= m == mat.length <= 150`

	- `1 <= n == mat[i].length <= 150`

	- `1 <= mat[i][j] <= 150`
