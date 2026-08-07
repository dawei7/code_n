### 1. Description

You are given an array `nums`. An array is considered **positive** if the sum of all numbers in each **subarray** with **more than two** elements is positive.

You can perform the following operation any number of times:

- Replace **one** element in `nums` with any integer between -$10^{18}$ and $10^{18}$.

Find the **minimum** number of operations needed to make `nums` **positive**.

### 2. Function Contract

- Refer to method signature.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [-10,15,-12]

**Output:** 1

**Explanation:**

The only subarray with more than 2 elements is the array itself. The sum of all elements is $(-10) + 15 + (-12) = -7$. By replacing $\text{nums}[0]$ with 0, the new sum becomes $0 + 15 + (-12) = 3$. Thus, the array is now positive.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [-1,-2,3,-1,2,6]

**Output:** 1

**Explanation:**

The only subarrays with more than 2 elements and a non-positive sum are:

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Subarray Indices</th>
			<th style="border: 1px solid black;">Subarray</th>
			<th style="border: 1px solid black;">Sum</th>
			<th style="border: 1px solid black;">Subarray After Replacement (Set nums[1] = 1)</th>
			<th style="border: 1px solid black;">New Sum</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">nums[0...2]</td>
			<td style="border: 1px solid black;">[-1, -2, 3]</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">[-1, 1, 3]</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">nums[0...3]</td>
			<td style="border: 1px solid black;">[-1, -2, 3, -1]</td>
			<td style="border: 1px solid black;">-1</td>
			<td style="border: 1px solid black;">[-1, 1, 3, -1]</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">nums[1...3]</td>
			<td style="border: 1px solid black;">[-2, 3, -1]</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">[1, 3, -1]</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
	</tbody>
</table>

Thus, `nums` is positive after one operation.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1,2,3]

**Output:** 0

**Explanation:**

The array is already positive, so no operations are needed.

</div>

### 4. Constraints

- $3 \le \text{nums.length} \le 10^{5}$

- $-10^{9} \le \text{nums}[i] \le 10^{9}$