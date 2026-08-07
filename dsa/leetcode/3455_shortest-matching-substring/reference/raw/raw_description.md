## Description

You are given a string `s` and a pattern string `p`, where `p` contains **exactly two** `'*'` characters.

The `'*'` in `p` matches any sequence of zero or more characters.

Return the length of the **shortest** <span data-keyword="substring">substring</span> in `s` that matches `p`. If there is no such substring, return -1.

**Note:** The empty substring is considered valid.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "abaacbaecebce", p = "ba*c*ce"</span>

**Output:** <span class="example-io">8</span>

**Explanation:**

The shortest matching substring of `p` in `s` is `"<u>**ba**</u>e<u>**c**</u>eb<u>**ce**</u>"`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "baccbaadbc", p = "cc*baa*adb"</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

There is no matching substring in `s`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "a", p = "**"</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

The empty substring is the shortest matching substring.

</div>

**Example 4:**

<div class="example-block">
**Input:** <span class="example-io">s = "madlogic", p = "*adlogi*"</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

The shortest matching substring of `p` in `s` is `"**<u>adlogi</u>**"`.

</div>

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `2 <= p.length <= 10^5`

	- `s` contains only lowercase English letters.

	- `p` contains only lowercase English letters and exactly two `'*'`.
