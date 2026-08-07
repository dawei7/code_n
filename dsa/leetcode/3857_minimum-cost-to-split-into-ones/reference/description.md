### 1. Description

You are given an integer `n`.

In one operation, you may split an integer `x` into two positive integers `a` and `b` such that $a + b = x$.

The cost of this operation is $a * b$.

Return an integer denoting the **minimum** total cost required to split the integer `n` into `n` ones.

### 2. Function Contract

**Inputs**

- `n`: The positive integer that begins as the only current part.

Every operation chooses a part `x > 1` and positive integers `a` and `b` satisfying $a + b = x$. It replaces `x` by those two parts and adds $a * b$ to the running cost.

The process finishes only when its multiset of parts contains `n` copies of `1` and nothing else.

**Return value**

Return the minimum possible sum of all operation costs over a complete sequence of splits.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** n = 3

**Output:** 3

**Explanation:**

One optimal set of operations is:

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">`x`</th>
			<th style="border: 1px solid black;">`a`</th>
			<th style="border: 1px solid black;">`b`</th>
			<th style="border: 1px solid black;">$a + b$</th>
			<th style="border: 1px solid black;">$a * b$</th>
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

Thus, the minimum total cost is $2 + 1 = 3$.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 4

**Output:** 6

**Explanation:**

<div class="example-block">
One optimal set of operations is:

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">`x`</th>
			<th style="border: 1px solid black;">`a`</th>
			<th style="border: 1px solid black;">`b`</th>
			<th style="border: 1px solid black;">$a + b$</th>
			<th style="border: 1px solid black;">$a * b$</th>
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

Thus, the minimum total cost is $4 + 1 + 1 = 6$.

</div>
</div>

### 4. Constraints

- $1 \le n \le 500$