## Description

You are given two strings `s` and `t` consisting of lowercase English letters.

You may choose **at most** one index in `s` and replace the character at that index with any lowercase English letter.

Return `true` if it is possible to make `s` a <span data-keyword="subsequence-string">subsequence</span> of `t`; otherwise, return `false`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "cat", t = "chat"</span>

**Output:** <span class="example-io">true</span>

**Explanation:**

	- Replace `s[1]` from `'a'` to `'h'`. The resulting string is `"cht"`.

	- `"cht"` is a subsequence of `"chat"` because we can match `'c'`, `'h'`, and `'t'` in order.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "plane", t = "apple"</span>

**Output:** <span class="example-io">false</span>

**Explanation:**

	- The characters `'p'`, `'l'`, and `'e'` can be matched in `t`, but the remaining characters cannot be matched while preserving the required order.

	- Even after replacing any one character in `s`, it is impossible to make `s` a subsequence of `t`.

</div>

**Constraints:**

	- `1 <= s.length, t.length <= 10^5`

	- `s` and `t` consist only of lowercase English letters.
