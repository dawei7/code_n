### 1. Description

You are given an `m x n` grid where each cell contains one of the values 0, 1, or 2. You are also given an integer `k`.

You start from the top-left corner `(0, 0)` and want to reach the bottom-right corner $(m - 1, n - 1)$ by moving only **right** or **down**.

Each cell contributes a specific score and incurs an associated cost, according to their cell values:

- 0: adds 0 to your score and costs 0.

- 1: adds 1 to your score and costs 1.

- 2: adds 2 to your score and costs 1. ​​​​​​​

Return the **maximum** score achievable without exceeding a total cost of `k`, or -1 if no valid path exists.

### 2. Function Contract

**Inputs**

- `grid`: A rectangular matrix of cell values whose dimensions are $m$ rows by $n$ columns.
- `k`: The maximum total path cost allowed.

Both the starting and ending cells belong to the path and contribute according to the same score-and-cost rules. The source guarantees $\text{grid}[0][0] = 0$.

For complexity notation, define

$L = \min(k,m+n-2),$

the useful cost-state limit because a right/down path visits $m+n-1$ cells and its guaranteed-zero starting cell costs nothing.

**Return value**

Return the maximum score among paths of cost at most `k`, or `-1` when every path exceeds the budget.

### 3. Note

If you reach the last cell but the total cost exceeds `k`, the path is invalid.

### 4. Examples

#### Example 1

- **Input:** grid = [[0, 1],[2, 0]], k = 1

- **Output:** 2

- **Explanation:** ​​​​​​​

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

#### Example 2

- **Input:** grid = [[0, 1],[1, 2]], k = 1

- **Output:** -1

- **Explanation:** There is no path that reaches cell `(1, 1)`​​​​​​​ without exceeding cost k. Thus, the answer is -1.

### 5. Constraints

- $1 \le m, n \le 200$

- $0 \le k \le 10^{3}​​​​​​​$

- $^​​​​​​​\text{grid}[0][0] = 0$

- $0 \le \text{grid}[i][j] \le 2$
