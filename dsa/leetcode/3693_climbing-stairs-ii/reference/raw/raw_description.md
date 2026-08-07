## Description

You are climbing a staircase with `n + 1` steps, numbered from 0 to `n`.

You are also given a **1-indexed** integer array `costs` of length `n`, where `costs[i]` is the cost of step `i`.

From step `i`, you can jump **only** to step `i + 1`, `i + 2`, or `i + 3`. The cost of jumping from step `i` to step `j` is defined as: `costs[j] + (j - i)^2`

You start from step 0 with `cost = 0`.

Return the **minimum** total cost to reach step `n`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 4, costs = [1,2,3,4]</span>

**Output:** <span class="example-io">13</span>

**Explanation:**

One optimal path is `0 → 1 → 2 → 4`

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Jump</th>
			<th style="border: 1px solid black;">Cost Calculation</th>
			<th style="border: 1px solid black;">Cost</th>
		</tr>
	</tbody>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0 → 1</td>
			<td style="border: 1px solid black;">`costs[1] + (1 - 0)^2 = 1 + 1`</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1 → 2</td>
			<td style="border: 1px solid black;">`costs[2] + (2 - 1)^2 = 2 + 1`</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2 → 4</td>
			<td style="border: 1px solid black;">`costs[4] + (4 - 2)^2 = 4 + 4`</td>
			<td style="border: 1px solid black;">8</td>
		</tr>
	</tbody>
</table>

Thus, the minimum total cost is `2 + 3 + 8 = 13`

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 4, costs = [5,1,6,2]</span>

**Output:** <span class="example-io">11</span>

**Explanation:**

One optimal path is `0 → 2 → 4`

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Jump</th>
			<th style="border: 1px solid black;">Cost Calculation</th>
			<th style="border: 1px solid black;">Cost</th>
		</tr>
	</tbody>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0 → 2</td>
			<td style="border: 1px solid black;">`costs[2] + (2 - 0)^2 = 1 + 4`</td>
			<td style="border: 1px solid black;">5</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2 → 4</td>
			<td style="border: 1px solid black;">`costs[4] + (4 - 2)^2 = 2 + 4`</td>
			<td style="border: 1px solid black;">6</td>
		</tr>
	</tbody>
</table>

Thus, the minimum total cost is `5 + 6 = 11`

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">n = 3, costs = [9,8,3]</span>

**Output:** <span class="example-io">12</span>

**Explanation:**

The optimal path is `0 → 3` with total cost = `costs[3] + (3 - 0)^2 = 3 + 9 = 12`

</div>

**Constraints:**

	- `1 <= n == costs.length <= 10^5​​​​​​​`

	- `1 <= costs[i] <= 10^4`
