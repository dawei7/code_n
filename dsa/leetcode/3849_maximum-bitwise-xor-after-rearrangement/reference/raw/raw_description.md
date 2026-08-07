## Description

You are given two binary strings `s` and `t`​​​​​​​, each of length `n`.

You may **rearrange** the characters of `t` in any order, but `s` **must remain unchanged**.

Return a **binary string** of length `n` representing the **maximum** integer value obtainable by taking the bitwise **XOR** of `s` and rearranged `t`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "101", t = "011"</span>

**Output:** <span class="example-io">"110"</span>

**Explanation:**

	- One optimal rearrangement of `t` is `"011"`.

	- The bitwise XOR of `s` and rearranged `t` is `"101" XOR "011" = "110"`, which is the maximum possible.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "0110", t = "1110"</span>

**Output:** <span class="example-io">"1101"</span>

**Explanation:**

	- One optimal rearrangement of `t` is `"1011"`.

	- The bitwise XOR of `s` and rearranged `t` is `"0110" XOR "1011" = "1101"`, which is the maximum possible.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "0101", t = "1001"</span>

**Output:** <span class="example-io">"1111"</span>

**Explanation:**

	- One optimal rearrangement of `t` is `"1010"`.

	- The bitwise XOR of `s` and rearranged `t` is `"0101" XOR "1010" = "1111"`, which is the maximum possible.

</div>

**Constraints:**

	- `1 <= n == s.length == t.length <= 2 * 10^5`

	- `s[i]` and `t[i]` are either `'0'` or `'1'`.
