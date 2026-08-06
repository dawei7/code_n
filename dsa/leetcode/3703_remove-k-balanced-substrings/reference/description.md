## Description

You are given a string `s` consisting of `'('` and `')'`, and an integer `k`.

A **string** is **k-balanced** if it is **exactly** `k` **consecutive** `'('` followed by `k` **consecutive** `')'`, i.e., `'(' * k + ')' * k`.

For example, if `k = 3`, k-balanced is `"((()))"`.

You must **repeatedly** remove all **non-overlapping k-balanced <span data-keyword="substring-nonempty">substrings</span>** from `s`, and then join the remaining parts. Continue this process until no k-balanced **substring** exists.

Return the final string after all possible removals.

 

​​​​​​​<strong class="example">Example 1:</strong>

<div class="example-block">
**Input:** <span class="example-io">s = "(())", k = 1</span>

**Output:** <span class="example-io">""</span>

**Explanation:**

k-balanced substring is `"()"`

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Step</th>
			<th style="border: 1px solid black;">Current `s`</th>
			<th style="border: 1px solid black;">`k-balanced`</th>
			<th style="border: 1px solid black;">Result `s`</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">`(())`</td>
			<td style="border: 1px solid black;">`(<s>**()**</s>)`</td>
			<td style="border: 1px solid black;">`()`</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">`()`</td>
			<td style="border: 1px solid black;"><s>**`()`**</s></td>
			<td style="border: 1px solid black;">Empty</td>
		</tr>
	</tbody>
</table>

Thus, the final string is `""`.

</div>
