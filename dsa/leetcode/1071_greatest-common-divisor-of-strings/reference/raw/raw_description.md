## Description

For two strings `s` and `t`, we say "`t` divides `s`" if and only if `s = t + t + t + ... + t + t` (i.e., `t` is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return *the largest string *`x`* such that *`x`* divides both *`str1`* and *`str2`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">str1 = "ABCABC", str2 = "ABC"</span>

**Output:** <span class="example-io">"ABC"</span>

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">str1 = "ABABAB", str2 = "ABAB"</span>

**Output:** <span class="example-io">"AB"</span>

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">str1 = "LEET", str2 = "CODE"</span>

**Output:** <span class="example-io">""</span>

</div>

**Example 4:**

<div class="example-block">
**Input:** <span class="example-io">str1 = "AAAAAB", str2 = "AAA"</span>

**Output:** <span class="example-io">""</span>​​​​​​​

</div>

**Constraints:**

	- `1 <= str1.length, str2.length <= 1000`

	- `str1` and `str2` consist of English uppercase letters.
