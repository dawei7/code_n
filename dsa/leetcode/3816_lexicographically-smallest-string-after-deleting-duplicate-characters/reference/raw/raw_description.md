## Description

You are given a string `s` that consists of lowercase English letters.

You can perform the following operation any number of times (possibly zero times):

	- Choose any letter that appears **at least twice** in the current string `s` and delete any **one** occurrence.

Return the **<span data-keyword="lexicographically-smaller-string">lexicographically smallest</span>** resulting string that can be formed this way.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "aaccb"</span>

**Output:** <span class="example-io">"aacb"</span>

**Explanation:**

We can form the strings `"acb"`, `"aacb"`, `"accb"`, and `"aaccb"`. `"aacb"` is the lexicographically smallest one.

For example, we can obtain `"aacb"` by choosing `'c'` and deleting its first occurrence.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "z"</span>

**Output:** <span class="example-io">"z"</span>

**Explanation:**

We cannot perform any operations. The only string we can form is `"z"`.

</div>

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` contains lowercase English letters only.
