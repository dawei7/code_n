## Description

You are given a string `s` and a character `c`. Return *the total number of <span data-keyword="substring-nonempty">substrings</span> of *`s`* that start and end with *`c`*.*

**Example 1:**

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: **<span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">s = "abada", c = "a"</span>

**Output: **<span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">6</span>

**Explanation:** Substrings starting and ending with `"a"` are: `"**<u>a</u>**bada"`, `"<u>**aba**</u>da"`, `"<u>**abada**</u>"`, `"ab<u>**a**</u>da"`, `"ab<u>**ada**</u>"`, `"abad<u>**a**</u>"`.

</div>

**Example 2:**

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: **<span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">s = "zzz", c = "z"</span>

**Output: **<span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">6</span>

**Explanation:** There are a total of `6` substrings in `s` and all start and end with `"z"`.

</div>

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` and `c` consist only of lowercase English letters.
