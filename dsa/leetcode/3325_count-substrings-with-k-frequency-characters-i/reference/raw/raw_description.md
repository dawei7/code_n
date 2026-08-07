## Description

Given a string `s` and an integer `k`, return the total number of <span data-keyword="substring-nonempty">substrings</span> of `s` where **at least one** character appears **at least** `k` times.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "abacb", k = 2</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

The valid substrings are:

	- `"aba"` (character `'a'` appears 2 times).

	- `"abac"` (character `'a'` appears 2 times).

	- `"abacb"` (character `'a'` appears 2 times).

	- `"bacb"` (character `'b'` appears 2 times).

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "abcde", k = 1</span>

**Output:** <span class="example-io">15</span>

**Explanation:**

All substrings are valid because every character appears at least once.

</div>

**Constraints:**

	- `1 <= s.length <= 3000`

	- `1 <= k <= s.length`

	- `s` consists only of lowercase English letters.
