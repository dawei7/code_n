## Description

You are given an integer array `nums` and an integer `k`.

In one operation, you can **increase or decrease **any element of `nums` by **exactly** `k`.

You are also given a 2D integer array `queries`, where each $\text{queries}[i] = [l_{i}, r_{i}]$.

For each query, find the **minimum** number of operations required to make **all** elements in the **subarray** $nums[l_{i}..r_{i}]$ **equal**. If it is impossible, the answer for that query is `-1`.

Return an array `ans`, where $\text{ans}[i]$ is the answer for the $$i^{\text{th}}$$ query.
### Function Contract

**Inputs**

- `nums`: The source integer array whose inclusive subarrays are queried.
- `k`: The exact positive amount added or subtracted in one operation.
- `queries`: An array of inclusive index pairs $[l_{i}, r_{i}]$.

Let $n=\lvert\texttt{nums}\rvert$ and $q=\lvert\texttt{queries}\rvert$. Each query is hypothetical and independent: its operations do not mutate `nums` for later queries.

**Return value**

Return an array of $q$ integers containing the minimum operation count for each query, or `-1` wherever equalization is impossible.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,4,7], k = 3, queries = [[0,1],[0,2]]

**Output:** [1,2]

**Explanation:**

One optimal set of operations:

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">$[l_{i}, r_{i}]$</th>
			<th style="border: 1px solid black;">$nums[l_{i}..r_{i}]$</th>
			<th style="border: 1px solid black;">Possibility</th>
			<th style="border: 1px solid black;">Operations</th>
			<th style="border: 1px solid black;">Final

			$nums[l_{i}..r_{i}]$</th>
			<th style="border: 1px solid black;">$\text{ans}[i]$</th>
		</tr>
	</tbody>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">[0, 1]</td>
			<td style="border: 1px solid black;">[1, 4]</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">$\text{nums}[0] + k = 1 + 3 = 4 = \text{nums}[1]$</td>
			<td style="border: 1px solid black;">[4, 4]</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[0, 2]</td>
			<td style="border: 1px solid black;">[1, 4, 7]</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">`nums[0] + k = 1 + 3 = 4 = nums[1]

			nums[2] - k = 7 - 3 = 4 = nums[1]`</td>
			<td style="border: 1px solid black;">[4, 4, 4]</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
	</tbody>
</table>

Thus, $ans = [1, 2]$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,2,4], k = 2, queries = [[0,2],[0,0],[1,2]]

**Output:** [-1,0,1]

**Explanation:**

One optimal set of operations:

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">$[l_{i}, r_{i}]$</th>
			<th style="border: 1px solid black;">$nums[l_{i}..r_{i}]$</th>
			<th style="border: 1px solid black;">Possibility</th>
			<th style="border: 1px solid black;">Operations</th>
			<th style="border: 1px solid black;">Final

			$nums[l_{i}..r_{i}]$</th>
			<th style="border: 1px solid black;">$\text{ans}[i]$</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">[0, 2]</td>
			<td style="border: 1px solid black;">[1, 2, 4]</td>
			<td style="border: 1px solid black;">No</td>
			<td style="border: 1px solid black;">-</td>
			<td style="border: 1px solid black;">[1, 2, 4]</td>
			<td style="border: 1px solid black;">-1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[0, 0]</td>
			<td style="border: 1px solid black;">[1]</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">Already equal</td>
			<td style="border: 1px solid black;">[1]</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">[1, 2]</td>
			<td style="border: 1px solid black;">[2, 4]</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">$\text{nums}[1] + k = 2 + 2 = 4 = \text{nums}[2]$</td>
			<td style="border: 1px solid black;">[4, 4]</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
	</tbody>
</table>

Thus, $ans = [-1, 0, 1]$.

</div>
### Constraints

- $1 \le n = \text{nums.length} \le 4 × 10^{4}$

- $1 \le \text{nums}[i] \le 10^{9}$​​​​​​​

- $1 \le k \le 10^{9}$

- $1 \le \text{queries.length} \le 4 × 10^{4}$

- $^​​​​​​​\text{queries}[i] = [l_{i}, r_{i}]$

- $0 \le l_{i} \le r_{i} \le n - 1$