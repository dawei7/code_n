## Description

A **subsequence** of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"<u>a</u>b<u>c</u>d<u>e</u>"` while `"aec"` is not).

Given two strings `source` and `target`, return *the minimum number of **subsequences** of *`source`* such that their concatenation equals *`target`. If the task is impossible, return `-1`.
### Function Contract

**Inputs**

- `source`: a nonempty string of lowercase English letters.
- `target`: a nonempty string of lowercase English letters.

Each selected piece may delete different characters from a fresh use of `source`, but every retained piece must preserve `source` order. Their concatenation must equal all of `target` exactly.

**Return value**

- The smallest number of subsequences of `source` whose concatenation is `target`, or `-1` when construction is impossible.

### Examples

#### Example 1

- **Input:** $source = "abc", target = "abcbc"$
- **Output:** `2`
- **Explanation:** The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
#### Example 2

- **Input:** $source = "abc", target = "acdbc"$
- **Output:** `-1`
- **Explanation:** The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
#### Example 3

- **Input:** $source = "xyz", target = "xzyxz"$
- **Output:** `3`
- **Explanation:** The target string can be constructed as follows "xz" + "y" + "xz".
### Constraints

- $1 \le \text{source.length}, \text{target.length} \le 1000$

- `source` and `target` consist of lowercase English letters.