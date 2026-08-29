### 1. Description

You are climbing a staircase with $n + 1$ steps, numbered from 0 to `n`.

You are also given a **1-indexed** integer array `costs` of length `n`, where $\text{costs}[i]$ is the cost of step `i`.

From step `i`, you can jump **only** to step $i + 1$, $i + 2$, or $i + 3$. The cost of jumping from step `i` to step `j` is defined as: $\text{costs}[j] + (j - i)^2$

You start from step 0 with $cost = 0$.

Return the **minimum** total cost to reach step `n`.

### 2. Function Contract

**Inputs**

- `n`: The index of the destination step and the number of entries in `costs`.
- `costs`: The serialized step costs. Its first list element represents conceptual $\text{costs}[1]$, the cost of landing on step $1$; in general, Python element $costs[k - 1]$ represents step $k$.

Only jumps of length $1$, $2$, or $3$ are permitted. Landing on step $j$ after leaving step $i$ adds $\text{costs}[j] + (j - i)^2$ under the statement's one-based cost notation.

**Return value**

Return the minimum total cost of any valid route from step $0$ to step $n$.

### 3. Examples

#### Example 1

- **Input:** n = 4, costs = [1,2,3,4]

- **Output:** 13

- **Explanation:** One optimal path is `0 → 1 → 2 → 4`

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
			<td style="border: 1px solid black;">$\text{costs}[1] + (1 - 0)^2 = 1 + 1$</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1 → 2</td>
			<td style="border: 1px solid black;">$\text{costs}[2] + (2 - 1)^2 = 2 + 1$</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2 → 4</td>
			<td style="border: 1px solid black;">$\text{costs}[4] + (4 - 2)^2 = 4 + 4$</td>
			<td style="border: 1px solid black;">8</td>
		</tr>
	</tbody>
</table>

Thus, the minimum total cost is $2 + 3 + 8 = 13$

#### Example 2

- **Input:** n = 4, costs = [5,1,6,2]

- **Output:** 11

- **Explanation:** One optimal path is `0 → 2 → 4`

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
			<td style="border: 1px solid black;">$\text{costs}[2] + (2 - 0)^2 = 1 + 4$</td>
			<td style="border: 1px solid black;">5</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2 → 4</td>
			<td style="border: 1px solid black;">$\text{costs}[4] + (4 - 2)^2 = 2 + 4$</td>
			<td style="border: 1px solid black;">6</td>
		</tr>
	</tbody>
</table>

Thus, the minimum total cost is $5 + 6 = 11$

#### Example 3

- **Input:** n = 3, costs = [9,8,3]

- **Output:** 12

- **Explanation:** The optimal path is `0 → 3` with total cost = $\text{costs}[3] + (3 - 0)^2 = 3 + 9 = 12$

### 4. Constraints

- $1 \le n = \text{costs.length} \le 10^{5}$

- $1 \le \text{costs}[i] \le 10^{4}$
