## Description

You are given an integer array `nums`.

A pair of indices `(i, j)` is called **perfect** if the following conditions are satisfied:

- `i < j`

- Let $a = \text{nums}[i]$, $b = \text{nums}[j]$. Then:

		<li>$min(|a - b|, |a + b|) \le min(|a|, |b|)$

- $max(|a - b|, |a + b|) \ge max(|a|, |b|)$

	</li>

Return the number of **distinct** perfect pairs.

**Note:** The absolute value `|x|` refers to the **non-negative** value of `x`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [0,1,2,3]

**Output:** 2

**Explanation:**

There are 2 perfect pairs:

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`(i, j)`</th>
			<th style="border: 1px solid black;">`(a, b)`</th>
			<th style="border: 1px solid black;">$min(|a − b|, |a + b|)$</th>
			<th style="border: 1px solid black;">`min(|a|, |b|)`</th>
			<th style="border: 1px solid black;">$max(|a − b|, |a + b|)$</th>
			<th style="border: 1px solid black;">`max(|a|, |b|)`</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">(1, 2)</td>
			<td style="border: 1px solid black;">(1, 2)</td>
			<td style="border: 1px solid black;">$min(|1 − 2|, |1 + 2|) = 1$</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">$max(|1 − 2|, |1 + 2|) = 3$</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">(2, 3)</td>
			<td style="border: 1px solid black;">(2, 3)</td>
			<td style="border: 1px solid black;">$min(|2 − 3|, |2 + 3|) = 1$</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">$max(|2 − 3|, |2 + 3|) = 5$</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
	</tbody>
</table>
</div>
#### Example 2

<div class="example-block">
**Input:** nums = [-3,2,-1,4]

**Output:** 4

**Explanation:**

There are 4 perfect pairs:

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`(i, j)`</th>
			<th style="border: 1px solid black;">`(a, b)`</th>
			<th style="border: 1px solid black;">$min(|a − b|, |a + b|)$</th>
			<th style="border: 1px solid black;">`min(|a|, |b|)`</th>
			<th style="border: 1px solid black;">$max(|a − b|, |a + b|)$</th>
			<th style="border: 1px solid black;">`max(|a|, |b|)`</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">(0, 1)</td>
			<td style="border: 1px solid black;">(-3, 2)</td>
			<td style="border: 1px solid black;">$min(|-3 - 2|, |-3 + 2|) = 1$</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">$max(|-3 - 2|, |-3 + 2|) = 5$</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">(0, 3)</td>
			<td style="border: 1px solid black;">(-3, 4)</td>
			<td style="border: 1px solid black;">$min(|-3 - 4|, |-3 + 4|) = 1$</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">$max(|-3 - 4|, |-3 + 4|) = 7$</td>
			<td style="border: 1px solid black;">4</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">(1, 2)</td>
			<td style="border: 1px solid black;">(2, -1)</td>
			<td style="border: 1px solid black;">$min(|2 - (-1)|, |2 + (-1)|) = 1$</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">$max(|2 - (-1)|, |2 + (-1)|) = 3$</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">(1, 3)</td>
			<td style="border: 1px solid black;">(2, 4)</td>
			<td style="border: 1px solid black;">$min(|2 - 4|, |2 + 4|) = 2$</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">$max(|2 - 4|, |2 + 4|) = 6$</td>
			<td style="border: 1px solid black;">4</td>
		</tr>
	</tbody>
</table>
</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1,10,100,1000]

**Output:** 0

**Explanation:**

There are no perfect pairs. Thus, the answer is 0.

</div>
### Constraints

- $2 \le \text{nums.length} \le 10^{5}$

- $-10^{9} \le \text{nums}[i] \le 10^{9}$