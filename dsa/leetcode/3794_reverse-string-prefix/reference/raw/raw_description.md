## Description

You are given a string `s` and an integer `k`.

Reverse the first `k` characters of `s` and return the resulting string.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "abcd", k = 2</span>

**Output:** <span class="example-io">"bacd"</span>

**Explanation:**​​​​​​​

The first `k = 2` characters `"ab"` are reversed to `"ba"`. The final resulting string is `"bacd"`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "xyz", k = 3</span>

**Output:** <span class="example-io">"zyx"</span>

**Explanation:**

The first `k = 3` characters `"xyz"` are reversed to `"zyx"`. The final resulting string is `"zyx"`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "hey", k = 1</span>

**Output:** <span class="example-io">"hey"</span>

**Explanation:**

The first `k = 1` character `"h"` remains unchanged on reversal. The final resulting string is `"hey"`.

</div>

**Constraints:**

	- `1 <= s.length <= 100`

	- `s` consists of lowercase English letters.

	- `1 <= k <= s.length`
