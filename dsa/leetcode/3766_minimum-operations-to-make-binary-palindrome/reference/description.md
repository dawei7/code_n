## Description

You are given an integer array `nums`.

For each element $\text{nums}[i]$, you may perform the following operations **any** number of times (including zero):

- Increase $\text{nums}[i]$ by 1, or

- Decrease $\text{nums}[i]$ by 1.

A number is called a **binary palindrome** if its binary representation without leading zeros reads the same forward and backward.

Your task is to return an integer array `ans`, where $\text{ans}[i]$ represents the **minimum** number of operations required to convert $\text{nums}[i]$ into a **binary palindrome**.
### Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers.

Each array position is solved separately; changing one value has no effect on any other position. Because each operation changes a value by exactly 1, converting an original value $x$ to a chosen binary palindrome $p$ costs exactly $\lvert x-p\rvert$ operations.

Let $N = \lvert\texttt{nums}\rvert$ and let $V = \max(\texttt{nums})$.

**Return value**

Return `ans`, where $\text{ans}[i]$ is the smallest absolute difference between $\text{nums}[i]$ and any nonnegative integer whose ordinary binary representation is palindromic. Preserve the input order.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2,4]

**Output:** [0,1,1]

**Explanation:**

One optimal set of operations:

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">$\text{nums}[i]$</th>
			<th style="border: 1px solid black;">Binary($\text{nums}[i]$)</th>
			<th style="border: 1px solid black;">Nearest

			Palindrome</th>
			<th style="border: 1px solid black;">Binary

			(Palindrome)</th>
			<th style="border: 1px solid black;">Operations Required</th>
			<th style="border: 1px solid black;">$\text{ans}[i]$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">Already palindrome</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">10</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">11</td>
			<td style="border: 1px solid black;">Increase by 1</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">100</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">11</td>
			<td style="border: 1px solid black;">Decrease by 1</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
	</tbody>
</table>

Thus, $ans = [0, 1, 1]$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [6,7,12]

**Output:** [1,0,3]

**Explanation:**

One optimal set of operations:

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">$\text{nums}[i]$</th>
			<th style="border: 1px solid black;">Binary($\text{nums}[i]$)</th>
			<th style="border: 1px solid black;">Nearest

			Palindrome</th>
			<th style="border: 1px solid black;">Binary

			(Palindrome)</th>
			<th style="border: 1px solid black;">Operations Required</th>
			<th style="border: 1px solid black;">$\text{ans}[i]$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">6</td>
			<td style="border: 1px solid black;">110</td>
			<td style="border: 1px solid black;">5</td>
			<td style="border: 1px solid black;">101</td>
			<td style="border: 1px solid black;">Decrease by 1</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">7</td>
			<td style="border: 1px solid black;">111</td>
			<td style="border: 1px solid black;">7</td>
			<td style="border: 1px solid black;">111</td>
			<td style="border: 1px solid black;">Already palindrome</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">12</td>
			<td style="border: 1px solid black;">1100</td>
			<td style="border: 1px solid black;">15</td>
			<td style="border: 1px solid black;">1111</td>
			<td style="border: 1px solid black;">Increase by 3</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
	</tbody>
</table>

Thus, $ans = [1, 0, 3]$.

</div>
### Constraints

- $1 \le \text{nums.length} \le 5000$

- $^​​​​​​​1 \le \text{nums}[i] \le ^ 5000$