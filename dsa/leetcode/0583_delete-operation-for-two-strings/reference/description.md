## Description

Given two strings `word1` and `word2`, return *the minimum number of **steps** required to make* `word1` *and* `word2` *the same*.

In one **step**, you can delete exactly one character in either string.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** $word1 = "sea", word2 = "eat"$
- **Output:** `2`
- **Explanation:** You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
#### Example 2

- **Input:** $word1 = "leetcode", word2 = "etco"$
- **Output:** `4`
### Constraints

- $1 \le \text{word1.length}, \text{word2.length} \le 500$

- `word1` and `word2` consist of only lowercase English letters.