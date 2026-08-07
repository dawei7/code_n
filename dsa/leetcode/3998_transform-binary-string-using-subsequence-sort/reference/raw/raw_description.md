## Description

You are given a <span data-keyword="binary-string">binary string</span> `s`.

You are also given an array of strings `strs`, where each `strs[i]` has the **same** length as `s` and consists of characters `'0'`, `'1'`, and `'?'`. Each `'?'` can be replaced by either `'0'` or `'1'`.

You may perform the following operation any number of times (including zero):

	- Choose any <span data-keyword="subsequence-string">subsequence</span> `sub` of `s`.

	- Sort `sub` in **non-decreasing** order.

	- Replace the chosen **subsequence** in `s` with the sorted `sub`, keeping all other characters unchanged.

Return a boolean array `ans`, where `ans[i]` is `true` if it's possible to replace all `'?'` in `strs[i]` with `'0'` or `'1'` and transform `s` into the resulting string using the allowed operation above, otherwise return `false`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "101", strs = ["1?1","0?1","0?0"]</span>

**Output:** <span class="example-io">[true,true,false]</span>

**Explanation:**

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">`strs[i]`</th>
			<th style="border: 1px solid black;">Replacement</th>
			<th style="border: 1px solid black;">Result `strs[i]`</th>
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

			Sort `"101"` to get `"011" = strs[i]`.</td>
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

Thus, `ans = [true, true, false]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "1100", strs = ["0011","11?1","1?1?"]</span>

**Output:** <span class="example-io">[true,false,true]</span>

**Explanation:**

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">`strs[i]`</th>
			<th style="border: 1px solid black;">Replacement</th>
			<th style="border: 1px solid black;">Result `strs[i]`</th>
			<th style="border: 1px solid black;">Operation(s)</th>
			<th style="border: 1px solid black;">Result</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">`"0011"`</td>
			<td style="border: 1px solid black;">-</td>
			<td style="border: 1px solid black;">`"0011"`</td>
			<td style="border: 1px solid black;">Select the subsequence at indices `[0..3]` of `s` → `"1100"`.

			Sort `"1100"` to get `"0011" = strs[i]`.</td>
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

Thus, `ans = [true, false, true]`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "1010", strs = ["0011"]</span>

**Output:** <span class="example-io">[true]</span>

**Explanation:**

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">`strs[i]`</th>
			<th style="border: 1px solid black;">Replacement</th>
			<th style="border: 1px solid black;">Result `strs[i]`</th>
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

Thus, `ans = [true]`.

</div>

**Constraints:**

	- `1 <= n == s.length <= 2000`

	- `s[i]` is either `'0'` or `'1'`.

	- `1 <= strs.length <= 2000`

	- `strs[i].length == n`

	- `strs[i]` is either `'0'`, `'1'`, or `'?'`​​​​​​​.
