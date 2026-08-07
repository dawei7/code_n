## Description

Given an `m x n` binary grid `grid` where:

- $\text{grid}[i][j] = 0$ represents an empty cell, and

- $\text{grid}[i][j] = 1$ represents a mirror.

A robot starts at the top-left corner of the grid `(0, 0)` and wants to reach the bottom-right corner $(m - 1, n - 1)$. It can move only **right** or **down**. If the robot attempts to move into a mirror cell, it is **reflected** before entering that cell:

- If it tries to move **right** into a mirror, it is turned **down** and moved into the cell directly below the mirror.

- If it tries to move **down** into a mirror, it is turned **right** and moved into the cell directly to the right of the mirror.

If this reflection would cause the robot to move outside the `grid` boundaries, the path is considered invalid and should not be counted.

Return the number of unique valid paths from `(0, 0)` to $(m - 1, n - 1)$.

Since the answer may be very large, return it **modulo** $10^{9} + 7$.

**Note**: If a reflection moves the robot into a mirror cell, the robot is immediately reflected again based on the direction it used to enter that mirror: if it entered while moving right, it will be turned down; if it entered while moving down, it will be turned right. This process will continue until either the last cell is reached, the robot moves out of bounds or the robot moves to a non-mirror cell.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** grid = [[0,1,0],[0,0,1],[1,0,0]]

**Output:** 5

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th align="center" style="border: 1px solid black;">Number</th>
			<th align="left" style="border: 1px solid black;">Full Path</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="left" style="border: 1px solid black;">(0, 0) → (0, 1) [M] → (1, 1) → (1, 2) [M] → (2, 2)</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="left" style="border: 1px solid black;">(0, 0) → (0, 1) [M] → (1, 1) → (2, 1) → (2, 2)</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">3</td>
			<td align="left" style="border: 1px solid black;">(0, 0) → (1, 0) → (1, 1) → (1, 2) [M] → (2, 2)</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">4</td>
			<td align="left" style="border: 1px solid black;">(0, 0) → (1, 0) → (1, 1) → (2, 1) → (2, 2)</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">5</td>
			<td align="left" style="border: 1px solid black;">(0, 0) → (1, 0) → (2, 0) [M] → (2, 1) → (2, 2)</td>
		</tr>
	</tbody>
</table>

- `[M]` indicates the robot attempted to enter a mirror cell and instead reflected.

</div>
#### Example 2

<div class="example-block">
**Input:** grid = [[0,0],[0,0]]

**Output:** 2

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th align="center" style="border: 1px solid black;">Number</th>
			<th align="left" style="border: 1px solid black;">Full Path</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="left" style="border: 1px solid black;">(0, 0) → (0, 1) → (1, 1)</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="left" style="border: 1px solid black;">(0, 0) → (1, 0) → (1, 1)</td>
		</tr>
	</tbody>
</table>
</div>
#### Example 3

<div class="example-block">
**Input:** grid = [[0,1,1],[1,1,0]]

**Output:** 1

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th align="center" style="border: 1px solid black;">Number</th>
			<th align="left" style="border: 1px solid black;">Full Path</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="left" style="border: 1px solid black;">(0, 0) → (0, 1) [M] → (1, 1) [M] → (1, 2)</td>
		</tr>
	</tbody>
</table>
`(0, 0) → (1, 0) [M] → (1, 1) [M] → (2, 1)` goes out of bounds, so it is invalid.</div>
### Constraints

- $m = \text{grid.length}$

- $n = \text{grid}[i].length$

- $2 \le m, n \le 500$

- $\text{grid}[i][j]$ is either `0` or `1`.

- $\text{grid}[0][0] = grid[m - 1][n - 1] = 0$