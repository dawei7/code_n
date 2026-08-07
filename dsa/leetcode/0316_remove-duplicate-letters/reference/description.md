## Description

Given a string `s`, remove duplicate letters so that every letter appears once and only once. You must make sure your result is **the smallest in lexicographical order** among all possible results.
### Function Contract

**Inputs**

- `s`: A nonempty string of lowercase English letters.

**Return value**

Return the lexicographically smallest subsequence that contains each distinct letter from `s` exactly once.

### Examples
#### Example 1

- **Input:** `s = "bcabc"`
- **Output:** `"abc"`
#### Example 2

- **Input:** `s = "cbacdcbc"`
- **Output:** `"acdb"`
### Constraints

- $1 \le \text{s.length} \le 10^{4}$

- `s` consists of lowercase English letters.

**Note:** This question is the same as 1081: <a href="https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/" target="_blank">https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/</a>