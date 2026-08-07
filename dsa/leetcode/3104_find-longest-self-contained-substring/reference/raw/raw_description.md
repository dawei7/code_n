## Description

Given a string `s`, your task is to find the length of the **longest self-contained** <span data-keyword="substring-nonempty">substring</span> of `s`.

A substring `t` of a string `s` is called **self-contained **if `t != s` and for every character in `t`, it doesn't exist in the *rest* of `s`.

Return the length of the *longest** **self-contained *substring of `s` if it exists, otherwise, return -1.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "abba"</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

Let's check the substring `"bb"`. You can see that no other `"b"` is outside of this substring. Hence the answer is 2.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "abab"</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

Every substring we choose does not satisfy the described property (there is some character which is inside and outside of that substring). So the answer would be -1.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "abacd"</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

Let's check the substring `"<span class="example-io">abac</span>"`. There is only one character outside of this substring and that is `"d"`. There is no `"d"` inside the chosen substring, so it satisfies the condition and the answer is 4.

</div>

**Constraints:**

	- `2 <= s.length <= 5 * 10^4`

	- `s` consists only of lowercase English letters.
