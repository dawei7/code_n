## Description

You are given an integer array `nums` of length `n`.

For every **positive** integer `g`, we define the **beauty** of `g` as the **product** of `g` and the number of **strictly increasing** **subsequences** of `nums` whose greatest common divisor (GCD) is exactly `g`.

Return the **sum** of **beauty** values for all positive integers `g`.

Since the answer could be very large, return it modulo $10^{9} + 7$.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2,3]

**Output:** 10

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

Total beauty is $5 + 2 + 3 = 10$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [4,6]

**Output:** 12

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

Total beauty is $2 + 4 + 6 = 12$.

</div>
### Constraints

- $1 \le n = \text{nums.length} \le 10^{4}$

- $1 \le \text{nums}[i] \le 7 * 10^{4}$