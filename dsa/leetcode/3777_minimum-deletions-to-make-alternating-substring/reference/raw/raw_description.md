## Description

You are given a string `s` of length `n` consisting only of the characters `'A'` and `'B'`.

You are also given a 2D integer array `queries` of length `q`, where each `queries[i]` is one of the following:

	- `[1, j]`: **Flip** the character at index `j` of `s` i.e. `'A'` changes to `'B'` (and vice versa). This operation mutates `s` and affects subsequent queries.

	- `[2, l, r]`: **Compute** the **minimum** number of character deletions required to make the **substring** `s[l..r]` **alternating**. This operation does not modify `s`; the length of `s` remains `n`.

A **<span data-keyword="substring-nonempty">substring</span>** is **alternating** if no two **adjacent** characters are **equal**. A substring of length 1 is always alternating.

Return an integer array `answer`, where `answer[i]` is the result of the `i^th` query of type `[2, l, r]`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "ABA", queries = [[2,1,2],[1,1],[2,0,2]]</span>

**Output:** <span class="example-io">[0,2]</span>

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th align="center" style="border: 1px solid black;">`**i**`</th>
			<th align="center" style="border: 1px solid black;">`**queries[i]**`</th>
			<th align="center" style="border: 1px solid black;">`**j**`</th>
			<th align="center" style="border: 1px solid black;">`**l**`</th>
			<th align="center" style="border: 1px solid black;">`**r**`</th>
			<th align="center" style="border: 1px solid black;">**`s` before query**</th>
			<th align="center" style="border: 1px solid black;">`**s[l..r]**`</th>
			<th align="center" style="border: 1px solid black;">**Result**</th>
			<th align="center" style="border: 1px solid black;">**Answer**</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="center" style="border: 1px solid black;">0</td>
			<td align="center" style="border: 1px solid black;">[2, 1, 2]</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">`"ABA"`</td>
			<td align="center" style="border: 1px solid black;">`"BA"`</td>
			<td align="center" style="border: 1px solid black;">Already alternating</td>
			<td align="center" style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">[1, 1]</td>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">`"ABA"`</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">Flip `s[1]` from `'B'` to `'A'`</td>
			<td align="center" style="border: 1px solid black;">-</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">[2, 0, 2]</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">0</td>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">`"AAA"`</td>
			<td align="center" style="border: 1px solid black;">`"AAA"`</td>
			<td align="center" style="border: 1px solid black;">Delete any two `'A'`s to get `"A"`</td>
			<td align="center" style="border: 1px solid black;">2</td>
		</tr>
	</tbody>
</table>

Thus, the answer is `[0, 2]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "ABB", queries = [[2,0,2],[1,2],[2,0,2]]</span>

**Output:** <span class="example-io">[1,0]</span>

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th align="center" style="border: 1px solid black;">`**i**`</th>
			<th align="center" style="border: 1px solid black;">`**queries[i]**`</th>
			<th align="center" style="border: 1px solid black;">`**j**`</th>
			<th align="center" style="border: 1px solid black;">`**l**`</th>
			<th align="center" style="border: 1px solid black;">`**r**`</th>
			<th align="center" style="border: 1px solid black;">**`s` before query**</th>
			<th align="center" style="border: 1px solid black;">`**s[l..r]**`</th>
			<th align="center" style="border: 1px solid black;">**Result**</th>
			<th align="center" style="border: 1px solid black;">**Answer**</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="center" style="border: 1px solid black;">0</td>
			<td align="center" style="border: 1px solid black;">[2, 0, 2]</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">0</td>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">`"ABB"`</td>
			<td align="center" style="border: 1px solid black;">`"ABB"`</td>
			<td align="center" style="border: 1px solid black;">Delete one `'B'` to get `"AB"`</td>
			<td align="center" style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">[1, 2]</td>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">`"ABB"`</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">Flip `s[2]` from `'B'` to `'A'`</td>
			<td align="center" style="border: 1px solid black;">-</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">[2, 0, 2]</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">0</td>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">`"ABA"`</td>
			<td align="center" style="border: 1px solid black;">`"ABA"`</td>
			<td align="center" style="border: 1px solid black;">Already alternating</td>
			<td align="center" style="border: 1px solid black;">0</td>
		</tr>
	</tbody>
</table>

Thus, the answer is `[1, 0]`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "BABA", queries = [[2,0,3],[1,1],[2,1,3]]</span>

**Output:** <span class="example-io">[0,1]</span>

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th align="center" style="border: 1px solid black;">`**i**`</th>
			<th align="center" style="border: 1px solid black;">`**queries[i]**`</th>
			<th align="center" style="border: 1px solid black;">`**j**`</th>
			<th align="center" style="border: 1px solid black;">`**l**`</th>
			<th align="center" style="border: 1px solid black;">`**r**`</th>
			<th align="center" style="border: 1px solid black;">**`s` before query**</th>
			<th align="center" style="border: 1px solid black;">`**s[l..r]**`</th>
			<th align="center" style="border: 1px solid black;">**Result**</th>
			<th align="center" style="border: 1px solid black;">**Answer**</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="center" style="border: 1px solid black;">0</td>
			<td align="center" style="border: 1px solid black;">[2, 0, 3]</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">0</td>
			<td align="center" style="border: 1px solid black;">3</td>
			<td align="center" style="border: 1px solid black;">`"BABA"`</td>
			<td align="center" style="border: 1px solid black;">`"BABA"`</td>
			<td align="center" style="border: 1px solid black;">Already alternating</td>
			<td align="center" style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">[1, 1]</td>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">`"BABA"`</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">Flip `s[1]` from `'A'` to `'B'`</td>
			<td align="center" style="border: 1px solid black;">-</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">[2, 1, 3]</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">3</td>
			<td align="center" style="border: 1px solid black;">`"BBBA"`</td>
			<td align="center" style="border: 1px solid black;">`"BBA"`</td>
			<td align="center" style="border: 1px solid black;">Delete one `'B'` to get `"BA"`</td>
			<td align="center" style="border: 1px solid black;">1</td>
		</tr>
	</tbody>
</table>

Thus, the answer is `[0, 1]`.

</div>

**Constraints:**

	- `1 <= n == s.length <= 10^5`

	- `s[i]` is either `'A'` or `'B'`.

	- `1 <= q == queries.length <= 10^5`

	- `queries[i].length == 2` or `3`

		<li>`queries[i] == [1, j]` or,

		- `queries[i] == [2, l, r]`

		- `0 <= j <= n - 1`

		- `0 <= l <= r <= n - 1`

	</li>
