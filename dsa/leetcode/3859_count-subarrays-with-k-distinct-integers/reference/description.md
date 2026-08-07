## Description

You are given an integer array `nums` and two integers `k` and `m`.

Return an integer denoting the count of **subarrays** of `nums` such that:

- The subarray contains **exactly** `k` **distinct** integers.

- Within the subarray, each **distinct** integer appears **at least** `m` times.
### Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers.
- `k`: The exact number of distinct integers required in a counted subarray.
- `m`: The minimum frequency required for each distinct integer inside that
  subarray.

Let $N = \lvert\texttt{nums}\rvert$ and $K = \texttt{k}$. A subarray is a
contiguous interval `nums[left:right + 1]`; no elements may be skipped. Both
the exact-distinct-count rule and the per-value frequency rule are evaluated
within that interval alone.

**Return value**

Return the number of subarrays that contain exactly $K$ distinct integers and
give each of those integers a frequency of at least `m`.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [1,2,1,2,2], k = 2, m = 2

**Output:** 2

**Explanation:**

The possible subarrays with $k = 2$ distinct integers, each appearing at least $m = 2$ times are:

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Subarray</th>
			<th style="border: 1px solid black;">Distinct

			numbers</th>
			<th style="border: 1px solid black;">Frequency</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">[1, 2, 1, 2]</td>
			<td style="border: 1px solid black;">{1, 2} → 2</td>
			<td style="border: 1px solid black;">{1: 2, 2: 2}</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">[1, 2, 1, 2, 2]</td>
			<td style="border: 1px solid black;">{1, 2} → 2</td>
			<td style="border: 1px solid black;">{1: 2, 2: 3}</td>
		</tr>
	</tbody>
</table>

Thus, the answer is 2.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [3,1,2,4], k = 2, m = 1

**Output:** 3

**Explanation:**

The possible subarrays with $k = 2$ distinct integers, each appearing at least $m = 1$ times are:

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Subarray</th>
			<th style="border: 1px solid black;">Distinct

			numbers</th>
			<th style="border: 1px solid black;">Frequency</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">[3, 1]</td>
			<td style="border: 1px solid black;">{3, 1} → 2</td>
			<td style="border: 1px solid black;">{3: 1, 1: 1}</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">[1, 2]</td>
			<td style="border: 1px solid black;">{1, 2} → 2</td>
			<td style="border: 1px solid black;">{1: 1, 2: 1}</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">[2, 4]</td>
			<td style="border: 1px solid black;">{2, 4} → 2</td>
			<td style="border: 1px solid black;">{2: 1, 4: 1}</td>
		</tr>
	</tbody>
</table>

Thus, the answer is 3.

</div>
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$

- $1 \le k, m \le \text{nums.length}$