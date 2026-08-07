## Description

Given an array of strings `strs`, group the <span data-keyword="anagram">anagrams</span> together. You can return the answer in **any order**.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">strs = ["eat","tea","tan","ate","nat","bat"]</span>

**Output:** <span class="example-io">[["bat"],["nat","tan"],["ate","eat","tea"]]</span>

**Explanation:**

	- There is no string in strs that can be rearranged to form `"bat"`.

	- The strings `"nat"` and `"tan"` are anagrams as they can be rearranged to form each other.

	- The strings `"ate"`, `"eat"`, and `"tea"` are anagrams as they can be rearranged to form each other.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">strs = [""]</span>

**Output:** <span class="example-io">[[""]]</span>

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">strs = ["a"]</span>

**Output:** <span class="example-io">[["a"]]</span>

</div>

**Constraints:**

	- `1 <= strs.length <= 10^4`

	- `0 <= strs[i].length <= 100`

	- `strs[i]` consists of lowercase English letters.
