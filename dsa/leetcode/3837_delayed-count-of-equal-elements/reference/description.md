## Description

You are given an integer array `nums` of length `n` and an integer `k`.

For each index `i`, define the **delayed count** as the number of indices `j` such that:

- $i + k < j \le n - 1$, and

- $\text{nums}[j] = \text{nums}[i]$

Return an array `ans` where $\text{ans}[i]$ is the **delayed count** of index `i`.
### Function Contract

**Inputs**

- `nums`: The integer array whose delayed equal-value occurrences must be counted.
- `k`: The number of positions immediately after each index that remain too close to count.

Let $N=\lvert\texttt{nums}\rvert$. For every index $i$, the returned value is

$$
\texttt{ans}[i]
=
\left\lvert
\left\{
j \mid i+\texttt{k}<j\le N-1
\text{ and }
\texttt{nums}[j]=\texttt{nums}[i]
\right\}
\right\rvert.
$$

The strict inequality excludes the position `i + k` as well as the `k` positions directly after `i`; the first eligible position is `i + k + 1`.

**Return value**

Return the length-$N$ array containing the delayed count for every original index.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [1,2,1,1], k = 1

**Output:** [2,0,0,0]

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">$\text{nums}[i]$</th>
			<th style="border: 1px solid black;">possible `j`</th>
			<th style="border: 1px solid black;">$\text{nums}[j]$</th>
			<th style="border: 1px solid black;">satisfying

			$\text{nums}[j] = \text{nums}[i]$</th>
			<th style="border: 1px solid black;">$\text{ans}[i]$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[2, 3]</td>
			<td style="border: 1px solid black;">[1, 1]</td>
			<td style="border: 1px solid black;">[2, 3]</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">[3]</td>
			<td style="border: 1px solid black;">[1]</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
	</tbody>
</table>

Thus, $ans = [2, 0, 0, 0]$​​​​​​​.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [3,1,3,1], k = 0

**Output:** [1,1,0,0]

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">$\text{nums}[i]$</th>
			<th style="border: 1px solid black;">possible `j`</th>
			<th style="border: 1px solid black;">$\text{nums}[j]$</th>
			<th style="border: 1px solid black;">satisfying

			$\text{nums}[j] = \text{nums}[i]$</th>
			<th style="border: 1px solid black;">$\text{ans}[i]$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">[1, 2, 3]</td>
			<td style="border: 1px solid black;">[1, 3, 1]</td>
			<td style="border: 1px solid black;">[2]</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[2, 3]</td>
			<td style="border: 1px solid black;">[3, 1]</td>
			<td style="border: 1px solid black;">[3]</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">[3]</td>
			<td style="border: 1px solid black;">[1]</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
	</tbody>
</table>

Thus, $ans = [1, 1, 0, 0]$​​​​​​​.

</div>
### Constraints

- $1 \le n = \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$

- $0 \le k \le n - 1$