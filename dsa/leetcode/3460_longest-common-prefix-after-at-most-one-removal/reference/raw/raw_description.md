## Description

You are given two strings `s` and `t`.

Return the **length** of the **longest common <span data-keyword="string-prefix">prefix</span>** between `s` and `t` after removing **at most** one character from `s`.

**Note:** `s` can be left without any removal.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "madxa", t = "madam"</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

Removing `s[3]` from `s` results in `"mada"`, which has a longest common prefix of length 4 with `t`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "leetcode", t = "eetcode"</span>

**Output:** <span class="example-io">7</span>

**Explanation:**

Removing `s[0]` from `s` results in `"eetcode"`, which matches `t`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "one", t = "one"</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

No removal is needed.

</div>

**Example 4:**

<div class="example-block">
**Input:** <span class="example-io">s = "a", t = "b"</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

`s` and `t` cannot have a common prefix.

</div>

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `1 <= t.length <= 10^5`

	- `s` and `t` contain only lowercase English letters.
