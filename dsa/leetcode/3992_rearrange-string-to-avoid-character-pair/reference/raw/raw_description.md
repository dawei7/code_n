## Description

You are given a string `s` and two distinct lowercase English letters `x` and `y`.

Rearrange the characters of `s` to construct a new string `t` such that:

	- `t` is a <span data-keyword="permutation-string">permutation</span> of `s`.

	- Every occurrence of `y` appears before every occurrence of `x` in `t`.

Return any valid string `t`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "aabc", x = "a", y = "c"</span>

**Output:** <span class="example-io">"cbaa"</span>

**Explanation:**

The string `"cbaa"` is a permutation of `"aabc"`, and every occurrence of `'c'` appears before every occurrence of `'a'`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "dcab", x = "d", y = "b"</span>

**Output:** <span class="example-io">"cabd"</span>

**Explanation:**

The string `"cabd"` is a permutation of `"dcab"`, and every occurrence of `'b'` appears before every occurrence of `'d'`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "axe", x = "o", y = "x"</span>

**Output:** <span class="example-io">"axe"</span>

**Explanation:**

The string `"axe"` is already valid. Since `'o'` does not occur in the string, the required condition is automatically satisfied.

</div>

**Constraints:**

	- `1 <= s.length <= 100`

	- `s` consists of lowercase English letters.

	- `x` and `y` are lowercase English letters.

	- `x != y`
