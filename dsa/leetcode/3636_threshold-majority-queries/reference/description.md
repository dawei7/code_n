### 1. Description

You are given an integer array `nums` of length `n` and an array `queries`, where $\text{queries}[i] = [l_{i}, r_{i}, \text{threshold}_{i}]$.

Return an array of integers `ans` where $\text{ans}[i]$ is equal to the element in the subarray $nums[l_{i}...r_{i}]$ that appears **at least** $\text{threshold}_{i}$ times, selecting the element with the **highest** frequency (choosing the **smallest** in case of a tie), or -1 if no such element *exists*.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).
- `queries`: Input parameter (`List[List[int]]`).

**Return value**

- Returns `List[int]`.

### 3. Examples

#### Example 1

- **Input:** nums = [1,1,2,2,1,1], queries = [[0,5,4],[0,3,3],[2,3,2]]

- **Output:** [1,-1,2]

- **Explanation:** <table style="border: 1px solid black;">
	<thead>
		<tr>
			<th align="left" style="border: 1px solid black;">Query</th>
			<th align="left" style="border: 1px solid black;">Sub-array</th>
			<th align="left" style="border: 1px solid black;">Threshold</th>
			<th align="left" style="border: 1px solid black;">Frequency table</th>
			<th align="left" style="border: 1px solid black;">Answer</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="left" style="border: 1px solid black;">[0, 5, 4]</td>
			<td align="left" style="border: 1px solid black;">[1, 1, 2, 2, 1, 1]</td>
			<td align="left" style="border: 1px solid black;">4</td>
			<td align="left" style="border: 1px solid black;">1 → 4, 2 → 2</td>
			<td align="left" style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td align="left" style="border: 1px solid black;">[0, 3, 3]</td>
			<td align="left" style="border: 1px solid black;">[1, 1, 2, 2]</td>
			<td align="left" style="border: 1px solid black;">3</td>
			<td align="left" style="border: 1px solid black;">1 → 2, 2 → 2</td>
			<td align="left" style="border: 1px solid black;">-1</td>
		</tr>
		<tr>
			<td align="left" style="border: 1px solid black;">[2, 3, 2]</td>
			<td align="left" style="border: 1px solid black;">[2, 2]</td>
			<td align="left" style="border: 1px solid black;">2</td>
			<td align="left" style="border: 1px solid black;">2 → 2</td>
			<td align="left" style="border: 1px solid black;">2</td>
		</tr>
	</tbody>
</table>

#### Example 2

- **Input:** nums = [3,2,3,2,3,2,3], queries = [[0,6,4],[1,5,2],[2,4,1],[3,3,1]]

- **Output:** [3,2,3,2]

- **Explanation:** <table style="border: 1px solid black;">
	<thead>
		<tr>
			<th align="left" style="border: 1px solid black;">Query</th>
			<th align="left" style="border: 1px solid black;">Sub-array</th>
			<th align="left" style="border: 1px solid black;">Threshold</th>
			<th align="left" style="border: 1px solid black;">Frequency table</th>
			<th align="left" style="border: 1px solid black;">Answer</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="left" style="border: 1px solid black;">[0, 6, 4]</td>
			<td align="left" style="border: 1px solid black;">[3, 2, 3, 2, 3, 2, 3]</td>
			<td align="left" style="border: 1px solid black;">4</td>
			<td align="left" style="border: 1px solid black;">3 → 4, 2 → 3</td>
			<td align="left" style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td align="left" style="border: 1px solid black;">[1, 5, 2]</td>
			<td align="left" style="border: 1px solid black;">[2, 3, 2, 3, 2]</td>
			<td align="left" style="border: 1px solid black;">2</td>
			<td align="left" style="border: 1px solid black;">2 → 3, 3 → 2</td>
			<td align="left" style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td align="left" style="border: 1px solid black;">[2, 4, 1]</td>
			<td align="left" style="border: 1px solid black;">[3, 2, 3]</td>
			<td align="left" style="border: 1px solid black;">1</td>
			<td align="left" style="border: 1px solid black;">3 → 2, 2 → 1</td>
			<td align="left" style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td align="left" style="border: 1px solid black;">[3, 3, 1]</td>
			<td align="left" style="border: 1px solid black;">[2]</td>
			<td align="left" style="border: 1px solid black;">1</td>
			<td align="left" style="border: 1px solid black;">2 → 1</td>
			<td align="left" style="border: 1px solid black;">2</td>
		</tr>
	</tbody>
</table>

### 4. Constraints

- $1 \le \text{nums.length} = n \le 10^{4}$

- $1 \le \text{nums}[i] \le 10^{9}$

- $1 \le \text{queries.length} \le 5 * 10^{4}$

- $\text{queries}[i] = [l_{i}, r_{i}, \text{threshold}_{i}]$

- $0 \le l_{i} \le r_{i} < n$

- $1 \le \text{threshold}_{i} \le r_{i} - l_{i} + 1$
