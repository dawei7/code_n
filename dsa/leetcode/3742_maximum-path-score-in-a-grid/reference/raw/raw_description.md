## Description

You are given an `m x n` grid where each cell contains one of the values 0, 1, or 2. You are also given an integer `k`.

You start from the top-left corner `(0, 0)` and want to reach the bottom-right corner `(m - 1, n - 1)` by moving only **right** or **down**.

Each cell contributes a specific score and incurs an associated cost, according to their cell values:

	- 0: adds 0 to your score and costs 0.

	- 1: adds 1 to your score and costs 1.

	- 2: adds 2 to your score and costs 1. ​​​​​​​

Return the **maximum** score achievable without exceeding a total cost of `k`, or -1 if no valid path exists.

**Note:** If you reach the last cell but the total cost exceeds `k`, the path is invalid.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[0, 1],[2, 0]], k = 1</span>

**Output:** <span class="example-io">2</span>

**Explanation:**​​​​​​​

The optimal path is:

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Cell</th>
			<th style="border: 1px solid black;">grid[i][j]</th>
			<th style="border: 1px solid black;">Score</th>
			<th style="border: 1px solid black;">Total

			Score</th>
			<th style="border: 1px solid black;">Cost</th>
			<th style="border: 1px solid black;">Total

			Cost</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">(0, 0)</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">(1, 0)</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">(1, 1)</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
	</tbody>
</table>

Thus, the maximum possible score is 2.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[0, 1],[1, 2]], k = 1</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

There is no path that reaches cell `(1, 1)`​​​​​​​ without exceeding cost k. Thus, the answer is -1.

</div>

**Constraints:**

	- `1 <= m, n <= 200`

	- `0 <= k <= 10^3​​​​​​​`

	- `^​​​​​​​grid[0][0] == 0`

	- `0 <= grid[i][j] <= 2`
