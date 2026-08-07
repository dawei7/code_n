## Description

You are given two strings, `s` and `t`.

You can create a new string by selecting a <span data-keyword="substring">substring</span> from `s` (possibly empty) and a substring from `t` (possibly empty), then concatenating them **in order**.

Return the length of the **longest** <span data-keyword="palindrome-string">palindrome</span> that can be formed this way.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "a", t = "a"</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

Concatenating `"a"` from `s` and `"a"` from `t` results in `"aa"`, which is a palindrome of length 2.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "abc", t = "def"</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

Since all characters are different, the longest palindrome is any single character, so the answer is 1.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "b", t = "aaaa"</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

Selecting "`aaaa`" from `t` is the longest palindrome, so the answer is 4.

</div>

**Example 4:**

<div class="example-block">
**Input:** <span class="example-io">s = "abcde", t = "ecdba"</span>

**Output:** <span class="example-io">5</span>

**Explanation:**

Concatenating `"abc"` from `s` and `"ba"` from `t` results in `"abcba"`, which is a palindrome of length 5.

</div>

**Constraints:**

	- `1 <= s.length, t.length <= 1000`

	- `s` and `t` consist of lowercase English letters.
