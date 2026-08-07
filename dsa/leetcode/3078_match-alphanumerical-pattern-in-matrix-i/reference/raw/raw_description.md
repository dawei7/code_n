## Description

You are given a 2D integer matrix `board` and a 2D character matrix `pattern`. Where `0 <= board[r][c] <= 9` and each element of `pattern` is either a digit or a lowercase English letter.

Your task is to find a <span data-keyword="submatrix">submatrix</span> of `board` that **matches** `pattern`.

An integer matrix `part` matches `pattern` if we can replace cells containing letters in `pattern` with some digits (each **distinct** letter with a **unique** digit) in such a way that the resulting matrix becomes identical to the integer matrix `part`. In other words,

	- The matrices have identical dimensions.

	- If `pattern[r][c]` is a digit, then `part[r][c]` must be the **same** digit.

	- If `pattern[r][c]` is a letter `x`:

		<li>For every `pattern[i][j] == x`, `part[i][j]` must be the **same** as `part[r][c]`.

		- For every `pattern[i][j] != x`, `part[i][j]` must be **different** than `part[r][c]`.<span style="display: none;"> </span>

	</li>

Return *an array of length *`2`* containing the row number and column number of the upper-left corner of a submatrix of *`board`* which matches *`pattern`*. If there is more than one such submatrix, return the coordinates of the submatrix with the lowest row index, and in case there is still a tie, return the coordinates of the submatrix with the lowest column index. If there are no suitable answers, return* `[-1, -1]`.

**Example 1:**

<div style="display:flex; flex-wrap: wrap; align-items: flex-start; gap: 12px;">
<table border="1" cellspacing="3" style="border-collapse: separate; text-align: center;">
	<tbody>
		<tr>
			<td style="padding: 5px 10px; border: 1px solid red; --darkreader-inline-border-top: #b30000; --darkreader-inline-border-right: #b30000; --darkreader-inline-border-bottom: #b30000; --darkreader-inline-border-left: #b30000;">1</td>
			<td style="padding: 5px 10px; border: 1px solid red; --darkreader-inline-border-top: #b30000; --darkreader-inline-border-right: #b30000; --darkreader-inline-border-bottom: #b30000; --darkreader-inline-border-left: #b30000;">2</td>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">2</td>
		</tr>
		<tr>
			<td style="padding: 5px 10px; border: 1px solid red; --darkreader-inline-border-top: #b30000; --darkreader-inline-border-right: #b30000; --darkreader-inline-border-bottom: #b30000; --darkreader-inline-border-left: #b30000;">2</td>
			<td style="padding: 5px 10px; border: 1px solid red; --darkreader-inline-border-top: #b30000; --darkreader-inline-border-right: #b30000; --darkreader-inline-border-bottom: #b30000; --darkreader-inline-border-left: #b30000;">2</td>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">3</td>
		</tr>
		<tr>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">2</td>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">3</td>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">3</td>
		</tr>
	</tbody>
</table>

<table border="1" cellspacing="3" style="border-collapse: separate; text-align: center;">
	<tbody>
		<tr>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">a</td>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">b</td>
		</tr>
		<tr>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">b</td>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">b</td>
		</tr>
	</tbody>
</table>
</div>

<div class="example-block">
**Input:** <span class="example-io">board = [[1,2,2],[2,2,3],[2,3,3]], pattern = ["ab","bb"]</span>

**Output:** <span class="example-io">[0,0]</span>

**Explanation:** If we consider this mapping: `"a" -> 1` and `"b" -> 2`; the submatrix with the upper-left corner `(0,0)` is a match as outlined in the matrix above.

Note that the submatrix with the upper-left corner (1,1) is also a match but since it comes after the other one, we return `[0,0]`.

</div>

**Example 2:**

<div style="display:flex; flex-wrap: wrap; align-items: flex-start; gap: 12px;">
<table border="1" cellspacing="3" style="border-collapse: separate; text-align: center;">
	<tbody>
		<tr>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">1</td>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">1</td>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">2</td>
		</tr>
		<tr>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">3</td>
			<td style="padding: 5px 10px; border: 1px solid red; --darkreader-inline-border-top: #b30000; --darkreader-inline-border-right: #b30000; --darkreader-inline-border-bottom: #b30000; --darkreader-inline-border-left: #b30000;">3</td>
			<td style="padding: 5px 10px; border: 1px solid red; --darkreader-inline-border-top: #b30000; --darkreader-inline-border-right: #b30000; --darkreader-inline-border-bottom: #b30000; --darkreader-inline-border-left: #b30000;">4</td>
		</tr>
		<tr>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">6</td>
			<td style="padding: 5px 10px; border: 1px solid red; --darkreader-inline-border-top: #b30000; --darkreader-inline-border-right: #b30000; --darkreader-inline-border-bottom: #b30000; --darkreader-inline-border-left: #b30000;">6</td>
			<td style="padding: 5px 10px; border: 1px solid red; --darkreader-inline-border-top: #b30000; --darkreader-inline-border-right: #b30000; --darkreader-inline-border-bottom: #b30000; --darkreader-inline-border-left: #b30000;">6</td>
		</tr>
	</tbody>
</table>

<table border="1" cellspacing="3" style="border-collapse: separate; text-align: center;">
	<tbody>
		<tr>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">a</td>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">b</td>
		</tr>
		<tr>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">6</td>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">6</td>
		</tr>
	</tbody>
</table>
</div>

<div class="example-block">
**Input:** <span class="example-io">board = [[1,1,2],[3,3,4],[6,6,6]], pattern = ["ab","66"]</span>

**Output:** <span class="example-io">[1,1]</span>

**Explanation:** If we consider this mapping: `"a" -> 3` and `"b" -> 4`; the submatrix with the upper-left corner `(1,1)` is a match as outlined in the matrix above.

Note that since the corresponding values of `"a"` and `"b"` must differ, the submatrix with the upper-left corner `(1,0)` is not a match. Hence, we return `[1,1]`.

</div>

**Example 3:**

<div style="display:flex; flex-wrap: wrap; align-items: flex-start; gap: 12px;">
<table border="1" cellspacing="3" style="border-collapse: separate; text-align: center;">
	<tbody>
		<tr>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">1</td>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">2</td>
		</tr>
		<tr>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">2</td>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">1</td>
		</tr>
	</tbody>
</table>

<table border="1" cellspacing="3" style="border-collapse: separate; text-align: center;">
	<tbody>
		<tr>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">x</td>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">x</td>
		</tr>
	</tbody>
</table>
</div>

<div class="example-block">
**Input:** <span class="example-io">board = [[1,2],[2,1]], pattern = ["xx"]</span>

**Output:** <span class="example-io">[-1,-1]</span>

**Explanation:** Since the values of the matched submatrix must be the same, there is no match. Hence, we return `[-1,-1]`.

</div>

**Constraints:**

	- `1 <= board.length <= 50`

	- `1 <= board[i].length <= 50`

	- `0 <= board[i][j] <= 9`

	- `1 <= pattern.length <= 50`

	- `1 <= pattern[i].length <= 50`

	- `pattern[i][j]` is either a digit represented as a string or a lowercase English letter.
