## Description

You are given an integer array `nums`, an integer `k`, and an integer `multiplier`.

You need to perform `k` operations on `nums`. In each operation:

- Find the **minimum** value `x` in `nums`. If there are multiple occurrences of the minimum value, select the one that appears **first**.

- Replace the selected minimum value `x` with $x * multiplier$.

Return an integer array denoting the *final state* of `nums` after performing all `k` operations.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [2,1,3,5,6], k = 5, multiplier = 2

**Output:** [8,4,6,5,6]

**Explanation:**

<table>
	<tbody>
		<tr>
			<th>Operation</th>
			<th>Result</th>
		</tr>
		<tr>
			<td>After operation 1</td>
			<td>[2, 2, 3, 5, 6]</td>
		</tr>
		<tr>
			<td>After operation 2</td>
			<td>[4, 2, 3, 5, 6]</td>
		</tr>
		<tr>
			<td>After operation 3</td>
			<td>[4, 4, 3, 5, 6]</td>
		</tr>
		<tr>
			<td>After operation 4</td>
			<td>[4, 4, 6, 5, 6]</td>
		</tr>
		<tr>
			<td>After operation 5</td>
			<td>[8, 4, 6, 5, 6]</td>
		</tr>
	</tbody>
</table>
</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,2], k = 3, multiplier = 4

**Output:** [16,8]

**Explanation:**

<table>
	<tbody>
		<tr>
			<th>Operation</th>
			<th>Result</th>
		</tr>
		<tr>
			<td>After operation 1</td>
			<td>[4, 2]</td>
		</tr>
		<tr>
			<td>After operation 2</td>
			<td>[4, 8]</td>
		</tr>
		<tr>
			<td>After operation 3</td>
			<td>[16, 8]</td>
		</tr>
	</tbody>
</table>
</div>
### Constraints

- $1 \le \text{nums.length} \le 100$

- $1 \le \text{nums}[i] \le 100$

- $1 \le k \le 10$

- $1 \le multiplier \le 5$