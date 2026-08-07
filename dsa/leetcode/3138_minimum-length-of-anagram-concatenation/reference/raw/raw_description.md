## Description

You are given a string `s`, which is known to be a concatenation of **anagrams** of some string `t`.

Return the **minimum** possible length of the string `t`.

An **anagram** is formed by rearranging the letters of a string. For example, "aab", "aba", and, "baa" are anagrams of "aab".

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "abba"</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

One possible string `t` could be `"ba"`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "cdef"</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

One possible string `t` could be `"cdef"`, notice that `t` can be equal to `s`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "abcbcacabbaccba"</span>

**Output:** <span class="example-io">3</span>

</div>

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` consist only of lowercase English letters.
