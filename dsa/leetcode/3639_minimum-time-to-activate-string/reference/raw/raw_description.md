## Description

You are given a string `s` of length `n` and an integer array `order`, where `order` is a **<span data-keyword="permutation">permutation</span>** of the numbers in the range `[0, n - 1]`.

Starting from time `t = 0`, replace the character at index `order[t]` in `s` with `'*'` at each time step.

A **<span data-keyword="substring-nonempty">substring</span>** is **valid** if it contains **at least** one `'*'`.

A string is **active** if the total number of **valid** substrings is greater than or equal to `k`.

Return the **minimum** time `t` at which the string `s` becomes **active**. If it is impossible, return -1.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "abc", order = [1,0,2], k = 2</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`t`</th>
			<th style="border: 1px solid black;">`order[t]`</th>
			<th style="border: 1px solid black;">Modified `s`</th>
			<th style="border: 1px solid black;">Valid Substrings</th>
			<th style="border: 1px solid black;">Count</th>
			<th style="border: 1px solid black;">Active

			(Count >= k)</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">`"a*c"`</td>
			<td style="border: 1px solid black;">`"*"`, `"a*"`, `"*c"`, `"a*c"`</td>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">Yes</td>
		</tr>
	</tbody>
</table>

The string `s` becomes active at `t = 0`. Thus, the answer is 0.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "cat", order = [0,2,1], k = 6</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`t`</th>
			<th style="border: 1px solid black;">`order[t]`</th>
			<th style="border: 1px solid black;">Modified `s`</th>
			<th style="border: 1px solid black;">Valid Substrings</th>
			<th style="border: 1px solid black;">Count</th>
			<th style="border: 1px solid black;">Active

			(Count >= k)</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">`"*at"`</td>
			<td style="border: 1px solid black;">`"*"`, `"*a"`, `"*at"`</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">No</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">`"*a*"`</td>
			<td style="border: 1px solid black;">`"*"`, `"*a"`, `"<code inline="">*a*"`</code>, `"<code inline="">a*"`</code>, `"*"`</td>
			<td style="border: 1px solid black;">5</td>
			<td style="border: 1px solid black;">No</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">`"***"`</td>
			<td style="border: 1px solid black;">All substrings (contain `'*'`)</td>
			<td style="border: 1px solid black;">6</td>
			<td style="border: 1px solid black;">Yes</td>
		</tr>
	</tbody>
</table>

The string `s` becomes active at `t = 2`. Thus, the answer is 2.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "xy", order = [0,1], k = 4</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

Even after all replacements, it is impossible to obtain `k = 4` valid substrings. Thus, the answer is -1.

</div>

**Constraints:**

	- `1 <= n == s.length <= 10^5`

	- `order.length == n`

	- `0 <= order[i] <= n - 1`

	- `s` consists of lowercase English letters.

	- `order` is a permutation of integers from 0 to `n - 1`.

	- `1 <= k <= 10^9`
