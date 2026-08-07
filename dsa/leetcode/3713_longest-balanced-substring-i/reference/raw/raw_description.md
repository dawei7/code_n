## Description

You are given a string `s` consisting of lowercase English letters.

A **<span data-keyword="substring-nonempty">substring</span>** of `s` is called **balanced** if all **distinct** characters in the **substring** appear the **same** number of times.

Return the **length** of the **longest balanced substring** of `s`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "abbac"</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

The longest balanced substring is `"abba"` because both distinct characters `'a'` and `'b'` each appear exactly 2 times.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "zzabccy"</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

The longest balanced substring is `"zabc"` because the distinct characters `'z'`, `'a'`, `'b'`, and `'c'` each appear exactly 1 time.​​​​​​​

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "aba"</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

**​​​​​​​**One of the longest balanced substrings is `"ab"` because both distinct characters `'a'` and `'b'` each appear exactly 1 time. Another longest balanced substring is `"ba"`.

</div>

**Constraints:**

	- `1 <= s.length <= 1000`

	- `s` consists of lowercase English letters.
