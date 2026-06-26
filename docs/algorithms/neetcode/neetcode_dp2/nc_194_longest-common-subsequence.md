## Problem Description & Examples
### Goal
Given two strings `text1` and `text2`, return the length of their longest common subsequence. If there is no common subsequence, return `0`.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

### Function Contract
**Inputs**

- `text1`: str
- `text2`: str

**Return value**

int - length of LCS

### Examples
**Example 1**

- Input: `text1 = "abcde", text2 = "ace"`
- Output: `3`

**Example 2**

- Input: `text1 = 'biqp', text2 = 'mzjp'`
- Output: `1`

**Example 3**

- Input: `text1 = 'idp', text2 = 'yop'`
- Output: `1`

---

## Underlying Base Algorithm(s)
- [Longest common subsequence](dp_04_longest-common-subsequence.md)
- [Edit distance](dp_08_edit-distance.md)
- [Unique paths](dp_10_unique-paths.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
