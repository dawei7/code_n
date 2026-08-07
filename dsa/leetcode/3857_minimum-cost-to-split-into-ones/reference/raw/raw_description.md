## Description

You are given an integer `n`.

In one operation, you may split an integer `x` into two positive integers `a` and `b` such that `a + b = x`.

The cost of this operation is `a * b`.

Return an integer denoting the **minimum** total cost required to split the integer `n` into `n` ones.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 3</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

One optimal set of operations is:

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">`x`</th>
			<th style="border: 1px solid black;">`a`</th>
			<th style="border: 1px solid black;">`b`</th>
			<th style="border: 1px solid black;">`a + b`</th>
			<th style="border: 1px solid black;">`a * b`</th>
			<th style="border: 1px solid black;">Cost</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
	</tbody>
</table>

Thus, the minimum total cost is `2 + 1 = 3`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 4</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

<div class="example-block">
One optimal set of operations is:

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">`x`</th>
			<th style="border: 1px solid black;">`a`</th>
			<th style="border: 1px solid black;">`b`</th>
			<th style="border: 1px solid black;">`a + b`</th>
			<th style="border: 1px solid black;">`a * b`</th>
			<th style="border: 1px solid black;">Cost</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">4</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
	</tbody>
</table>

Thus, the minimum total cost is `4 + 1 + 1 = 6`.

</div>
</div>

**Constraints:**

	- `1 <= n <= 500`
