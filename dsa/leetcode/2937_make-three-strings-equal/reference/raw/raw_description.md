## Description

You are given three strings: `s1`, `s2`, and `s3`. In one operation you can choose one of these strings and delete its **rightmost** character. Note that you **cannot** completely empty a string.

Return the *minimum number of operations* required to make the strings equal*. *If it is impossible to make them equal, return `-1`.

**Example 1:**

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: **<span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">s1 = "abc", s2 = "abb", s3 = "ab"</span>

**Output: **<span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">2</span>

**Explanation: **Deleting the rightmost character from both `s1` and `s2` will result in three equal strings.

</div>

**Example 2:**

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: **<span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">s1 = "dac", s2 = "bac", s3 = "cac"</span>

**Output: **<span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">-1</span>

**Explanation:** Since the first letters of `s1` and `s2` differ, they cannot be made equal.

</div>

**Constraints:**

	- `1 <= s1.length, s2.length, s3.length <= 100`

	- <font face="monospace">`s1`,</font> `<font face="monospace">s2</font>`<font face="monospace"> and</font> `<font face="monospace">s3</font>` consist only of lowercase English letters.
