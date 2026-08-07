## Description

You are given a string `s` consisting of one or more words separated by single spaces. Each word in `s` consists of lowercase English letters.

We obtain the **expanded** string `t` from `s` as follows:

	- For each **word** in `s`, repeat its first character once, then its second character twice, and so on.

For example, if `s = "hello world"`, then `t = "heelllllllooooo woorrrllllddddd"`.

You are also given an integer `k`, representing a **valid** index of the string `t`.

Return the `k^th` character of the string `t`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "hello world", k = 0</span>

**Output:** <span class="example-io">"h"</span>

**Explanation:**

`t = "heelllllllooooo woorrrllllddddd"`. Therefore, the answer is `t[0] = "h"`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "hello world", k = 15</span>

**Output:** <span class="example-io">" "</span>

**Explanation:**

`t = "heelllllllooooo woorrrllllddddd"`. Therefore, the answer is `t[15] = " "`.

</div>

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` contains only lowercase English letters and spaces `' '`.

	- `s` **does not contain** any leading or trailing spaces.

	- All the words in `s` are separated by a **single space**.

	- `0 <= k < t.length`. That is, `k` is a **valid** index of `t`.
