## Description

You are given a string `s` consisting of lowercase English letters and digits.

For each character, its **mirror character** is defined by reversing the order of its character set:

- For letters, the mirror of a character is the letter at the same position from the end of the alphabet.

		<li>For example, the mirror of `'a'` is `'z'`, and the mirror of `'b'` is `'y'`, and so on.

	</li>
- For digits, the mirror of a character is the digit at the same position from the end of the range `'0'` to `'9'`.

		<li>For example, the mirror of `'0'` is `'9'`, and the mirror of `'1'` is `'8'`, and so on.

	</li>

For each **unique** character `c` in the string:

- Let `m` be its **mirror** character.

- Let `freq(x)` denote the number of times character `x` appears in the string.

- Compute the **absolute difference** between their **frequencies**, defined as: $|freq(c) - freq(m)|$

The mirror pairs `(c, m)` and `(m, c)` are the same and must be counted **only once**.

Return an integer denoting the total sum of these values over all such **distinct mirror pairs**.
### Function Contract

**Inputs**

- `s`: A nonempty string containing only lowercase English letters and digits.

Letters are mirrored only within `a` through `z`, while digits are mirrored only within `0` through `9`. A mirror character need not itself occur in `s`; its frequency is then zero.

**Return value**

Return the sum of the absolute frequency differences for all distinct mirror pairs. Each unordered pair is included at most once.

### Examples
#### Example 1

<div class="example-block">
**Input:** s = "ab1z9"

**Output:** 3

**Explanation:**

For every mirror pair:

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`c`</th>
			<th style="border: 1px solid black;">`m`</th>
			<th style="border: 1px solid black;">`freq(c)`</th>
			<th style="border: 1px solid black;">`freq(m)`</th>
			<th style="border: 1px solid black;">$|freq(c) - freq(m)|$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">a</td>
			<td style="border: 1px solid black;">z</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">b</td>
			<td style="border: 1px solid black;">y</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">8</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">9</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
	</tbody>
</table>

Thus, the answer is $0 + 1 + 1 + 1 = 3$.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "4m7n"

**Output:** 2

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`c`</th>
			<th style="border: 1px solid black;">`m`</th>
			<th style="border: 1px solid black;">`freq(c)`</th>
			<th style="border: 1px solid black;">`freq(m)`</th>
			<th style="border: 1px solid black;">$|freq(c) - freq(m)|$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">5</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">m</td>
			<td style="border: 1px solid black;">n</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">7</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
	</tbody>
</table>

Thus, the answer is $1 + 0 + 1 = 2$.​​​​​​​

</div>
#### Example 3

<div class="example-block">
**Input:** s = "byby"

**Output:** 0

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`c`</th>
			<th style="border: 1px solid black;">`m`</th>
			<th style="border: 1px solid black;">`freq(c)`</th>
			<th style="border: 1px solid black;">`freq(m)`</th>
			<th style="border: 1px solid black;">$|freq(c) - freq(m)|$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">b</td>
			<td style="border: 1px solid black;">y</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
	</tbody>
</table>

Thus, the answer is 0.

</div>
### Constraints

- $1 \le \text{s.length} \le 5 * 10^{5}$

- `s` consists only of lowercase English letters and digits.