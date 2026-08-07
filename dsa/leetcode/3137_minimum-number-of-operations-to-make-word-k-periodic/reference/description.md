## Description

You are given a string `word` of size `n`, and an integer `k` such that `k` divides `n`.

In one operation, you can pick any two indices `i` and `j`, that are divisible by `k`, then replace the substring of length `k` starting at `i` with the substring of length `k` starting at `j`. That is, replace the substring $word[i..i + k - 1]$ with the substring $word[j..j + k - 1]$.<!-- notionvc: 49ac84f7-0724-452a-ab43-0c5e53f1db33 -->

Return *the **minimum** number of operations required to make* `word` ***k-periodic***.

We say that `word` is **k-periodic** if there is some string `s` of length `k` such that `word` can be obtained by concatenating `s` an arbitrary number of times. For example, if $word = “ababab”$, then `word` is 2-periodic for `s = "ab"`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** word = "leetcodeleet", k = 4

**Output:** 1

**Explanation:**

We can obtain a 4-periodic string by picking i = 4 and j = 0. After this operation, word becomes equal to "leetleetleet".

</div>
#### Example 2

<div class="example-block">
**Input:** word = "leetcoleet", k = 2

**Output:** 3

**Explanation:**

We can obtain a 2-periodic string by applying the operations in the table below.

<table border="1" bordercolor="#ccc" cellpadding="5" cellspacing="0" height="146" style="border-collapse:collapse; text-align: center; vertical-align: middle;">
	<tbody>
		<tr>
			<th>i</th>
			<th>j</th>
			<th>word</th>
		</tr>
		<tr>
			<td style="padding: 5px 15px;">0</td>
			<td style="padding: 5px 15px;">2</td>
			<td style="padding: 5px 15px;">etetcoleet</td>
		</tr>
		<tr>
			<td style="padding: 5px 15px;">4</td>
			<td style="padding: 5px 15px;">0</td>
			<td style="padding: 5px 15px;">etetetleet</td>
		</tr>
		<tr>
			<td style="padding: 5px 15px;">6</td>
			<td style="padding: 5px 15px;">0</td>
			<td style="padding: 5px 15px;">etetetetet</td>
		</tr>
	</tbody>
</table>
</div>

<div id="gtx-trans" style="position: absolute; left: 107px; top: 238.5px;">
<div class="gtx-trans-icon"> </div>
</div>
### Constraints

- $1 \le n = \text{word.length} \le 10^{5}$

- $1 \le k \le \text{word.length}$

- `k` divides `word.length`.

- `word` consists only of lowercase English letters.