### 1. Description

You are given an integer array `nums` where `nums` is **strictly increasing**.

You are also given a 2D integer array `queries`, where $\text{queries}[i] = [l_{i}, r_{i}, k_{i}]$.

For each query $[l_{i}, r_{i}, k_{i}]$:

- Consider the **subarray** $nums[l_{i}..r_{i}]$

- From the **infinite** sequence of all **positive even integers**: `2, 4, 6, 8, 10, 12, 14, ...`

- **Remove** all elements that appear in the **subarray** $nums[l_{i}..r_{i}]$.

- Find the $k_{i}^th$ **smallest integer** remaining in the sequence after the removals.

Return an integer array `ans`, where $\text{ans}[i]$ is the result for the $$i^{\text{th}}$$ query.

### 2. Function Contract

**Inputs**

- `nums`: A strictly increasing array of positive integers.
- `queries`: Query triples `[l, r, k]`, where `l` and `r` delimit an inclusive subarray and `k` is a one-based rank in the remaining-even sequence.

Let $n = \lvert\texttt{nums}\rvert$ and $q = \lvert\texttt{queries}\rvert$.

**Return value**

Return an array of length $q$. Its $i$-th value is the $k_i$-th smallest positive even integer left after removing the even values present in $nums[l_{i}..r_{i}]$.

### 3. Examples

#### Example 1

- **Input:** nums = [1,4,7], queries = [[0,2,1],[1,1,2],[0,0,3]]

- **Output:** [2,6,6]

- **Explanation:** <table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">$\text{queries}[i]$</th>
			<th style="border: 1px solid black;">$nums[l_{i}..r_{i}]$</th>
			<th style="border: 1px solid black;">Removed

			Evens</th>
			<th style="border: 1px solid black;">Remaining

			Evens</th>
			<th style="border: 1px solid black;">$k_{i}$</th>
			<th style="border: 1px solid black;">$\text{ans}[i]$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">[0, 2, 1]</td>
			<td style="border: 1px solid black;">[1, 4, 7]</td>
			<td style="border: 1px solid black;">[4]</td>
			<td style="border: 1px solid black;">2, 6, 8, ...</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[1, 1, 2]</td>
			<td style="border: 1px solid black;">[4]</td>
			<td style="border: 1px solid black;">[4]</td>
			<td style="border: 1px solid black;">2, 6, 8, ...</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">6</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">[0, 0, 3]</td>
			<td style="border: 1px solid black;">[1]</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">2, 4, 6, ...</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">6</td>
		</tr>
	</tbody>
</table>

Thus, $ans = [2, 6, 6]$.

#### Example 2

- **Input:** nums = [2,5,8], queries = [[0,1,2],[1,2,1],[0,2,4]]

- **Output:** [6,2,12]

- **Explanation:** <table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">$\text{queries}[i]$</th>
			<th style="border: 1px solid black;">$nums[l_{i}..r_{i}]$</th>
			<th style="border: 1px solid black;">Removed

			Evens</th>
			<th style="border: 1px solid black;">Remaining

			Evens</th>
			<th style="border: 1px solid black;">$k_{i}$</th>
			<th style="border: 1px solid black;">$\text{ans}[i]$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">[0, 1, 2]</td>
			<td style="border: 1px solid black;">[2, 5]</td>
			<td style="border: 1px solid black;">[2]</td>
			<td style="border: 1px solid black;">4, 6, 8, ...</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">6</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[1, 2, 1]</td>
			<td style="border: 1px solid black;">[5, 8]</td>
			<td style="border: 1px solid black;">[8]</td>
			<td style="border: 1px solid black;">2, 4, 6, ...</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">[0, 2, 4]</td>
			<td style="border: 1px solid black;">[2, 5, 8]</td>
			<td style="border: 1px solid black;">[2, 8]</td>
			<td style="border: 1px solid black;">4, 6, 10, 12, ...</td>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">12</td>
		</tr>
	</tbody>
</table>

Thus, $ans = [6, 2, 12]$.

#### Example 3

- **Input:** nums = [3,6], queries = [[0,1,1],[1,1,3]]

- **Output:** [2,8]

- **Explanation:** <table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">$\text{queries}[i]$</th>
			<th style="border: 1px solid black;">$nums[l_{i}..r_{i}]$</th>
			<th style="border: 1px solid black;">Removed

			Evens</th>
			<th style="border: 1px solid black;">Remaining

			Evens</th>
			<th style="border: 1px solid black;">$k_{i}$</th>
			<th style="border: 1px solid black;">$\text{ans}[i]$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">[0, 1, 1]</td>
			<td style="border: 1px solid black;">[3, 6]</td>
			<td style="border: 1px solid black;">[6]</td>
			<td style="border: 1px solid black;">2, 4, 8, ...</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[1, 1, 3]</td>
			<td style="border: 1px solid black;">[6]</td>
			<td style="border: 1px solid black;">[6]</td>
			<td style="border: 1px solid black;">2, 4, 8, ...</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">8</td>
		</tr>
	</tbody>
</table>

Thus, $ans = [2, 8]$.

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{9}$

- `nums` is strictly increasing

- $1 \le \text{queries.length} \le 10^{5}$

- $\text{queries}[i] = [l_{i}, r_{i}, k_{i}]$

- $0 \le l_{i} \le r_{i} < \text{nums.length}$

- $1 \le k_{i} \le 10^{9}$​​​​​​​
