## Description

We call a string `s` of **even** length `n` an **anti-palindrome** if for each index `0 <= i < n`, `s[i] != s[n - i - 1]`.

Given a string `s`, your task is to make `s` an **anti-palindrome** by doing **any** number of operations (including zero).

In one operation, you can select two characters from `s` and swap them.

Return *the resulting string. If multiple strings meet the conditions, return the <span data-keyword="lexicographically-smaller-string">lexicographically smallest</span> one. If it can't be made into an anti-palindrome, return *`"-1"`*.*

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "abca"</span>

**Output:** <span class="example-io">"aabc"</span>

**Explanation:**

`"aabc"` is an anti-palindrome string since `s[0] != s[3]` and `s[1] != s[2]`. Also, it is a rearrangement of `"abca"`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "abba"</span>

**Output:** <span class="example-io">"aabb"</span>

**Explanation:**

`"aabb"` is an anti-palindrome string since `s[0] != s[3]` and `s[1] != s[2]`. Also, it is a rearrangement of `"abba"`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "cccd"</span>

**Output:** <span class="example-io">"-1"</span>

**Explanation:**

You can see that no matter how you rearrange the characters of `"cccd"`, either `s[0] == s[3]` or `s[1] == s[2]`. So it can not form an anti-palindrome string.

</div>

**Constraints:**

	- `2 <= s.length <= 10^5`

	- `s.length % 2 == 0`

	- `s` consists only of lowercase English letters.
