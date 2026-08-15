### 1. Description

You are given an array of positive integers `nums` and a positive integer `k`.

A permutation of `nums` is said to form a **divisible concatenation** if, when you *concatenate* *the decimal representations* of the numbers in the order specified by the permutation, the resulting number is **divisible by** `k`.

Return the **lexicographically smallest** permutation (when considered as a list of integers) that forms a **divisible concatenation**. If no such permutation exists, return an empty list.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).
- `k`: Input parameter (`int`).

**Return value**

- Returns `List[int]`.

### 3. Examples

#### Example 1

- **Input:** nums = [3,12,45], k = 5

- **Output:** [3,12,45]

- **Explanation:** <table data-end="896" data-start="441" node="[object Object]" style="border: 1px solid black;">
	<thead data-end="497" data-start="441">
		<tr data-end="497" data-start="441">
			<th data-end="458" data-start="441" style="border: 1px solid black;">Permutation</th>
			<th data-end="479" data-start="458" style="border: 1px solid black;">Concatenated Value</th>
			<th data-end="497" data-start="479" style="border: 1px solid black;">Divisible by 5</th>
		</tr>
	</thead>
	<tbody data-end="896" data-start="555">
		<tr data-end="611" data-start="555">
			<td style="border: 1px solid black;">[3, 12, 45]</td>
			<td style="border: 1px solid black;">31245</td>
			<td style="border: 1px solid black;">Yes</td>
		</tr>
		<tr data-end="668" data-start="612">
			<td style="border: 1px solid black;">[3, 45, 12]</td>
			<td style="border: 1px solid black;">34512</td>
			<td style="border: 1px solid black;">No</td>
		</tr>
		<tr data-end="725" data-start="669">
			<td style="border: 1px solid black;">[12, 3, 45]</td>
			<td style="border: 1px solid black;">12345</td>
			<td style="border: 1px solid black;">Yes</td>
		</tr>
		<tr data-end="782" data-start="726">
			<td style="border: 1px solid black;">[12, 45, 3]</td>
			<td style="border: 1px solid black;">12453</td>
			<td style="border: 1px solid black;">No</td>
		</tr>
		<tr data-end="839" data-start="783">
			<td style="border: 1px solid black;">[45, 3, 12]</td>
			<td style="border: 1px solid black;">45312</td>
			<td style="border: 1px solid black;">No</td>
		</tr>
		<tr data-end="896" data-start="840">
			<td style="border: 1px solid black;">[45, 12, 3]</td>
			<td style="border: 1px solid black;">45123</td>
			<td style="border: 1px solid black;">No</td>
		</tr>
	</tbody>
</table>

The lexicographically smallest permutation that forms a divisible concatenation is `[3,12,45]`.

#### Example 2

- **Input:** nums = [10,5], k = 10

- **Output:** [5,10]

- **Explanation:** <table data-end="1421" data-start="1200" node="[object Object]" style="border: 1px solid black;">
	<thead data-end="1255" data-start="1200">
		<tr data-end="1255" data-start="1200">
			<th data-end="1216" data-start="1200" style="border: 1px solid black;">Permutation</th>
			<th data-end="1237" data-start="1216" style="border: 1px solid black;">Concatenated Value</th>
			<th data-end="1255" data-start="1237" style="border: 1px solid black;">Divisible by 10</th>
		</tr>
	</thead>
	<tbody data-end="1421" data-start="1312">
		<tr data-end="1366" data-start="1312">
			<td style="border: 1px solid black;">[5, 10]</td>
			<td style="border: 1px solid black;">510</td>
			<td style="border: 1px solid black;">Yes</td>
		</tr>
		<tr data-end="1421" data-start="1367">
			<td style="border: 1px solid black;">[10, 5]</td>
			<td style="border: 1px solid black;">105</td>
			<td style="border: 1px solid black;">No</td>
		</tr>
	</tbody>
</table>

The lexicographically smallest permutation that forms a divisible concatenation is `[5,10]`.

#### Example 3

- **Input:** nums = [1,2,3], k = 5

- **Output:** []

- **Explanation:** Since no permutation of `nums` forms a valid divisible concatenation, return an empty list.

### 4. Constraints

- $1 \le \text{nums.length} \le 13$

- $1 \le \text{nums}[i] \le 10^{5}$

- $1 \le k \le 100$
