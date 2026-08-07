## Description

You are given a string `s`, which is known to be a concatenation of **anagrams** of some string `t`.

Return the **minimum** possible length of the string `t`.

An **anagram** is formed by rearranging the letters of a string. For example, "aab", "aba", and, "baa" are anagrams of "aab".
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** s = "abba"

**Output:** 2

**Explanation:**

One possible string `t` could be `"ba"`.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "cdef"

**Output:** 4

**Explanation:**

One possible string `t` could be `"cdef"`, notice that `t` can be equal to `s`.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "abcbcacabbaccba"

**Output:** 3

</div>
### Constraints

- $1 \le \text{s.length} \le 10^{5}$

- `s` consist only of lowercase English letters.