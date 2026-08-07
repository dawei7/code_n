### 1. Description

You are given two 2D integer arrays `series1` and `series2`.

Each element in both series is of the form `[timestamp, value]`, where:

- `timestamp` is an integer representing the time.

- `value` is an integer representing the value at that timestamp.

Each array is sorted in strictly increasing order of `timestamp`.

For any timestamp **not present** in a series, its value is taken from the **next available timestamp** in the same series if one exists. Otherwise, its value is considered 0.

The **aggregated series** is formed by summing the corresponding values from both series at every timestamp that appears in either series.

Return the **aggregated series** as a 2D integer array of `[timestamp, summedValue]` pairs, sorted in **strictly increasing** order of timestamp.

### 2. Function Contract

**Inputs**

- `series1`: A nonempty array of `[timestamp, value]` pairs in strictly increasing timestamp order.
- `series2`: A second nonempty array with the same pair format and ordering guarantee.

Let $n=\lvert\texttt{series1}\rvert$ and $m=\lvert\texttt{series2}\rvert$. For a timestamp `t`, a series contributes the value belonging to its first entry whose timestamp is at least `t`, or zero if it has no such entry.

**Return value**

Return one `[timestamp, summedValue]` pair for every distinct timestamp present in either series, sorted in strictly increasing timestamp order.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** series1 = [[1,3],[4,1]], series2 = [[2,2],[5,2]]

**Output:** [[1,5],[2,3],[4,3],[5,2]]

**Explanation:**

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Timestamp</th>
			<th style="border: 1px solid black;">`series1`</th>
			<th style="border: 1px solid black;">`series2`</th>
			<th style="border: 1px solid black;">`summedValue`</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">5</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">5</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
	</tbody>
</table>

Thus, the aggregated series is `[[1, 5], [2, 3], [4, 3], [5, 2]]`.

</div>
#### Example 2

<div class="example-block">
**Input:** series1 = [[1,5],[3,1]], series2 = [[2,2]]

**Output:** [[1,7],[2,3],[3,1]]

**Explanation:**

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Timestamp</th>
			<th style="border: 1px solid black;">`series1`</th>
			<th style="border: 1px solid black;">`series2`</th>
			<th style="border: 1px solid black;">`summedValue`</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">5</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">7</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
	</tbody>
</table>

Thus, the aggregated series is `[[1, 7], [2, 3], [3, 1]]`.

</div>
#### Example 3

<div class="example-block">
**Input:** series1 = [[1,5]], series2 = [[1000000000,2]]

**Output:** [[1,7],[1000000000,2]]

**Explanation:**

At timestamp 1, the next available value in `series2` is 2 at timestamp 1000000000. At timestamp 1000000000, there is no later timestamp in `series1`, so its value is 0. Only timestamps that appear in at least one of the two series are included.

</div>

### 4. Constraints

- $1 \le \text{series1.length}, \text{series2.length} \le 10^{5}$

- $\text{series1}[i].length = \text{series2}[i].length = 2$

- $1 \le \text{series1}[i][0], \text{series2}[i][0] \le 10^{9}$

- $1 \le \text{series1}[i][1], \text{series2}[i][1] \le 10^{9}$

- Each series is sorted in strictly increasing order of `timestamp`.