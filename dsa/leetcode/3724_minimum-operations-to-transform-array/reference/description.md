## Description

You are given two integer arrays `nums1` of length `n` and `nums2` of length $n + 1$.

You want to transform `nums1` into `nums2` using the **minimum** number of operations.

You may perform the following operations **any** number of times, each time choosing an index `i`:

- **Increase** $\text{nums1}[i]$ by 1.

- **Decrease** $\text{nums1}[i]$ by 1.

- **Append** $\text{nums1}[i]$ to the **end** of the array.

Return the **minimum** number of operations required to transform `nums1` into `nums2`.
### Function Contract

**Inputs**

- `nums1`: The initial array of $n$ integers.
- `nums2`: The target array of $n+1$ integers.

Incrementing or decrementing changes one selected value by exactly one. Appending copies the selected value at that moment; it does not remove or relocate the original element.

**Return value**

Return the minimum number of increments, decrements, and append operations required to transform `nums1` exactly into `nums2`.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums1 = [2,8], nums2 = [1,7,3]

**Output:** 4

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th align="center" style="border: 1px solid black;">Step</th>
			<th align="center" style="border: 1px solid black;">`i`</th>
			<th align="center" style="border: 1px solid black;">Operation</th>
			<th align="center" style="border: 1px solid black;">$\text{nums1}[i]$</th>
			<th align="center" style="border: 1px solid black;">Updated `nums1`</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">0</td>
			<td align="center" style="border: 1px solid black;">Append</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">[2, 8, 2]</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">0</td>
			<td align="center" style="border: 1px solid black;">Decrement</td>
			<td align="center" style="border: 1px solid black;">Decreases to 1</td>
			<td align="center" style="border: 1px solid black;">[1, 8, 2]</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">3</td>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">Decrement</td>
			<td align="center" style="border: 1px solid black;">Decreases to 7</td>
			<td align="center" style="border: 1px solid black;">[1, 7, 2]</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">4</td>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">Increment</td>
			<td align="center" style="border: 1px solid black;">Increases to 3</td>
			<td align="center" style="border: 1px solid black;">[1, 7, 3]</td>
		</tr>
	</tbody>
</table>

Thus, after 4 operations `nums1` is transformed into `nums2`.

</div>
#### Example 2

<div class="example-block">
**Input:** nums1 = [1,3,6], nums2 = [2,4,5,3]

**Output:** 4

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th align="center" style="border: 1px solid black;">Step</th>
			<th align="center" style="border: 1px solid black;">`i`</th>
			<th align="center" style="border: 1px solid black;">Operation</th>
			<th align="center" style="border: 1px solid black;">$\text{nums1}[i]$</th>
			<th align="center" style="border: 1px solid black;">Updated `nums1`</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">Append</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">[1, 3, 6, 3]</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">0</td>
			<td align="center" style="border: 1px solid black;">Increment</td>
			<td align="center" style="border: 1px solid black;">Increases to 2</td>
			<td align="center" style="border: 1px solid black;">[2, 3, 6, 3]</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">3</td>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">Increment</td>
			<td align="center" style="border: 1px solid black;">Increases to 4</td>
			<td align="center" style="border: 1px solid black;">[2, 4, 6, 3]</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">4</td>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">Decrement</td>
			<td align="center" style="border: 1px solid black;">Decreases to 5</td>
			<td align="center" style="border: 1px solid black;">[2, 4, 5, 3]</td>
		</tr>
	</tbody>
</table>

Thus, after 4 operations `nums1` is transformed into `nums2`.

</div>
#### Example 3

<div class="example-block">
**Input:** nums1 = [2], nums2 = [3,4]

**Output:** 3

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th align="center" style="border: 1px solid black;">Step</th>
			<th align="center" style="border: 1px solid black;">`i`</th>
			<th align="center" style="border: 1px solid black;">Operation</th>
			<th align="center" style="border: 1px solid black;">$\text{nums1}[i]$</th>
			<th align="center" style="border: 1px solid black;">Updated `nums1`</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">0</td>
			<td align="center" style="border: 1px solid black;">Increment</td>
			<td align="center" style="border: 1px solid black;">Increases to 3</td>
			<td align="center" style="border: 1px solid black;">[3]</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">0</td>
			<td align="center" style="border: 1px solid black;">Append</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">[3, 3]</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">3</td>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">Increment</td>
			<td align="center" style="border: 1px solid black;">Increases to 4</td>
			<td align="center" style="border: 1px solid black;">[3, 4]</td>
		</tr>
	</tbody>
</table>

Thus, after 3 operations `nums1` is transformed into `nums2`.

</div>
### Constraints

- $1 \le n = \text{nums1.length} \le 10^{5}$

- $\text{nums2.length} = n + 1$

- $1 \le \text{nums1}[i], \text{nums2}[i] \le 10^{5}$