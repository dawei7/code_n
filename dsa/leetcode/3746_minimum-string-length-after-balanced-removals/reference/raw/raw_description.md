## Description

You are given a string `s` consisting only of the characters `'a'` and `'b'`.

You are allowed to repeatedly remove **any <span data-keyword="substring-nonempty">substring</span>** where the number of `'a'` characters is equal to the number of `'b'` characters. After each removal, the remaining parts of the string are concatenated together without gaps.

Return an integer denoting the **minimum possible length** of the string after performing any number of such operations.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = `"aabbab"`</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

The substring `"aabbab"` has three `'a'` and three `'b'`. Since their counts are equal, we can remove the entire string directly. The minimum length is 0.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = `"aaaa"`</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

Every substring of `"aaaa"` contains only `'a'` characters. No substring can be removed as a result, so the minimum length remains 4.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = `"aaabb"`</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

First, remove the substring `"ab"`, leaving `"aab"`. Next, remove the new substring `"ab"`, leaving `"a"`. No further removals are possible, so the minimum length is 1.

</div>

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s[i]` is either `'a'` or `'b'`.
