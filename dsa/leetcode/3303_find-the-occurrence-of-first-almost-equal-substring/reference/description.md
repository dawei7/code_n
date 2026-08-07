### 1. Description

You are given two strings `s` and `pattern`.

A string `x` is called **almost equal** to `y` if you can change **at most** one character in `x` to make it *identical* to `y`.

Return the **smallest** *starting index* of a substring in `s` that is **almost equal** to `pattern`. If no such index exists, return `-1`.

A **substring** is a contiguous **non-empty** sequence of characters within a string.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** s = "abcdefg", pattern = "bcdffg"

**Output:** 1

**Explanation:**

The substring $s[1..6] = "bcdefg"$ can be converted to `"bcdffg"` by changing $s[4]$ to `"f"`.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "ababbababa", pattern = "bacaba"

**Output:** 4

**Explanation:**

The substring $s[4..9] = "bababa"$ can be converted to `"bacaba"` by changing $s[6]$ to `"c"`.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "abcd", pattern = "dba"

**Output:** -1

</div>
#### Example 4

<div class="example-block">
**Input:** s = "dde", pattern = "d"

**Output:** 0

</div>

### 4. Constraints

- $1 \le \text{pattern.length} < \text{s.length} \le 10^{5}$

- `s` and `pattern` consist only of lowercase English letters.

### 5. Follow-up

Could you solve the problem if **at most** `k` **consecutive** characters can be changed?