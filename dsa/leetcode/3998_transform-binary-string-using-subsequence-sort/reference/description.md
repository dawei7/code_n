### 1. Description

You are given a binary string `s`.

You are also given an array of strings `strs`, where each $\text{strs}[i]$ has the **same** length as `s` and consists of characters `'0'`, `'1'`, and `'?'`. Each `'?'` can be replaced by either `'0'` or `'1'`.

You may perform the following operation any number of times (including zero):

- Choose any subsequence `sub` of `s`.

- Sort `sub` in **non-decreasing** order.

- Replace the chosen **subsequence** in `s` with the sorted `sub`, keeping all other characters unchanged.

Return a boolean array `ans`, where $\text{ans}[i]$ is `true` if it's possible to replace all `'?'` in $\text{strs}[i]$ with `'0'` or `'1'` and transform `s` into the resulting string using the allowed operation above, otherwise return `false`.

### 2. Function Contract

**Inputs**

- `s`: A binary string of length $n$ containing only `0` and `1`.
- `strs`: An array of $m$ patterns. Every pattern has length $n$ and contains only `0`, `1`, and `?`.

A subsequence keeps the selected indices in their original order; the operation sorts only the characters selected at those indices.

**Return value**

Return a length-$m$ boolean array. Its element at index `i` is `true` exactly when at least one complete binary replacement of $\text{strs}[i]$ is reachable from `s`; otherwise it is `false`.

### 3. Examples

#### Example 1

- **Input:** s = "101", strs = ["1?1","0?1","0?0"]

- **Output:** [true,true,false]

- **Explanation:** <table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">$\text{strs}[i]$</th>
			<th style="border: 1px solid black;">Replacement</th>
			<th style="border: 1px solid black;">Result $\text{strs}[i]$</th>
			<th style="border: 1px solid black;">Operation(s)</th>
			<th style="border: 1px solid black;">Result</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">`"1?1"`</td>
			<td style="border: 1px solid black;">`? → 0`</td>
			<td style="border: 1px solid black;">`"101"`</td>
			<td style="border: 1px solid black;">Matches `s`.</td>
			<td style="border: 1px solid black;">`true`</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">`"0?1"`</td>
			<td style="border: 1px solid black;">`? → 1`</td>
			<td style="border: 1px solid black;">`"011"`</td>
			<td style="border: 1px solid black;">Select the subsequence at indices `[0..2]` of `s` → `"101"`.

			Sort `"101"` to get $"011" = \text{strs}[i]$.</td>
			<td style="border: 1px solid black;">`true`</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">`"0?0"`</td>
			<td style="border: 1px solid black;">`? → 0` or `1`</td>
			<td style="border: 1px solid black;">`"000"` or `"010"`</td>
			<td style="border: 1px solid black;">Not feasible.</td>
			<td style="border: 1px solid black;">`false`</td>
		</tr>
	</tbody>
</table>

Thus, $ans = [true, true, false]$.

#### Example 2

- **Input:** s = "1100", strs = ["0011","11?1","1?1?"]

- **Output:** [true,false,true]

- **Explanation:** <table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">$\text{strs}[i]$</th>
			<th style="border: 1px solid black;">Replacement</th>
			<th style="border: 1px solid black;">Result $\text{strs}[i]$</th>
			<th style="border: 1px solid black;">Operation(s)</th>
			<th style="border: 1px solid black;">Result</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">`"0011"`</td>
			<td style="border: 1px solid black;">-</td>
			<td style="border: 1px solid black;">`"0011"`</td>
			<td style="border: 1px solid black;">Select the subsequence at indices `[0..3]` of `s` → `"1100"`.

			Sort `"1100"` to get $"0011" = \text{strs}[i]$.</td>
			<td style="border: 1px solid black;">`true`</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">`"11?1"`</td>
			<td style="border: 1px solid black;">`? → 0`</td>
			<td style="border: 1px solid black;">`"1101"`</td>
			<td style="border: 1px solid black;">Not feasible.</td>
			<td style="border: 1px solid black;">`false`</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">`"1?1?"`</td>
			<td style="border: 1px solid black;">First `? → 0`

			Second `? → 0`</td>
			<td style="border: 1px solid black;">`"1010"`</td>
			<td style="border: 1px solid black;">Select the subsequence at indices `[1, 2]` of `s` → `"10"`.

			Sort `"10"` to get `"01"`, so `s = "1<u>01</u>0"`.</td>
			<td style="border: 1px solid black;">`true`</td>
		</tr>
	</tbody>
</table>

Thus, $ans = [true, false, true]$.

#### Example 3

- **Input:** s = "1010", strs = ["0011"]

- **Output:** [true]

- **Explanation:** <table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">$\text{strs}[i]$</th>
			<th style="border: 1px solid black;">Replacement</th>
			<th style="border: 1px solid black;">Result $\text{strs}[i]$</th>
			<th style="border: 1px solid black;">Operation(s)</th>
			<th style="border: 1px solid black;">Result</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">`"0011"`</td>
			<td style="border: 1px solid black;">-</td>
			<td style="border: 1px solid black;">`"0011"`</td>
			<td style="border: 1px solid black;">Select the subsequence at indices `[0, 2, 3]` of `s` → `"110"`.

			Sort `"110"` to get `"011"`, so `s = "0<u>0</u>11" = strs[i]`.</td>
			<td style="border: 1px solid black;">`true`</td>
		</tr>
	</tbody>
</table>

Thus, $ans = [true]$.

### 4. Constraints

- $1 \le n = \text{s.length} \le 2000$

- $s[i]$ is either `'0'` or `'1'`.

- $1 \le \text{strs.length} \le 2000$

- $\text{strs}[i].length = n$

- $\text{strs}[i]$ is either `'0'`, `'1'`, or `'?'`.
