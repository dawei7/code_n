### 1. Description

You are given two integer arrays `prices` and `strategy`, where:

- $\text{prices}[i]$ is the price of a given stock on the $$i^{\text{th}}$$ day.

- $\text{strategy}[i]$ represents a trading action on the $$i^{\text{th}}$$ day, where:

		- `-1` indicates buying one unit of the stock.

- `0` indicates holding the stock.

- `1` indicates selling one unit of the stock.

You are also given an **even** integer `k`, and may perform **at most one** modification to `strategy`. A modification consists of:

- Selecting exactly `k` **consecutive** elements in `strategy`.

- Set the **first** $k / 2$ elements to `0` (hold).

- Set the **last** $k / 2$ elements to `1` (sell).

The **profit** is defined as the **sum** of $\text{strategy}[i] * \text{prices}[i]$ across all days.

Return the **maximum** possible profit you can achieve.

### 2. Function Contract

**Inputs**

- `prices`: Input parameter (`List[int]`).
- `strategy`: Input parameter (`List[int]`).
- `k`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Note

There are no constraints on budget or stock ownership, so all buy and sell operations are feasible regardless of past actions.

### 4. Examples

#### Example 1

- **Input:** prices = [4,2,8], strategy = [-1,0,1], k = 2

- **Output:** 10

- **Explanation:** <table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Modification</th>
			<th style="border: 1px solid black;">Strategy</th>
			<th style="border: 1px solid black;">Profit Calculation</th>
			<th style="border: 1px solid black;">Profit</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">Original</td>
			<td style="border: 1px solid black;">[-1, 0, 1]</td>
			<td style="border: 1px solid black;">(-1 × 4) + (0 × 2) + (1 × 8) = -4 + 0 + 8</td>
			<td style="border: 1px solid black;">4</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">Modify [0, 1]</td>
			<td style="border: 1px solid black;">[0, 1, 1]</td>
			<td style="border: 1px solid black;">(0 × 4) + (1 × 2) + (1 × 8) = 0 + 2 + 8</td>
			<td style="border: 1px solid black;">10</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">Modify [1, 2]</td>
			<td style="border: 1px solid black;">[-1, 0, 1]</td>
			<td style="border: 1px solid black;">(-1 × 4) + (0 × 2) + (1 × 8) = -4 + 0 + 8</td>
			<td style="border: 1px solid black;">4</td>
		</tr>
	</tbody>
</table>

Thus, the maximum possible profit is 10, which is achieved by modifying the subarray `[0, 1]`​​​​​​​.

#### Example 2

- **Input:** prices = [5,4,3], strategy = [1,1,0], k = 2

- **Output:** 9

- **Explanation:** <table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Modification</th>
			<th style="border: 1px solid black;">Strategy</th>
			<th style="border: 1px solid black;">Profit Calculation</th>
			<th style="border: 1px solid black;">Profit</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">Original</td>
			<td style="border: 1px solid black;">[1, 1, 0]</td>
			<td style="border: 1px solid black;">(1 × 5) + (1 × 4) + (0 × 3) = 5 + 4 + 0</td>
			<td style="border: 1px solid black;">9</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">Modify [0, 1]</td>
			<td style="border: 1px solid black;">[0, 1, 0]</td>
			<td style="border: 1px solid black;">(0 × 5) + (1 × 4) + (0 × 3) = 0 + 4 + 0</td>
			<td style="border: 1px solid black;">4</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">Modify [1, 2]</td>
			<td style="border: 1px solid black;">[1, 0, 1]</td>
			<td style="border: 1px solid black;">(1 × 5) + (0 × 4) + (1 × 3) = 5 + 0 + 3</td>
			<td style="border: 1px solid black;">8</td>
		</tr>
	</tbody>
</table>

Thus, the maximum possible profit is 9, which is achieved without any modification.

### 5. Constraints

- $2 \le \text{prices.length} = \text{strategy.length} \le 10^{5}$

- $1 \le \text{prices}[i] \le 10^{5}$

- $-1 \le \text{strategy}[i] \le 1$

- $2 \le k \le \text{prices.length}$

- `k` is even
