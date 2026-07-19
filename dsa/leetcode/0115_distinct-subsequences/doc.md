# Distinct Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 115 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/distinct-subsequences/) |

## Problem Description
### Goal
Given two strings `s` and `t`, count the distinct subsequences of `s` that equal `t`. A subsequence is formed by deleting any number of characters from `s` while preserving the relative order of every character that remains; characters cannot be rearranged or reused.

Two results are distinct when they select different source indices, even if repeated characters make the resulting text look identical. Return the total number of valid index selections as an integer. Selecting no characters forms the empty target exactly once, while a nonempty target cannot be formed from an empty source or from a source with too few usable characters.

### Function Contract
**Inputs**

- `s`: the source string from which characters may be deleted
- `t`: the target string that selected characters must form

**Return value**

The number of source subsequences equal to `t`.

### Examples
**Example 1**

- Input: `s = "rabbbit", t = "rabbit"`
- Output: `3`

**Example 2**

- Input: `s = "babgbag", t = "bag"`
- Output: `5`

**Example 3**

- Input: `s = "", t = ""`
- Output: `1`
