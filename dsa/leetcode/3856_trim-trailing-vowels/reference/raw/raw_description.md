## Description

You are given a string `s` that consists of lowercase English letters.

Return the string obtained by removing **all** trailing **vowels** from `s`.

The **vowels** consist of the characters `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "idea"</span>

**Output:** <span class="example-io">"id"</span>

**Explanation:**

Removing `"id<u>**ea**</u>"`, we obtain the string `"id"`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "day"</span>

**Output:** <span class="example-io">"day"</span>

**Explanation:**

There are no trailing vowels in the string `"day"`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "aeiou"</span>

**Output:** <span class="example-io">""</span>

**Explanation:**

Removing `"<u>**aeiou**</u>"`, we obtain the string `""`.

</div>

**Constraints:**

	- `1 <= s.length <= 100`

	- `s` consists of only lowercase English letters.
