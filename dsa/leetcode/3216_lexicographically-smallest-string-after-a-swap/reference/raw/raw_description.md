## Description

Given a string `s` containing only digits, return the <span data-keyword="lexicographically-smaller-string">lexicographically smallest string</span> that can be obtained after swapping **adjacent** digits in `s` with the same **parity** at most **once**.

Digits have the same parity if both are odd or both are even. For example, 5 and 9, as well as 2 and 4, have the same parity, while 6 and 9 do not.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "45320"</span>

**Output:** <span class="example-io">"43520"</span>

**Explanation: **

`s[1] == '5'` and `s[2] == '3'` both have the same parity, and swapping them results in the lexicographically smallest string.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "001"</span>

**Output:** <span class="example-io">"001"</span>

**Explanation:**

There is no need to perform a swap because `s` is already the lexicographically smallest.

</div>

**Constraints:**

	- `2 <= s.length <= 100`

	- `s` consists only of digits.
