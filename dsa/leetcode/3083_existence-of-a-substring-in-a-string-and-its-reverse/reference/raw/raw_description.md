## Description

Given a** **string `s`, find any <span data-keyword="substring">substring</span> of length `2` which is also present in the reverse of `s`.

Return `true`* if such a substring exists, and *`false`* otherwise.*

**Example 1:**

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: **<span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">s = "leetcode"</span>

**Output: **<span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">true</span>

**Explanation:** Substring `"ee"` is of length `2` which is also present in `reverse(s) == "edocteel"`.

</div>

**Example 2:**

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: **<span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">s = "abcba"</span>

**Output: **<span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">true</span>

**Explanation:** All of the substrings of length `2` `"ab"`, `"bc"`, `"cb"`, `"ba"` are also present in `reverse(s) == "abcba"`.

</div>

**Example 3:**

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: **<span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">s = "abcd"</span>

**Output: **<span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">false</span>

**Explanation:** There is no substring of length `2` in `s`, which is also present in the reverse of `s`.

</div>

**Constraints:**

	- `1 <= s.length <= 100`

	- `s` consists only of lowercase English letters.
