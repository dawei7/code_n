# Make String a Subsequence Using Cyclic Increments

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2825 |
| Difficulty | Medium |
| Topics | Two Pointers, String |
| Official Link | [LeetCode](https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/) |

## Problem Description
### Goal

You are given two 0-indexed strings, `str1` and `str2`, containing only lowercase English letters.

You may perform at most one operation. In that operation, choose any set of indices in `str1` and increment the character at every chosen index by one cyclic alphabet step: `a` becomes `b`, `b` becomes `c`, and so on, while `z` wraps to `a`. An index is either left unchanged or incremented once; a character cannot advance by multiple steps.

Determine whether `str2` can be made a subsequence of the resulting `str1`. A subsequence keeps the relative order of its selected characters but may delete any number of the other characters.

### Function Contract
**Inputs**

- `str1`: A lowercase English string with length between $1$ and $10^5$, inclusive.
- `str2`: A lowercase English string with length between $1$ and $10^5$, inclusive.

**Return value**

Return `true` if one allowed choice of indices makes `str2` a subsequence of `str1`; otherwise return `false`.

### Examples
**Example 1**

- Input: `str1 = "abc", str2 = "ad"`
- Output: `true`
- Explanation: Increment the final `c` to `d`; then `ad` is a subsequence of `abd`.

**Example 2**

- Input: `str1 = "zc", str2 = "ad"`
- Output: `true`
- Explanation: Increment `z` to `a` and `c` to `d`, producing `ad`.

**Example 3**

- Input: `str1 = "ab", str2 = "d"`
- Output: `false`
- Explanation: Neither source character is `d` or one cyclic step before `d`.
