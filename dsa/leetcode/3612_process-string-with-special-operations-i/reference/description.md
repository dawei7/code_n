## Description

You are given a string `s` consisting of lowercase English letters and the special characters: `*`, `#`, and `%`.

Build a new string `result` by processing `s` according to the following rules from left to right:

- If the letter is a **lowercase** English letter append it to `result`.

- A `'*'` **removes** the last character from `result`, if it exists.

- A `'#'` **duplicates** the current `result` and **appends** it to itself.

- A `'%'` **reverses** the current `result`.

Return the final string `result` after processing all characters in `s`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** s = "a#b%*"

**Output:** "ba"

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">$s[i]$</th>
			<th style="border: 1px solid black;">Operation</th>
			<th style="border: 1px solid black;">Current `result`</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">`'a'`</td>
			<td style="border: 1px solid black;">Append `'a'`</td>
			<td style="border: 1px solid black;">`"a"`</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">`'#'`</td>
			<td style="border: 1px solid black;">Duplicate `result`</td>
			<td style="border: 1px solid black;">`"aa"`</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">`'b'`</td>
			<td style="border: 1px solid black;">Append `'b'`</td>
			<td style="border: 1px solid black;">`"aab"`</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">`'%'`</td>
			<td style="border: 1px solid black;">Reverse `result`</td>
			<td style="border: 1px solid black;">`"baa"`</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">`'*'`</td>
			<td style="border: 1px solid black;">Remove the last character</td>
			<td style="border: 1px solid black;">`"ba"`</td>
		</tr>
	</tbody>
</table>

Thus, the final `result` is `"ba"`.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "z*#"

**Output:** ""

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">$s[i]$</th>
			<th style="border: 1px solid black;">Operation</th>
			<th style="border: 1px solid black;">Current `result`</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">`'z'`</td>
			<td style="border: 1px solid black;">Append `'z'`</td>
			<td style="border: 1px solid black;">`"z"`</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">`'*'`</td>
			<td style="border: 1px solid black;">Remove the last character</td>
			<td style="border: 1px solid black;">`""`</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">`'#'`</td>
			<td style="border: 1px solid black;">Duplicate the string</td>
			<td style="border: 1px solid black;">`""`</td>
		</tr>
	</tbody>
</table>

Thus, the final `result` is `""`.

</div>
### Constraints

- $1 \le \text{s.length} \le 20$

- `s` consists of only lowercase English letters and special characters `*`, `#`, and `%`.