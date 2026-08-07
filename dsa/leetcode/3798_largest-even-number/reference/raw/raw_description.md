## Description

You are given a string `s` consisting only of the characters `'1'` and `'2'`.

You may delete any number of characters from `s` without changing the order of the remaining characters.

Return the **largest possible resultant string** that represents an **even** integer. If there is no such string, return the empty string `""`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "1112"</span>

**Output:** <span class="example-io">"1112"</span>

**Explanation:**

The string already represents the largest possible even number, so no deletions are needed.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "221"</span>

**Output:** <span class="example-io">"22"</span>

**Explanation:**

Deleting `'1'` results in the largest possible even number which is equal to 22.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "1"</span>

**Output:** <span class="example-io">""</span>

**Explanation:**

There is no way to get an even number.

</div>

**Constraints:**

	- `1 <= s.length <= 100`

	- `s` consists only of the characters `'1'` and `'2'`.
