## Description

Given a string `s`, calculate its **reverse degree**.

The **reverse degree** is calculated as follows:

- For each character, multiply its position in the *reversed* alphabet (`'a'` = 26, `'b'` = 25, ..., `'z'` = 1) with its position in the string **(1-indexed)**.

- Sum these products for all characters in the string.

Return the **reverse degree** of `s`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** s = "abc"

**Output:** 148

**Explanation:**

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Letter</th>
			<th style="border: 1px solid black;">Index in Reversed Alphabet</th>
			<th style="border: 1px solid black;">Index in String</th>
			<th style="border: 1px solid black;">Product</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`'a'`</td>
			<td style="border: 1px solid black;">26</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">26</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`'b'`</td>
			<td style="border: 1px solid black;">25</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">50</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`'c'`</td>
			<td style="border: 1px solid black;">24</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">72</td>
		</tr>
	</tbody>
</table>

The reversed degree is $26 + 50 + 72 = 148$.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "zaza"

**Output:** 160

**Explanation:**

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Letter</th>
			<th style="border: 1px solid black;">Index in Reversed Alphabet</th>
			<th style="border: 1px solid black;">Index in String</th>
			<th style="border: 1px solid black;">Product</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`'z'`</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`'a'`</td>
			<td style="border: 1px solid black;">26</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">52</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`'z'`</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`'a'`</td>
			<td style="border: 1px solid black;">26</td>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">104</td>
		</tr>
	</tbody>
</table>

The reverse degree is $1 + 52 + 3 + 104 = 160$.

</div>
### Constraints

- $1 \le \text{s.length} \le 1000$

- `s` contains only lowercase English letters.