### 1. Description

You are given a string `s` consisting of lowercase English letters.

The **frequency group** for a value `k` is the set of characters that appear exactly `k` times in s.

The **majority frequency group** is the frequency group that contains the largest number of **distinct** characters.

Return a string containing all characters in the majority frequency group, in **any** order. If two or more frequency groups tie for that largest size, pick the group whose frequency `k` is **larger**.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** s = "aaabbbccdddde"

**Output:** "ab"

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Frequency (k)</th>
			<th style="border: 1px solid black;">Distinct characters in group</th>
			<th style="border: 1px solid black;">Group size</th>
			<th style="border: 1px solid black;">Majority?</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">{d}</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">No</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">{a, b}</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">**Yes**</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">{c}</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">No</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">{e}</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">No</td>
		</tr>
	</tbody>
</table>

Both characters `'a'` and `'b'` share the same frequency 3, they are in the majority frequency group. `"ba"` is also a valid answer.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "abcd"

**Output:** "abcd"

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Frequency (k)</th>
			<th style="border: 1px solid black;">Distinct characters in group</th>
			<th style="border: 1px solid black;">Group size</th>
			<th style="border: 1px solid black;">Majority?</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">{a, b, c, d}</td>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">**Yes**</td>
		</tr>
	</tbody>
</table>

All characters share the same frequency 1, they are all in the majority frequency group.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "pfpfgi"

**Output:** "fp"

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Frequency (k)</th>
			<th style="border: 1px solid black;">Distinct characters in group</th>
			<th style="border: 1px solid black;">Group size</th>
			<th style="border: 1px solid black;">Majority?</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">{p, f}</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">**Yes**</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">{g, i}</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">No (tied size, lower frequency)</td>
		</tr>
	</tbody>
</table>

Both characters `'p'` and `'f'` share the same frequency 2, they are in the majority frequency group. There is a tie in group size with frequency 1, but we pick the higher frequency: 2.

</div>

### 4. Constraints

- $1 \le \text{s.length} \le 100$

- `s` consists only of lowercase English letters.