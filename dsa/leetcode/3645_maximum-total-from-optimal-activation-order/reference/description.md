### 1. Description

You are given two integer arrays `value` and `limit`, both of length `n`.

Initially, all elements are **inactive**. You may activate them in any order.

- To activate an inactive element at index `i`, the number of **currently** active elements must be **strictly less** than $\text{limit}[i]$.

- When you activate the element at index `i`, it adds $\text{value}[i]$ to the **total** activation value (i.e., the sum of $\text{value}[i]$ for all elements that have undergone activation operations).

- After each activation, if the number of **currently** active elements becomes `x`, then **all** elements `j` with $\text{limit}[j] \le x$ become **permanently** inactive, even if they are already active.

Return the **maximum** **total** you can obtain by choosing the activation order optimally.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** value = [3,5,8], limit = [2,1,3]

**Output:** 16

**Explanation:**

One optimal activation order is:

<table>
	<thead>
		<tr>
			<th align="center" style="border: 1px solid black;">Step</th>
			<th align="center" style="border: 1px solid black;">Activated `i`</th>
			<th align="center" style="border: 1px solid black;">$\text{value}[i]$</th>
			<th align="center" style="border: 1px solid black;">Active Before `i`</th>
			<th align="center" style="border: 1px solid black;">Active After `i`</th>
			<th align="center" style="border: 1px solid black;">Becomes Inactive `j`</th>
			<th align="center" style="border: 1px solid black;">Inactive Elements</th>
			<th align="center" style="border: 1px solid black;">Total</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">5</td>
			<td align="center" style="border: 1px solid black;">0</td>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">$j = 1$ as $\text{limit}[1] = 1$</td>
			<td align="center" style="border: 1px solid black;">[1]</td>
			<td align="center" style="border: 1px solid black;">5</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">0</td>
			<td align="center" style="border: 1px solid black;">3</td>
			<td align="center" style="border: 1px solid black;">0</td>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">[1]</td>
			<td align="center" style="border: 1px solid black;">8</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">3</td>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">8</td>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">$j = 0$ as $\text{limit}[0] = 2$</td>
			<td align="center" style="border: 1px solid black;">[0, 1]</td>
			<td align="center" style="border: 1px solid black;">16</td>
		</tr>
	</tbody>
</table>

Thus, the maximum possible total is 16.

</div>
#### Example 2

<div class="example-block">
**Input:** value = [4,2,6], limit = [1,1,1]

**Output:** 6

**Explanation:**

One optimal activation order is:

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th align="center" style="border: 1px solid black;">Step</th>
			<th align="center" style="border: 1px solid black;">Activated `i`</th>
			<th align="center" style="border: 1px solid black;">$\text{value}[i]$</th>
			<th align="center" style="border: 1px solid black;">Active Before `i`</th>
			<th align="center" style="border: 1px solid black;">Active After `i`</th>
			<th align="center" style="border: 1px solid black;">Becomes Inactive `j`</th>
			<th align="center" style="border: 1px solid black;">Inactive Elements</th>
			<th align="center" style="border: 1px solid black;">Total</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">6</td>
			<td align="center" style="border: 1px solid black;">0</td>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">$j = 0, 1, 2$ as $\text{limit}[j] = 1$</td>
			<td align="center" style="border: 1px solid black;">[0, 1, 2]</td>
			<td align="center" style="border: 1px solid black;">6</td>
		</tr>
	</tbody>
</table>

Thus, the maximum possible total is 6.

</div>
#### Example 3

<div class="example-block">
**Input:** value = [4,1,5,2], limit = [3,3,2,3]

**Output:** 12

**Explanation:**

One optimal activation order is:​​​​​​​**​​​​​​​**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th align="center" style="border: 1px solid black;">Step</th>
			<th align="center" style="border: 1px solid black;">Activated `i`</th>
			<th align="center" style="border: 1px solid black;">$\text{value}[i]$</th>
			<th align="center" style="border: 1px solid black;">Active Before `i`</th>
			<th align="center" style="border: 1px solid black;">Active After `i`</th>
			<th align="center" style="border: 1px solid black;">Becomes Inactive `j`</th>
			<th align="center" style="border: 1px solid black;">Inactive Elements</th>
			<th align="center" style="border: 1px solid black;">Total</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">5</td>
			<td align="center" style="border: 1px solid black;">0</td>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">[ ]</td>
			<td align="center" style="border: 1px solid black;">5</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">0</td>
			<td align="center" style="border: 1px solid black;">4</td>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">$j = 2$ as $\text{limit}[2] = 2$</td>
			<td align="center" style="border: 1px solid black;">[2]</td>
			<td align="center" style="border: 1px solid black;">9</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">3</td>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">[2]</td>
			<td align="center" style="border: 1px solid black;">10</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">4</td>
			<td align="center" style="border: 1px solid black;">3</td>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">3</td>
			<td align="center" style="border: 1px solid black;">$j = 0, 1, 3$ as $\text{limit}[j] = 3$</td>
			<td align="center" style="border: 1px solid black;">[0, 1, 2, 3]</td>
			<td align="center" style="border: 1px solid black;">12</td>
		</tr>
	</tbody>
</table>

Thus, the maximum possible total is 12.

</div>

### 4. Constraints

- $1 \le n = \text{value.length} = \text{limit.length} \le 10^{5}$

- $1 \le \text{value}[i] \le 10^{5}$​​​​​​​

- $1 \le \text{limit}[i] \le n$