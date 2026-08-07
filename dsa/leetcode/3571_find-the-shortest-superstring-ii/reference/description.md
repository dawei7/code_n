## Description

You are given **two** strings, `s1` and `s2`. Return the **shortest** *possible* string that contains both `s1` and `s2` as substrings. If there are multiple valid answers, return *any *one of them.

A **substring** is a contiguous sequence of characters within a string.
### Function Contract

- Refer to method signature.

### Examples
#### Example 1

<div class="example-block">
**Input:** s1 = "aba", s2 = "bab"

**Output:** "abab"

**Explanation:**

`"abab"` is the shortest string that contains both `"aba"` and `"bab"` as substrings.

</div>
#### Example 2

<div class="example-block">
**Input:** s1 = "aa", s2 = "aaa"

**Output:** "aaa"

**Explanation:**

`"aa"` is already contained within `"aaa"`, so the shortest superstring is `"aaa"`.

</div>
### Constraints

- $1 \le \text{s1.length} \le 100$

- $1 \le \text{s2.length} \le 100$

- `s1` and `s2` consist of lowercase English letters only.