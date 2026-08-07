## Description

You are given a string `s`. It may contain any number of `'*'` characters. Your task is to remove all `'*'` characters.

While there is a `'*'`, do the following operation:

	- Delete the leftmost `'*'` and the **smallest** non-`'*'` character to its *left*. If there are several smallest characters, you can delete any of them.

Return the <span data-keyword="lexicographically-smaller-string">lexicographically smallest</span> resulting string after removing all `'*'` characters.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "aaba*"</span>

**Output:** <span class="example-io">"aab"</span>

**Explanation:**

We should delete one of the `'a'` characters with `'*'`. If we choose `s[3]`, `s` becomes the lexicographically smallest.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "abc"</span>

**Output:** <span class="example-io">"abc"</span>

**Explanation:**

There is no `'*'` in the string.<!-- notionvc: ff07e34f-b1d6-41fb-9f83-5d0ba3c1ecde -->

</div>

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` consists only of lowercase English letters and `'*'`.

	- The input is generated such that it is possible to delete all `'*'` characters.
