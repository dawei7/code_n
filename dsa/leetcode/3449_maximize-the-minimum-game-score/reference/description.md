## Description

You are given an array `points` of size `n` and an integer `m`. There is another array `gameScore` of size `n`, where $\text{gameScore}[i]$ represents the score achieved at the $$i^{\text{th}}$$game. Initially,$\text{gameScore}[i] = 0$ for all `i`.

You start at index -1, which is outside the array (before the first position at index 0). You can make **at most** `m` moves. In each move, you can either:

- Increase the index by 1 and add $\text{points}[i]$ to $\text{gameScore}[i]$.

- Decrease the index by 1 and add $\text{points}[i]$ to $\text{gameScore}[i]$.

**Note** that the index must always remain within the bounds of the array after the first move.

Return the **maximum possible minimum** value in `gameScore` after **at most** `m` moves.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** points = [2,4], m = 3

**Output:** 4

**Explanation:**

Initially, index $i = -1$ and $gameScore = [0, 0]$.

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Move</th>
			<th style="border: 1px solid black;">Index</th>
			<th style="border: 1px solid black;">gameScore</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">Increase `i`</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">`[2, 0]`</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">Increase `i`</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">`[2, 4]`</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">Decrease `i`</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">`[4, 4]`</td>
		</tr>
	</tbody>
</table>

The minimum value in `gameScore` is 4, and this is the maximum possible minimum among all configurations. Hence, 4 is the output.

</div>
#### Example 2

<div class="example-block">
**Input:** points = [1,2,3], m = 5

**Output:** 2

**Explanation:**

Initially, index $i = -1$ and $gameScore = [0, 0, 0]$.

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Move</th>
			<th style="border: 1px solid black;">Index</th>
			<th style="border: 1px solid black;">gameScore</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">Increase `i`</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">`[1, 0, 0]`</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">Increase `i`</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">`[1, 2, 0]`</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">Decrease `i`</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">`[2, 2, 0]`</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">Increase `i`</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">`[2, 4, 0]`</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">Increase `i`</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">`[2, 4, 3]`</td>
		</tr>
	</tbody>
</table>

The minimum value in `gameScore` is 2, and this is the maximum possible minimum among all configurations. Hence, 2 is the output.

</div>
### Constraints

- $2 \le n = \text{points.length} \le 5 * 10^{4}$

- $1 \le \text{points}[i] \le 10^{6}$

- $1 \le m \le 10^{9}$