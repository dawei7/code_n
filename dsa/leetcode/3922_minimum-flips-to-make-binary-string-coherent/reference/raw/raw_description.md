## Description

You are given a binary string `s`.

A string is considered **coherent** if it does **not** contain `"011"` or `"110"` as <span data-keyword="subsequence-string">subsequences</span>.

In one operation, you can **flip** any character in `s` (`'0'` to `'1'` or `'1'` to `'0'`).

Return an integer denoting the **minimum** number of operations required to make `s` coherent.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "1010"</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

Flip `s[0]` to get `"0010"`, which contains no `"011"` or `"110"` subsequences.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "0110"</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

Flip `s[1]` to get `"0010"`, removing all forbidden subsequences `"011"` and `"110"`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "1000"</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

The string already has no `"011"` or `"110"` subsequences, so no flips are needed.

</div>

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s[i]` is either `'0'` or `'1'`.
