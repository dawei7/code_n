### 1. Description

You are given an integer array `nums` of length `n` and an integer `p`.

A **non-empty subsequence** of `nums` is called **good** if:

- Its length is **strictly less** than `n`.

- The **greatest common divisor (GCD)** of its elements is **exactly** `p`.

You are also given a 2D integer array `queries` of length `q`, where each $\text{queries}[i] = [\text{ind}_{i}, \text{val}_{i}]$ indicates that you should update $nums[\text{ind}_{i}]$ to $\text{val}_{i}$.

After each query, determine whether there exists **any good subsequence** in the current array.

Return the **number** of queries for which a **good subsequence** exists.

The term `gcd(a, b)` denotes the **greatest common divisor** of `a` and `b`.

### 2. Function Contract

**Inputs**

- `nums`: An integer array of length $n$.
- `p`: The exact GCD required from a good subsequence.
- `queries`: A list of point updates. Each entry is $[\text{ind}_{i}, \text{val}_{i}]$ and assigns $nums[\text{ind}_{i}] = \text{val}_{i}$.

Queries are processed from left to right on the same mutable logical array. A selected subsequence must contain at least one element, may skip arbitrary positions, and must omit at least one of the $n$ array elements.

**Return value**

Return the number of updates after which at least one non-empty proper subsequence has GCD exactly `p`.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [4,8,12,16], p = 2, queries = [[0,3],[2,6]]

**Output:** 1

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">i</th>
			<th style="border: 1px solid black;">$[\text{ind}_{i}, \text{val}_{i}]$</th>
			<th style="border: 1px solid black;">Operation</th>
			<th style="border: 1px solid black;">Updated `nums`</th>
			<th style="border: 1px solid black;">Any good Subsequence</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">`[0, 3]`</td>
			<td style="border: 1px solid black;">Update $\text{nums}[0]$ to `3`</td>
			<td style="border: 1px solid black;">`[3, 8, 12, 16]`</td>
			<td style="border: 1px solid black;">No, as no subsequence has GCD exactly $p = 2$</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">`[2, 6]`</td>
			<td style="border: 1px solid black;">Update $\text{nums}[2]$ to `6`</td>
			<td style="border: 1px solid black;">`[3, 8, 6, 16]`</td>
			<td style="border: 1px solid black;">Yes, subsequence `[8, 6]` has GCD exactly $p = 2$</td>
		</tr>
	</tbody>
</table>

Thus, the answer is 1.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [4,5,7,8], p = 3, queries = [[0,6],[1,9],[2,3]]

**Output:** 2

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">i</th>
			<th style="border: 1px solid black;">$[\text{ind}_{i}, \text{val}_{i}]$</th>
			<th style="border: 1px solid black;">Operation</th>
			<th style="border: 1px solid black;">Updated `nums`</th>
			<th style="border: 1px solid black;">Any good Subsequence</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">`[0, 6]`</td>
			<td style="border: 1px solid black;">Update $\text{nums}[0]$ to `6`</td>
			<td style="border: 1px solid black;">`[6, 5, 7, 8]`</td>
			<td style="border: 1px solid black;">No, as no subsequence has GCD exactly $p = 3$</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">`[1, 9]`</td>
			<td style="border: 1px solid black;">Update $\text{nums}[1]$ to `9`</td>
			<td style="border: 1px solid black;">`[6, 9, 7, 8]`</td>
			<td style="border: 1px solid black;">Yes, subsequence `[6, 9]` has GCD exactly $p = 3$</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">`[2, 3]`</td>
			<td style="border: 1px solid black;">Update $\text{nums}[2]$ to `3`</td>
			<td style="border: 1px solid black;">`[6, 9, 3, 8]`</td>
			<td style="border: 1px solid black;">Yes, subsequence `[6, 9, 3]` has GCD exactly $p = 3$</td>
		</tr>
	</tbody>
</table>

Thus, the answer is 2.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [5,7,9], p = 2, queries = [[1,4],[2,8]]

**Output:** 0

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">i</th>
			<th style="border: 1px solid black;">$[\text{ind}_{i}, \text{val}_{i}]$</th>
			<th style="border: 1px solid black;">Operation</th>
			<th style="border: 1px solid black;">Updated `nums`</th>
			<th style="border: 1px solid black;">Any good Subsequence</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">`[1, 4]`</td>
			<td style="border: 1px solid black;">Update $\text{nums}[1]$ to `4`</td>
			<td style="border: 1px solid black;">`[5, 4, 9]`</td>
			<td style="border: 1px solid black;">No, as no subsequence has GCD exactly $p = 2$</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">`[2, 8]`</td>
			<td style="border: 1px solid black;">Update $\text{nums}[2]$ to `8`</td>
			<td style="border: 1px solid black;">`[5, 4, 8]`</td>
			<td style="border: 1px solid black;">No, as no subsequence has GCD exactly $p = 2$</td>
		</tr>
	</tbody>
</table>

Thus, the answer is 0.

</div>

### 4. Constraints

- $2 \le n = \text{nums.length} \le 5 * 10^{4}$

- $1 \le \text{nums}[i] \le 5 * 10^{4}$

- $1 \le \text{queries.length} \le 5 * 10^{4}$

- $\text{queries}[i] = [\text{ind}_{i}, \text{val}_{i}]$

- $1 \le \text{val}_{i}, p \le 5 * 10^{4}$

- $0 \le \text{ind}_{i} \le n - 1$