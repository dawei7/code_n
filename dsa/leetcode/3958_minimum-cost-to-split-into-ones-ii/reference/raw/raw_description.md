## Description

You are given an integer `n`.

In one operation, you may split an integer `x` into two positive integers `a` and `b` such that `a + b = x`.

The cost of this operation is `a * b`.

Return the **minimum** total cost required to split the integer `n` into `n` ones.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 3</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

One optimal set of operations is:

<table border="1" bordercolor="#ccc" cellpadding="5" cellspacing="0" style="border-collapse:collapse;">
	<tbody>
		<tr>
			<th>`x`</th>
			<th>`a`</th>
			<th>`b`</th>
			<th>`a + b`</th>
			<th>`a * b`</th>
			<th>Cost</th>
		</tr>
		<tr>
			<td>3</td>
			<td>1</td>
			<td>2</td>
			<td>3</td>
			<td>2</td>
			<td>2</td>
		</tr>
		<tr>
			<td>2</td>
			<td>1</td>
			<td>1</td>
			<td>2</td>
			<td>1</td>
			<td>1</td>
		</tr>
	</tbody>
</table>

Thus, the minimum total cost is `2 + 1 = 3`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 4</span>

**Output:** <span class="example-io">6</span>

**Explanation:​​​​​​​**

One optimal set of operations is:

<table border="1" bordercolor="#ccc" cellpadding="5" cellspacing="0" style="border-collapse:collapse;">
	<tbody>
		<tr>
			<th>`x`</th>
			<th>`a`</th>
			<th>`b`</th>
			<th>`a + b`</th>
			<th>`a * b`</th>
			<th>Cost</th>
		</tr>
		<tr>
			<td>4</td>
			<td>2</td>
			<td>2</td>
			<td>4</td>
			<td>4</td>
			<td>4</td>
		</tr>
		<tr>
			<td>2</td>
			<td>1</td>
			<td>1</td>
			<td>2</td>
			<td>1</td>
			<td>1</td>
		</tr>
	</tbody>
</table>

Thus, the minimum total cost is `4 + 1 + 1 = 6`.

</div>

**Constraints:**

	- `1 <= n <= 5 * 10^7`
