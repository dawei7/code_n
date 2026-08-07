## Description

You are given a string `s`.

Your task is to remove **all** digits by doing this operation repeatedly:

	- Delete the *first* digit and the **closest** **non-digit** character to its *left*.

Return the resulting string after removing all digits.

**Note** that the operation *cannot* be performed on a digit that does not have any non-digit character to its left.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "abc"</span>

**Output:** <span class="example-io">"abc"</span>

**Explanation:**

There is no digit in the string.<!-- notionvc: ff07e34f-b1d6-41fb-9f83-5d0ba3c1ecde -->

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "cb34"</span>

**Output:** <span class="example-io">""</span>

**Explanation:**

First, we apply the operation on `s[2]`, and `s` becomes `"c4"`.

Then we apply the operation on `s[1]`, and `s` becomes `""`.

</div>

**Constraints:**

	- `1 <= s.length <= 100`

	- `s` consists only of lowercase English letters and digits.

	- The input is generated such that it is possible to delete all digits.
