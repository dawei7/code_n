## Description

You are given two strings `s` and `pattern`.

A string `x` is called **almost equal** to `y` if you can change **at most** one character in `x` to make it *identical* to `y`.

Return the **smallest** *starting index* of a <span data-keyword="substring-nonempty">substring</span> in `s` that is **almost equal** to `pattern`. If no such index exists, return `-1`.

A **substring** is a contiguous **non-empty** sequence of characters within a string.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "abcdefg", pattern = "bcdffg"</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

The substring `s[1..6] == "bcdefg"` can be converted to `"bcdffg"` by changing `s[4]` to `"f"`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "ababbababa", pattern = "bacaba"</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

The substring `s[4..9] == "bababa"` can be converted to `"bacaba"` by changing `s[6]` to `"c"`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "abcd", pattern = "dba"</span>

**Output:** <span class="example-io">-1</span>

</div>

**Example 4:**

<div class="example-block">
**Input:** <span class="example-io">s = "dde", pattern = "d"</span>

**Output:** <span class="example-io">0</span>

</div>

**Constraints:**

	- `1 <= pattern.length < s.length <= 10^5`

	- `s` and `pattern` consist only of lowercase English letters.

**Follow-up:** Could you solve the problem if **at most** `k` **consecutive** characters can be changed?
