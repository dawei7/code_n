## Description

You are given two strings `word1` and `word2`.

A string `x` is called **valid** if `x` can be rearranged to have `word2` as a prefix.

Return the total number of **valid** substrings of `word1`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** word1 = "bcca", word2 = "abc"

**Output:** 1

**Explanation:**

The only valid substring is `"bcca"` which can be rearranged to `"abcc"` having `"abc"` as a prefix.

</div>
#### Example 2

<div class="example-block">
**Input:** word1 = "abcabc", word2 = "abc"

**Output:** 10

**Explanation:**

All the substrings except substrings of size 1 and size 2 are valid.

</div>
#### Example 3

<div class="example-block">
**Input:** word1 = "abcabc", word2 = "aaabc"

**Output:** 0

</div>
### Constraints

- $1 \le \text{word1.length} \le 10^{5}$

- $1 \le \text{word2.length} \le 10^{4}$

- `word1` and `word2` consist only of lowercase English letters.