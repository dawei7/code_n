## Description

The **count-and-say** sequence is a sequence of digit strings defined by the recursive formula:

	- `countAndSay(1) = "1"`

	- `countAndSay(n)` is the run-length encoding of `countAndSay(n - 1)`.

<a href="http://en.wikipedia.org/wiki/Run-length_encoding" target="_blank">Run-length encoding</a> (RLE) is a string compression method that works by replacing each maximal group of consecutive identical characters with the concatenation of the length of the group followed by the character itself. For example, to compress the string `"3322251"` we replace `"33"` with `"23"`, replace `"222"` with `"32"`, replace `"5"` with `"15"`, and replace `"1"` with `"11"`. Thus the compressed string becomes `"23321511"`.

Given a positive integer `n`, return *the *`n^th`* element of the **count-and-say** sequence*.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 4</span>

**Output:** <span class="example-io">"1211"</span>

**Explanation:**

```
countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
countAndSay(4) = RLE of "21" = "1211"
```

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 1</span>

**Output:** <span class="example-io">"1"</span>

**Explanation:**

This is the base case.

</div>

**Constraints:**

	- `1 <= n <= 30`

**Follow up:** Could you solve it iteratively?
