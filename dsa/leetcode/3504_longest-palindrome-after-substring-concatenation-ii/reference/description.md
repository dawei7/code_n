## Description

You are given two strings, `s` and `t`.

You can create a new string by selecting a substring from `s` (possibly empty) and a substring from `t` (possibly empty), then concatenating them **in order**.

Return the length of the **longest** palindrome that can be formed this way.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** s = "a", t = "a"

**Output:** 2

**Explanation:**

Concatenating `"a"` from `s` and `"a"` from `t` results in `"aa"`, which is a palindrome of length 2.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "abc", t = "def"

**Output:** 1

**Explanation:**

Since all characters are different, the longest palindrome is any single character, so the answer is 1.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "b", t = "aaaa"

**Output:** 4

**Explanation:**

Selecting "`aaaa`" from `t` is the longest palindrome, so the answer is 4.

</div>
#### Example 4

<div class="example-block">
**Input:** s = "abcde", t = "ecdba"

**Output:** 5

**Explanation:**

Concatenating `"abc"` from `s` and `"ba"` from `t` results in `"abcba"`, which is a palindrome of length 5.

</div>
### Constraints

- $1 \le \text{s.length}, \text{t.length} \le 1000$

- `s` and `t` consist of lowercase English letters.