## Description

You are given an integer array `nums`.

For any positive integer `x`, define the following sequence:

- $p_{0} = x$

- $p_{i}+1 = popcount(p_{i})$ for all $i \ge 0$, where `popcount(y)` is the number of set bits (1's) in the binary representation of `y`.

This sequence will eventually reach the value 1.

The **popcount-depth** of `x` is defined as the **smallest** integer $d \ge 0$ such that $p_{d} = 1$.

For example, if $x = 7$ (binary representation `"111"`). Then, the sequence is: `7 → 3 → 2 → 1`, so the popcount-depth of 7 is 3.

You are also given a 2D integer array `queries`, where each $\text{queries}[i]$ is either:

- `[1, l, r, k]` - **Determine** the number of indices `j` such that $l \le j \le r$ and the **popcount-depth** of $\text{nums}[j]$ is equal to `k`.

- `[2, idx, val]` - **Update** $\text{nums}[idx]$ to `val`.

Return an integer array `answer`, where $\text{answer}[i]$ is the number of indices for the $$i^{\text{th}}$$ query of type `[1, l, r, k]`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [2,4], queries = [[1,0,1,1],[2,1,1],[1,0,1,0]]

**Output:** [2,1]

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">$\text{queries}[i]$</th>
			<th style="border: 1px solid black;">`nums`</th>
			<th style="border: 1px solid black;">binary(`nums`)</th>
			<th style="border: 1px solid black;">popcount-

			depth</th>
			<th style="border: 1px solid black;">`[l, r]`</th>
			<th style="border: 1px solid black;">`k`</th>
			<th style="border: 1px solid black;">Valid

			$\text{nums}[j]$</th>
			<th style="border: 1px solid black;">updated

			`nums`</th>
			<th style="border: 1px solid black;">Answer</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">[1,0,1,1]</td>
			<td style="border: 1px solid black;">[2,4]</td>
			<td style="border: 1px solid black;">[10, 100]</td>
			<td style="border: 1px solid black;">[1, 1]</td>
			<td style="border: 1px solid black;">[0, 1]</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[0, 1]</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[2,1,1]</td>
			<td style="border: 1px solid black;">[2,4]</td>
			<td style="border: 1px solid black;">[10, 100]</td>
			<td style="border: 1px solid black;">[1, 1]</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">[2,1]</td>
			<td style="border: 1px solid black;">—</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">[1,0,1,0]</td>
			<td style="border: 1px solid black;">[2,1]</td>
			<td style="border: 1px solid black;">[10, 1]</td>
			<td style="border: 1px solid black;">[1, 0]</td>
			<td style="border: 1px solid black;">[0, 1]</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">[1]</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
	</tbody>
</table>

Thus, the final `answer` is `[2, 1]`.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [3,5,6], queries = [[1,0,2,2],[2,1,4],[1,1,2,1],[1,0,1,0]]

**Output:** [3,1,0]

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">$\text{queries}[i]$</th>
			<th style="border: 1px solid black;">`nums`</th>
			<th style="border: 1px solid black;">binary(`nums`)</th>
			<th style="border: 1px solid black;">popcount-

			depth</th>
			<th style="border: 1px solid black;">`[l, r]`</th>
			<th style="border: 1px solid black;">`k`</th>
			<th style="border: 1px solid black;">Valid

			$\text{nums}[j]$</th>
			<th style="border: 1px solid black;">updated

			`nums`</th>
			<th style="border: 1px solid black;">Answer</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">[1,0,2,2]</td>
			<td style="border: 1px solid black;">[3, 5, 6]</td>
			<td style="border: 1px solid black;">[11, 101, 110]</td>
			<td style="border: 1px solid black;">[2, 2, 2]</td>
			<td style="border: 1px solid black;">[0, 2]</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">[0, 1, 2]</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[2,1,4]</td>
			<td style="border: 1px solid black;">[3, 5, 6]</td>
			<td style="border: 1px solid black;">[11, 101, 110]</td>
			<td style="border: 1px solid black;">[2, 2, 2]</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">[3, 4, 6]</td>
			<td style="border: 1px solid black;">—</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">[1,1,2,1]</td>
			<td style="border: 1px solid black;">[3, 4, 6]</td>
			<td style="border: 1px solid black;">[11, 100, 110]</td>
			<td style="border: 1px solid black;">[2, 1, 2]</td>
			<td style="border: 1px solid black;">[1, 2]</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[1]</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">[1,0,1,0]</td>
			<td style="border: 1px solid black;">[3, 4, 6]</td>
			<td style="border: 1px solid black;">[11, 100, 110]</td>
			<td style="border: 1px solid black;">[2, 1, 2]</td>
			<td style="border: 1px solid black;">[0, 1]</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
	</tbody>
</table>

Thus, the final `answer` is `[3, 1, 0]`.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1,2], queries = [[1,0,1,1],[2,0,3],[1,0,0,1],[1,0,0,2]]

**Output:** [1,0,1]

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">$\text{queries}[i]$</th>
			<th style="border: 1px solid black;">`nums`</th>
			<th style="border: 1px solid black;">binary(`nums`)</th>
			<th style="border: 1px solid black;">popcount-

			depth</th>
			<th style="border: 1px solid black;">`[l, r]`</th>
			<th style="border: 1px solid black;">`k`</th>
			<th style="border: 1px solid black;">Valid

			$\text{nums}[j]$</th>
			<th style="border: 1px solid black;">updated

			`nums`</th>
			<th style="border: 1px solid black;">Answer</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">[1,0,1,1]</td>
			<td style="border: 1px solid black;">[1, 2]</td>
			<td style="border: 1px solid black;">[1, 10]</td>
			<td style="border: 1px solid black;">[0, 1]</td>
			<td style="border: 1px solid black;">[0, 1]</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[1]</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[2,0,3]</td>
			<td style="border: 1px solid black;">[1, 2]</td>
			<td style="border: 1px solid black;">[1, 10]</td>
			<td style="border: 1px solid black;">[0, 1]</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">[3, 2]</td>
			<td style="border: 1px solid black;"> </td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">[1,0,0,1]</td>
			<td style="border: 1px solid black;">[3, 2]</td>
			<td style="border: 1px solid black;">[11, 10]</td>
			<td style="border: 1px solid black;">[2, 1]</td>
			<td style="border: 1px solid black;">[0, 0]</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">[1,0,0,2]</td>
			<td style="border: 1px solid black;">[3, 2]</td>
			<td style="border: 1px solid black;">[11, 10]</td>
			<td style="border: 1px solid black;">[2, 1]</td>
			<td style="border: 1px solid black;">[0, 0]</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">[0]</td>
			<td style="border: 1px solid black;">—</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
	</tbody>
</table>

Thus, the final `answer` is `[1, 0, 1]`.

</div>
### Constraints

- $1 \le n = \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{15}$

- $1 \le \text{queries.length} \le 10^{5}$

- $\text{queries}[i].length = 3$ or `4`

		<li>$\text{queries}[i] = [1, l, r, k]$ or,

- $\text{queries}[i] = [2, idx, val]$

- $0 \le l \le r \le n - 1$

- $0 \le k \le 5$

- $0 \le idx \le n - 1$

- $1 \le val \le 10^{15}$

	</li>