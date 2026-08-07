## Description

You are given a **1-indexed** integer array `numWays`, where `numWays[i]` represents the number of ways to select a total amount `i` using an **infinite** supply of some *fixed* coin denominations. Each denomination is a **positive** integer with value **at most** `numWays.length`.

However, the exact coin denominations have been *lost*. Your task is to recover the set of denominations that could have resulted in the given `numWays` array.

Return a **sorted** array containing **unique** integers which represents this set of denominations.

If no such set exists, return an **empty** array.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">numWays = [0,1,0,2,0,3,0,4,0,5]</span>

**Output:** <span class="example-io">[2,4,6]</span>

**Explanation:**

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Amount</th>
			<th style="border: 1px solid black;">Number of ways</th>
			<th style="border: 1px solid black;">Explanation</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">There is no way to select coins with total value 1.</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">The only way is `[2]`.</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">There is no way to select coins with total value 3.</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">The ways are `[2, 2]` and `[4]`.</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">5</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">There is no way to select coins with total value 5.</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">6</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">The ways are `[2, 2, 2]`, `[2, 4]`, and `[6]`.</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">7</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">There is no way to select coins with total value 7.</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">8</td>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">The ways are `[2, 2, 2, 2]`, `[2, 2, 4]`, `[2, 6]`, and `[4, 4]`.</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">9</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">There is no way to select coins with total value 9.</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">10</td>
			<td style="border: 1px solid black;">5</td>
			<td style="border: 1px solid black;">The ways are `[2, 2, 2, 2, 2]`, `[2, 2, 2, 4]`, `[2, 4, 4]`, `[2, 2, 6]`, and `[4, 6]`.</td>
		</tr>
	</tbody>
</table>
**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">numWays = [1,2,2,3,4]</span>

**Output:** <span class="example-io">[1,2,5]</span>

**Explanation:**

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Amount</th>
			<th style="border: 1px solid black;">Number of ways</th>
			<th style="border: 1px solid black;">Explanation</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">The only way is `[1]`.</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">The ways are `[1, 1]` and `[2]`.</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">The ways are `[1, 1, 1]` and `[1, 2]`.</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">The ways are `[1, 1, 1, 1]`, `[1, 1, 2]`, and `[2, 2]`.</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">5</td>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">The ways are `[1, 1, 1, 1, 1]`, `[1, 1, 1, 2]`, `[1, 2, 2]`, and `[5]`.</td>
		</tr>
	</tbody>
</table>
</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">numWays = [1,2,3,4,15]</span>

**Output:** <span class="example-io">[]</span>

**Explanation:**

No set of denomination satisfies this array.

</div>

<table style="border: 1px solid black;">
</table>
</div>

**Constraints:**

	- `1 <= numWays.length <= 100`

	- `0 <= numWays[i] <= 2 * 10^8`
