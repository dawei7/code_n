## Description

You are given a string `s` consisting of lowercase English letters.

The **score** of a string is the sum of the positions of its characters in the alphabet, where `'a' = 1`, `'b' = 2`, ..., `'z' = 26`.

Determine whether there exists an index `i` such that the string can be split into two **non-empty** **<strong><span data-keyword="substring-nonempty">substrings</span>**</strong> `s[0..i]` and `s[(i + 1)..(n - 1)]` that have **equal** scores.

Return `true` if such a split exists, otherwise return `false`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "adcb"</span>

**Output:** <span class="example-io">true</span>

**Explanation:**

Split at index `i = 1`:

	- Left substring = `s[0..1] = "ad"` with `score = 1 + 4 = 5`

	- Right substring = `s[2..3] = "cb"` with `score = 3 + 2 = 5`

Both substrings have equal scores, so the output is `true`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "bace"</span>

**Output:** <span class="example-io">false</span>

**Explanation:​​​​​​**

**​​​​​​​**No split produces equal scores, so the output is `false`.

</div>

**Constraints:**

	- `2 <= s.length <= 100`

	- `s` consists of lowercase English letters.
