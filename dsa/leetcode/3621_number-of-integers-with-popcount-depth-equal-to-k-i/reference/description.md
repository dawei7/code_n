### 1. Description

You are given two integers `n` and `k`.

For any positive integer `x`, define the following sequence:

- $p_{0} = x$

- $p_{i}+1 = popcount(p_{i})$ for all $i \ge 0$, where `popcount(y)` is the number of set bits (1's) in the binary representation of `y`.

This sequence will eventually reach the value 1.

The **popcount-depth** of `x` is defined as the **smallest** integer $d \ge 0$ such that $p_{d} = 1$.

For example, if $x = 7$ (binary representation `"111"`). Then, the sequence is: `7 → 3 → 2 → 1`, so the popcount-depth of 7 is 3.

Your task is to determine the number of integers in the range `[1, n]` whose popcount-depth is **exactly** equal to `k`.

Return the number of such integers.

### 2. Function Contract

**Inputs**

- `n`: Input parameter (`int`).
- `k`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** n = 4, k = 1

- **Output:** 2

- **Explanation:** The following integers in the range `[1, 4]` have popcount-depth exactly equal to 1:

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th align="center" style="border: 1px solid black;">x</th>
			<th align="center" style="border: 1px solid black;">Binary</th>
			<th align="left" style="border: 1px solid black;">Sequence</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">`"10"`</td>
			<td align="left" style="border: 1px solid black;">`2 → 1`</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">4</td>
			<td align="center" style="border: 1px solid black;">`"100"`</td>
			<td align="left" style="border: 1px solid black;">`4 → 1`</td>
		</tr>
	</tbody>
</table>

Thus, the answer is 2.

#### Example 2

- **Input:** n = 7, k = 2

- **Output:** 3

- **Explanation:** The following integers in the range `[1, 7]` have popcount-depth exactly equal to 2:

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">x</th>
			<th style="border: 1px solid black;">Binary</th>
			<th style="border: 1px solid black;">Sequence</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">`"11"`</td>
			<td style="border: 1px solid black;">`3 → 2 → 1`</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">5</td>
			<td style="border: 1px solid black;">`"101"`</td>
			<td style="border: 1px solid black;">`5 → 2 → 1`</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">6</td>
			<td style="border: 1px solid black;">`"110"`</td>
			<td style="border: 1px solid black;">`6 → 2 → 1`</td>
		</tr>
	</tbody>
</table>

Thus, the answer is 3.

### 4. Constraints

- $1 \le n \le 10^{15}$

- $0 \le k \le 5$
