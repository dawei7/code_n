## Description

You are given a string `s` consisting of the characters `'N'`, `'S'`, `'E'`, and `'W'`, where $s[i]$ indicates movements in an infinite grid:

- `'N'` : Move north by 1 unit.

- `'S'` : Move south by 1 unit.

- `'E'` : Move east by 1 unit.

- `'W'` : Move west by 1 unit.

Initially, you are at the origin `(0, 0)`. You can change **at most** `k` characters to any of the four directions.

Find the **maximum** **Manhattan distance** from the origin that can be achieved **at any time** while performing the movements **in order**.

The **Manhattan Distance** between two cells $(x_{i}, y_{i})$ and $(x_{j}, y_{j})$ is $|x_{i} - x_{j}| + |y_{i} - y_{j}|$.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** s = "NWSE", k = 1

**Output:** 3

**Explanation:**

Change $s[2]$ from `'S'` to `'N'`. The string `s` becomes `"NWNE"`.

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Movement</th>
			<th style="border: 1px solid black;">Position (x, y)</th>
			<th style="border: 1px solid black;">Manhattan Distance</th>
			<th style="border: 1px solid black;">Maximum</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">s[0] == 'N'</td>
			<td style="border: 1px solid black;">(0, 1)</td>
			<td style="border: 1px solid black;">0 + 1 = 1</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">s[1] == 'W'</td>
			<td style="border: 1px solid black;">(-1, 1)</td>
			<td style="border: 1px solid black;">1 + 1 = 2</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">s[2] == 'N'</td>
			<td style="border: 1px solid black;">(-1, 2)</td>
			<td style="border: 1px solid black;">1 + 2 = 3</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">s[3] == 'E'</td>
			<td style="border: 1px solid black;">(0, 2)</td>
			<td style="border: 1px solid black;">0 + 2 = 2</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
	</tbody>
</table>

The maximum Manhattan distance from the origin that can be achieved is 3. Hence, 3 is the output.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "NSWWEW", k = 3

**Output:** 6

**Explanation:**

Change $s[1]$ from `'S'` to `'N'`, and $s[4]$ from `'E'` to `'W'`. The string `s` becomes `"NNWWWW"`.

The maximum Manhattan distance from the origin that can be achieved is 6. Hence, 6 is the output.

</div>
### Constraints

- $1 \le \text{s.length} \le 10^{5}$

- $0 \le k \le \text{s.length}$

- `s` consists of only `'N'`, `'S'`, `'E'`, and `'W'`.