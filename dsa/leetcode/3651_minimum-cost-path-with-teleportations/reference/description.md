## Description

You are given a `m x n` 2D integer array `grid` and an integer `k`. You start at the top-left cell `(0, 0)` and your goal is to reach the bottom‐right cell $(m - 1, n - 1)$.

There are two types of moves available:

- **Normal move**: You can move right or down from your current cell `(i, j)`, i.e. you can move to $(i, j + 1)$ (right) or $(i + 1, j)$ (down). The cost is the value of the destination cell.

- **Teleportation**: You can teleport from any cell `(i, j)`, to any cell `(x, y)` such that $\text{grid}[x][y] \le \text{grid}[i][j]$; the cost of this move is 0. You may teleport at most `k` times.

Return the **minimum** total cost to reach cell $(m - 1, n - 1)$ from `(0, 0)`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** grid = [[1,3,3],[2,5,4],[4,3,5]], k = 2

**Output:** 7

**Explanation:**

Initially we are at (0, 0) and cost is 0.

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Current Position</th>
			<th style="border: 1px solid black;">Move</th>
			<th style="border: 1px solid black;">New Position</th>
			<th style="border: 1px solid black;">Total Cost</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`(0, 0)`</td>
			<td style="border: 1px solid black;">Move Down</td>
			<td style="border: 1px solid black;">`(1, 0)`</td>
			<td style="border: 1px solid black;">$0 + 2 = 2$</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`(1, 0)`</td>
			<td style="border: 1px solid black;">Move Right</td>
			<td style="border: 1px solid black;">`(1, 1)`</td>
			<td style="border: 1px solid black;">$2 + 5 = 7$</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`(1, 1)`</td>
			<td style="border: 1px solid black;">Teleport to `(2, 2)`</td>
			<td style="border: 1px solid black;">`(2, 2)`</td>
			<td style="border: 1px solid black;">$7 + 0 = 7$</td>
		</tr>
	</tbody>
</table>

The minimum cost to reach bottom-right cell is 7.

</div>
#### Example 2

<div class="example-block">
**Input:** grid = [[1,2],[2,3],[3,4]], k = 1

**Output:** 9

**Explanation: **

Initially we are at (0, 0) and cost is 0.

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Current Position</th>
			<th style="border: 1px solid black;">Move</th>
			<th style="border: 1px solid black;">New Position</th>
			<th style="border: 1px solid black;">Total Cost</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`(0, 0)`</td>
			<td style="border: 1px solid black;">Move Down</td>
			<td style="border: 1px solid black;">`(1, 0)`</td>
			<td style="border: 1px solid black;">$0 + 2 = 2$</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`(1, 0)`</td>
			<td style="border: 1px solid black;">Move Right</td>
			<td style="border: 1px solid black;">`(1, 1)`</td>
			<td style="border: 1px solid black;">$2 + 3 = 5$</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`(1, 1)`</td>
			<td style="border: 1px solid black;">Move Down</td>
			<td style="border: 1px solid black;">`(2, 1)`</td>
			<td style="border: 1px solid black;">$5 + 4 = 9$</td>
		</tr>
	</tbody>
</table>

The minimum cost to reach bottom-right cell is 9.

</div>
### Constraints

- $2 \le m, n \le 80$

- $m = \text{grid.length}$

- $n = \text{grid}[i].length$

- $0 \le \text{grid}[i][j] \le 10^{4}$

- $0 \le k \le 10$