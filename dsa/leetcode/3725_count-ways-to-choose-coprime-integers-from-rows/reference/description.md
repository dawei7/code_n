## Description

You are given a `m x n` matrix `mat` of positive integers.

Return an integer denoting the number of ways to choose **exactly one** integer from each row of `mat` such that the **greatest common divisor** of all chosen integers is 1.

Since the answer may be very large, return it **modulo** $10^{9} + 7$.
### Function Contract

**Inputs**

- `mat`: A rectangular matrix of positive integers; exactly one position must be selected from each row.

Choices are based on cell positions. If the same value occurs more than once in a row, selecting either occurrence represents a different way even though it contributes the same integer to the GCD.

**Return value**

Return the number of row-by-row selections whose overall greatest common divisor equals `1`, reduced modulo $1{,}000{,}000{,}007$.

### Examples

#### Example 1

<div class="example-block">
**Input:** mat = [[1,2],[3,4]]

**Output:** 3

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
#### Example 2

<div class="example-block">
**Input:** mat = [[2,2],[2,2]]

**Output:** 0

**Explanation:**

Every combination has a greatest common divisor of 2. Therefore, the answer is 0.

</div>
### Constraints

- $1 \le m = \text{mat.length} \le 150$

- $1 \le n = \text{mat}[i].length \le 150$

- $1 \le \text{mat}[i][j] \le 150$