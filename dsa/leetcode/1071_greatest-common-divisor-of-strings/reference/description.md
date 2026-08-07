## Description

For two strings `s` and `t`, we say "`t` divides `s`" if and only if $s = t + t + t + ... + t + t$ (i.e., `t` is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return *the largest string *`x`* such that *`x`* divides both *`str1`* and *`str2`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** str1 = "ABCABC", str2 = "ABC"

**Output:** "ABC"

</div>
#### Example 2

<div class="example-block">
**Input:** str1 = "ABABAB", str2 = "ABAB"

**Output:** "AB"

</div>
#### Example 3

<div class="example-block">
**Input:** str1 = "LEET", str2 = "CODE"

**Output:** ""

</div>
#### Example 4

<div class="example-block">
**Input:** str1 = "AAAAAB", str2 = "AAA"

**Output:** ""​​​​​​​

</div>
### Constraints

- $1 \le \text{str1.length}, \text{str2.length} \le 1000$

- `str1` and `str2` consist of English uppercase letters.