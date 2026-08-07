## Description

You are given a digit string `s` that consists of digits from 0 to 9.

A string is called **semi-repetitive** if there is **at most** one adjacent pair of the same digit. For example, `"0010"`, `"002020"`, `"0123"`, `"2002"`, and `"54944"` are semi-repetitive while the following are not: `"00101022"` (adjacent same digit pairs are 00 and 22), and `"1101234883"` (adjacent same digit pairs are 11 and 88).

Return the length of the **longest semi-repetitive <span data-keyword="substring-nonempty">substring</span>** of `s`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "52233"</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

The longest semi-repetitive substring is "5223". Picking the whole string "52233" has two adjacent same digit pairs 22 and 33, but at most one is allowed.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "5494"</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

`s` is a semi-repetitive string.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "1111111"</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The longest semi-repetitive substring is "11". Picking the substring "111" has two adjacent same digit pairs, but at most one is allowed.

</div>

**Constraints:**

	- `1 <= s.length <= 50`

	- `'0' <= s[i] <= '9'`
