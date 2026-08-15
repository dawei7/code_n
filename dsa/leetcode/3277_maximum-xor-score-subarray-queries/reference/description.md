### 1. Description

You are given an array `nums` of `n` integers, and a 2D integer array `queries` of size `q`, where $\text{queries}[i] = [l_{i}, r_{i}]$.

For each query, you must find the **maximum XOR score** of any subarray of $nums[l_{i}..r_{i}]$.

The **XOR score** of an array `a` is found by repeatedly applying the following operations on `a` so that only one element remains, that is the **score**:

- Simultaneously replace $a[i]$ with $a[i] XOR a[i + 1]$ for all indices `i` except the last one.

- Remove the last element of `a`.

Return an array `answer` of size `q` where $\text{answer}[i]$ is the answer to query `i`.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).
- `queries`: Input parameter (`List[List[int]]`).

**Return value**

- Returns `List[int]`.

### 3. Examples

#### Example 1

- **Input:** nums = [2,8,4,32,16,1], queries = [[0,2],[1,4],[0,5]]

- **Output:** [12,60,60]

- **Explanation:** In the first query, `nums[0..2]` has 6 subarrays `[2]`, `[8]`, `[4]`, `[2, 8]`, `[8, 4]`, and `[2, 8, 4]` each with a respective XOR score of 2, 8, 4, 10, 12, and 6. The answer for the query is 12, the largest of all XOR scores.

In the second query, the subarray of `nums[1..4]` with the largest XOR score is `nums[1..4]` with a score of 60.

In the third query, the subarray of `nums[0..5]` with the largest XOR score is `nums[1..4]` with a score of 60.

#### Example 2

- **Input:** nums = [0,7,3,2,8,5,1], queries = [[0,3],[1,5],[2,4],[2,6],[5,6]]

- **Output:** [7,14,11,14,5]

- **Explanation:** <table height="70" width="472">
	<thead>
		<tr>
			<th>Index</th>
			<th>nums[l_i..r_i]</th>
			<th>Maximum XOR Score Subarray</th>
			<th>Maximum Subarray XOR Score</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>0</td>
			<td>[0, 7, 3, 2]</td>
			<td>[7]</td>
			<td>7</td>
		</tr>
		<tr>
			<td>1</td>
			<td>[7, 3, 2, 8, 5]</td>
			<td>[7, 3, 2, 8]</td>
			<td>14</td>
		</tr>
		<tr>
			<td>2</td>
			<td>[3, 2, 8]</td>
			<td>[3, 2, 8]</td>
			<td>11</td>
		</tr>
		<tr>
			<td>3</td>
			<td>[3, 2, 8, 5, 1]</td>
			<td>[2, 8, 5, 1]</td>
			<td>14</td>
		</tr>
		<tr>
			<td>4</td>
			<td>[5, 1]</td>
			<td>[5]</td>
			<td>5</td>
		</tr>
	</tbody>
</table>

### 4. Constraints

- $1 \le n = \text{nums.length} \le 2000$

- $0 \le \text{nums}[i] \le 2^{31} - 1$

- $1 \le q = \text{queries.length} \le 10^{5}$

- $\text{queries}[i].length = 2$

- $\text{queries}[i] = [l_{i}, r_{i}]$

- $0 \le l_{i} \le r_{i} \le n - 1$
