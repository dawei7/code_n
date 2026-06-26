# Interleaving String

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_199` |
| Frontend ID | 97 |
| Difficulty | Medium |
| Topics | String, Dynamic Programming |
| Official Link | [interleaving-string](https://leetcode.com/problems/interleaving-string/) |

## Problem Description & Examples
### Goal
Given strings `s1`, `s2`, and `s3`, find whether `s3` is formed by an interleaving of `s1` and `s2`.

An interleaving of two strings `s` and `t` is a configuration where they are divided into non-empty substrings such that:
- `s = s_1 + s_2 + ... + s_n`
- `t = t_1 + t_2 + ... + t_m`
- `|n - m| <= 1`
- The interleaving is `s_1 + t_1 + s_2 + t_2 ...` or `t_1 + s_1 + t_2 + s_2 ...`

### Function Contract
**Inputs**

- `s1`: str
- `s2`: str
- `s3`: str

**Return value**

bool - true if s3 is interleaving of s1 and s2

### Examples
**Example 1**

- Input: `s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"`
- Output: `True`

**Example 2**

- Input: `s1 = 'ab', s2 = 'bb', s3 = 'bbab'`
- Output: `True`

**Example 3**

- Input: `s1 = 'ba', s2 = 'bb', s3 = 'babc'`
- Output: `False`

---

## Underlying Base Algorithm(s)
- [Longest common subsequence](dp_04_longest-common-subsequence.md)
- [Edit distance](dp_08_edit-distance.md)
- [Unique paths](dp_10_unique-paths.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
