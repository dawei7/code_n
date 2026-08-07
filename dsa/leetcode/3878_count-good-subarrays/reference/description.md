### 1. Description

You are given an integer array `nums`.

A **subarray** is called **good** if the **bitwise OR** of all its elements is equal to **at least one** element present in that subarray.

Return the number of good subarrays in `nums`.

Here, the bitwise OR of two integers `a` and `b` is denoted by `a | b`.

### 2. Function Contract

**Inputs**

- `nums`: The integer array whose non-empty contiguous subarrays are examined.

Let $n=\lvert\texttt{nums}\rvert$. Every legal value uses at most 30 bits because it lies between $0$ and $10^9$ inclusive.

For any subarray, each indexed occurrence is retained when testing whether its aggregate OR equals a value present in that same range. Equal values at different positions do not merge subarrays or witnesses.

**Return value**

Return the number of index intervals $[l,r]$ whose bitwise OR equals $\text{nums}[k]$ for at least one index $k$ with $l\le k\le r$.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [4,2,3]

**Output:** 4

**Explanation:**

The subarrays of `nums` are:

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Subarray</th>
			<th style="border: 1px solid black;">Bitwise OR</th>
			<th style="border: 1px solid black;">Present in Subarray</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[4]`</td>
			<td style="border: 1px solid black;">$4 = 4$</td>
			<td style="border: 1px solid black;">Yes</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[2]`</td>
			<td style="border: 1px solid black;">$2 = 2$</td>
			<td style="border: 1px solid black;">Yes</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[3]`</td>
			<td style="border: 1px solid black;">$3 = 3$</td>
			<td style="border: 1px solid black;">Yes</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[4, 2]`</td>
			<td style="border: 1px solid black;">$4 | 2 = 6$</td>
			<td style="border: 1px solid black;">No</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[2, 3]`</td>
			<td style="border: 1px solid black;">$2 | 3 = 3$</td>
			<td style="border: 1px solid black;">Yes</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[4, 2, 3]`</td>
			<td style="border: 1px solid black;">$4 | 2 | 3 = 7$</td>
			<td style="border: 1px solid black;">No</td>
		</tr>
	</tbody>
</table>

Thus, the good subarrays of `nums` are `[4]`, `[2]`, `[3]` and `[2, 3]`. Thus, the answer is 4.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,3,1]

**Output:** 6

**Explanation:**

Any subarray of `nums` containing 3 has bitwise OR equal to 3, and subarrays containing only 1 have bitwise OR equal to 1.

In both cases, the result is present in the subarray, so all subarrays are good, and the answer is 6.

</div>

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $0 \le \text{nums}[i] \le 10^{9}$