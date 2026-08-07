### 1. Description

The **count-and-say** sequence is a sequence of digit strings defined by the recursive formula:

- $countAndSay(1) = "1"$

- `countAndSay(n)` is the run-length encoding of $countAndSay(n - 1)$.

<a href="http://en.wikipedia.org/wiki/Run-length_encoding" target="_blank">Run-length encoding</a> (RLE) is a string compression method that works by replacing each maximal group of consecutive identical characters with the concatenation of the length of the group followed by the character itself. For example, to compress the string `"3322251"` we replace `"33"` with `"23"`, replace `"222"` with `"32"`, replace `"5"` with `"15"`, and replace `"1"` with `"11"`. Thus the compressed string becomes `"23321511"`.

Given a positive integer `n`, return *the *$$n^{\text{th}}$$* element of the **count-and-say** sequence*.

### 2. Function Contract

**Inputs**

- `n`: The one-based position of the requested sequence term.

Let $L_n$ denote the number of characters in the $n$th term.

**Return value**

Return the $n$th count-and-say term as a digit string.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** n = 4

**Output:** "1211"

**Explanation:**

```
countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
countAndSay(4) = RLE of "21" = "1211"
```

</div>
#### Example 2

<div class="example-block">
**Input:** n = 1

**Output:** "1"

**Explanation:**

This is the base case.

</div>

### 4. Constraints

- $1 \le n \le 30$

**Follow up:** Could you solve it iteratively?