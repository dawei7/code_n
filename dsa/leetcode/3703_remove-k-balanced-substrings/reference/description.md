### 1. Description

You are given a string `s` consisting of `'('` and `')'`, and an integer `k`.

A **string** is **k-balanced** if it is **exactly** `k` **consecutive** `'('` followed by `k` **consecutive** `')'`, i.e., $'(' * k + ')' * k$.

For example, if $k = 3$, k-balanced is `"((()))"`.

You must **repeatedly** remove all **non-overlapping k-balanced substrings** from `s`, and then join the remaining parts. Continue this process until no k-balanced **substring** exists.

Return the final string after all possible removals.

​​​​​​​**Example 1:**

**Input:** s = "(())", k = 1

**Output:** ""

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

#### Example 2

- **Input:** s = "(()(", k = 1

- **Output:** "(("

- **Explanation:** k-balanced substring is `"()"`

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
			<td style="border: 1px solid black;">`(()(`</td>
			<td style="border: 1px solid black;">`(<s>**()**</s>(`</td>
			<td style="border: 1px solid black;">`((`</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">`((`</td>
			<td style="border: 1px solid black;">-</td>
			<td style="border: 1px solid black;">`((`</td>
		</tr>
	</tbody>
</table>

Thus, the final string is `"(("`.

#### Example 3

- **Input:** s = "((()))()()()", k = 3

- **Output:** "()()()"

- **Explanation:** k-balanced substring is `"((()))"`

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
			<td style="border: 1px solid black;">`((()))()()()`</td>
			<td style="border: 1px solid black;">`<s>**((()))**</s>()()()`</td>
			<td style="border: 1px solid black;">`()()()`</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">`()()()`</td>
			<td style="border: 1px solid black;">-</td>
			<td style="border: 1px solid black;">`()()()`</td>
		</tr>
	</tbody>
</table>

Thus, the final string is `"()()()"`.

### 2. Function Contract

**Inputs**

- `s`: A parenthesis string to reduce.
- `k`: The number of consecutive opening parentheses and consecutive closing parentheses in the removable pattern.

The removable substring has length $2 * k$ and is exactly $'(' * k + ')' * k$. Removals may create new occurrences across the newly joined boundary, so processing continues to a fixed point.

**Return value**

Return the unreduced characters, in their original relative order, after no k-balanced substring remains.

### 3. Constraints

- $2 \le \text{s.length} \le 10^{5}$

- `s` consists only of `'('` and `')'`.

- $1 \le k \le \text{s.length} / 2$
