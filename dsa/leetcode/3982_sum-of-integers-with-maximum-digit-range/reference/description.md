### 1. Description

You are given an integer array `nums`.

The **digit range** of an integer is defined as the difference between its **largest** digit and **smallest** digit.

For example, the digit range of 5724 is $7 - 2 = 5$.

Return the sum of all integers in `nums` whose **digit range** is equal to the **maximum digit range** among all integers in the array.

### 2. Function Contract

`solve(nums) -> int`

Let $S$ be the total number of decimal digits across the input values:

$S = \sum_{x \in \texttt{nums}} \operatorname{digits}(x).$

**Inputs**

- `nums`: A nonempty list of positive integers.

Each array position is a separate contribution candidate. The digit range of a value is its maximum decimal digit minus its minimum decimal digit.

**Output**

Return the sum of all values whose digit range equals the largest digit range present anywhere in `nums`.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [5724,111,350]

**Output:** 6074

**Explanation:**

<table border="1" bordercolor="#ccc" cellpadding="5" cellspacing="0" style="border-collapse:collapse;">
	<tbody>
		<tr>
			<th style="text-align:center;">`i`</th>
			<th style="text-align:center;">$\text{nums}[i]$</th>
			<th style="text-align:center;">Largest</th>
			<th style="text-align:center;">Smallest</th>
			<th style="text-align:center;">Digit Range</th>
		</tr>
		<tr>
			<td style="text-align:center;">0</td>
			<td style="text-align:center;">5724</td>
			<td style="text-align:center;">7</td>
			<td style="text-align:center;">2</td>
			<td style="text-align:center;">5</td>
		</tr>
		<tr>
			<td style="text-align:center;">1</td>
			<td style="text-align:center;">111</td>
			<td style="text-align:center;">1</td>
			<td style="text-align:center;">1</td>
			<td style="text-align:center;">0</td>
		</tr>
		<tr>
			<td style="text-align:center;">2</td>
			<td style="text-align:center;">350</td>
			<td style="text-align:center;">5</td>
			<td style="text-align:center;">0</td>
			<td style="text-align:center;">5</td>
		</tr>
	</tbody>
</table>

The maximum digit range is 5. The integers with this digit range are 5724 and 350, so the answer is $5724 + 350 = 6074$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [90,900]

**Output:** 990

**Explanation:**

<table border="1" bordercolor="#ccc" cellpadding="5" cellspacing="0" style="border-collapse:collapse;">
	<tbody>
		<tr>
			<th style="text-align:center;">`i`</th>
			<th style="text-align:center;">$\text{nums}[i]$</th>
			<th style="text-align:center;">Largest</th>
			<th style="text-align:center;">Smallest</th>
			<th style="text-align:center;">Digit Range</th>
		</tr>
		<tr>
			<td style="text-align:center;">0</td>
			<td style="text-align:center;">90</td>
			<td style="text-align:center;">9</td>
			<td style="text-align:center;">0</td>
			<td style="text-align:center;">9</td>
		</tr>
		<tr>
			<td style="text-align:center;">1</td>
			<td style="text-align:center;">900</td>
			<td style="text-align:center;">9</td>
			<td style="text-align:center;">0</td>
			<td style="text-align:center;">9</td>
		</tr>
	</tbody>
</table>

The maximum digit range is 9. Both integers have this digit range, so the answer is $90 + 900 = 990$.

</div>

### 4. Constraints

- $1 \le \text{nums.length} \le 100$

- $10 \le \text{nums}[i] \le 10^{5}$