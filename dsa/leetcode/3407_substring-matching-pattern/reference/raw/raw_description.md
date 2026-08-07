## Description

You are given a string `s` and a pattern string `p`, where `p` contains **exactly one** `'*'` character.

The `'*'` in `p` can be replaced with any sequence of zero or more characters.

Return `true` if `p` can be made a <span data-keyword="substring-nonempty">substring</span> of `s`, and `false` otherwise.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "leetcode", p = "ee*e"</span>

**Output:** <span class="example-io">true</span>

**Explanation:**

By replacing the `'*'` with `"tcod"`, the substring `"eetcode"` matches the pattern.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "car", p = "c*v"</span>

**Output:** <span class="example-io">false</span>

**Explanation:**

There is no substring matching the pattern.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "luck", p = "u*"</span>

**Output:** <span class="example-io">true</span>

**Explanation:**

The substrings `"u"`, `"uc"`, and `"uck"` match the pattern.

</div>

**Constraints:**

	- `1 <= s.length <= 50`

	- `1 <= p.length <= 50 `

	- `s` contains only lowercase English letters.

	- `p` contains only lowercase English letters and exactly one `'*'`
