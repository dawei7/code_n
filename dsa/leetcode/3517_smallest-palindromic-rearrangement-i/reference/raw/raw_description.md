## Description

You are given a **<span data-keyword="palindrome-string">palindromic</span>** string `s`.

Return the **<span data-keyword="lexicographically-smaller-string">lexicographically smallest</span>** palindromic <span data-keyword="permutation-string">permutation</span> of `s`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "z"</span>

**Output:** <span class="example-io">"z"</span>

**Explanation:**

A string of only one character is already the lexicographically smallest palindrome.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "babab"</span>

**Output:** <span class="example-io">"abbba"</span>

**Explanation:**

Rearranging `"babab"` → `"abbba"` gives the smallest lexicographic palindrome.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "daccad"</span>

**Output:** <span class="example-io">"acddca"</span>

**Explanation:**

Rearranging `"daccad"` → `"acddca"` gives the smallest lexicographic palindrome.

</div>

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` consists of lowercase English letters.

	- `s` is guaranteed to be palindromic.
