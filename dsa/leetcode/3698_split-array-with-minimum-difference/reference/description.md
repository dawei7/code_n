### 1. Description

You are given an integer array `nums`.

Split the array into **exactly** two subarrays, `left` and `right`, such that `left` is **strictly increasing ** and `right` is **strictly decreasing**.

Return the **minimum possible absolute difference** between the sums of `left` and `right`. If no valid split exists, return `-1`.

### 2. Function Contract

**Inputs**

- `nums`: The positive integer array to divide into two nonempty contiguous parts.

A split after index $i$ produces $left = nums[0..i]$ and $right = nums[i+1..n-1]$. Adjacent values in `left` must increase strictly; adjacent values in `right` must decrease strictly.

**Return value**

Return the minimum value of $\lvert\operatorname{sum}(\texttt{left})-\operatorname{sum}(\texttt{right})\rvert$ over valid splits, or `-1` if none exists.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,3,2]

**Output:** 2

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">`left`</th>
			<th style="border: 1px solid black;">`right`</th>
			<th style="border: 1px solid black;">Validity</th>
			<th style="border: 1px solid black;">`left` sum</th>
			<th style="border: 1px solid black;">`right` sum</th>
			<th style="border: 1px solid black;">Absolute difference</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">[1]</td>
			<td style="border: 1px solid black;">[3, 2]</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">5</td>
			<td style="border: 1px solid black;">$|1 - 5| = 4$</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[1, 3]</td>
			<td style="border: 1px solid black;">[2]</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">$|4 - 2| = 2$</td>
		</tr>
	</tbody>
</table>

Thus, the minimum absolute difference is 2.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,2,4,3]

**Output:** 4

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">`left`</th>
			<th style="border: 1px solid black;">`right`</th>
			<th style="border: 1px solid black;">Validity</th>
			<th style="border: 1px solid black;">`left` sum</th>
			<th style="border: 1px solid black;">`right` sum</th>
			<th style="border: 1px solid black;">Absolute difference</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">[1]</td>
			<td style="border: 1px solid black;">[2, 4, 3]</td>
			<td style="border: 1px solid black;">No</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">9</td>
			<td style="border: 1px solid black;">-</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[1, 2]</td>
			<td style="border: 1px solid black;">[4, 3]</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">7</td>
			<td style="border: 1px solid black;">$|3 - 7| = 4$</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">[1, 2, 4]</td>
			<td style="border: 1px solid black;">[3]</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">7</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">$|7 - 3| = 4$</td>
		</tr>
	</tbody>
</table>

Thus, the minimum absolute difference is 4.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [3,1,2]

**Output:** -1

**Explanation:**

No valid split exists, so the answer is -1.

</div>

### 4. Constraints

- $2 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$