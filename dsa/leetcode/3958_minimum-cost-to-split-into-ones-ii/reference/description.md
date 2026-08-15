### 1. Description

You are given an integer `n`.

In one operation, you may split an integer `x` into two positive integers `a` and `b` such that $a + b = x$.

The cost of this operation is $a * b$.

Return the **minimum** total cost required to split the integer `n` into `n` ones.

### 2. Function Contract

**Inputs**

- `n`: The positive integer initially present before any split.

Every split must produce two positive integers, so neither part may be zero.

**Return value**

Return the minimum possible sum of operation costs after every remaining piece equals one. The result can exceed the range of a signed 32-bit integer.

### 3. Examples

#### Example 1

- **Input:** n = 3

- **Output:** 3

- **Explanation:** One optimal set of operations is:

<table border="1" bordercolor="#ccc" cellpadding="5" cellspacing="0" style="border-collapse:collapse;">
	<tbody>
		<tr>
			<th>`x`</th>
			<th>`a`</th>
			<th>`b`</th>
			<th>$a + b$</th>
			<th>$a * b$</th>
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

Thus, the minimum total cost is $2 + 1 = 3$.

#### Example 2

- **Input:** n = 4

- **Output:** 6

- **Explanation:** ​​​​​​​**

One optimal set of operations is:

<table border="1" bordercolor="#ccc" cellpadding="5" cellspacing="0" style="border-collapse:collapse;">
	<tbody>
		<tr>
			<th>`x`</th>
			<th>`a`</th>
			<th>`b`</th>
			<th>$a + b$</th>
			<th>$a * b$</th>
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

Thus, the minimum total cost is $4 + 1 + 1 = 6$.

### 4. Constraints

- $1 \le n \le 5 * 10^{7}$
