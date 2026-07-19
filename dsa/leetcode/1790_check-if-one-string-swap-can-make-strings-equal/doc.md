# Check if One String Swap Can Make Strings Equal

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/) |
| Frontend ID | 1790 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You are given two lowercase strings `s1` and `s2` of equal length. One string swap chooses two indices in one string and exchanges the characters at those positions; the indices are allowed to be the same.

Determine whether the strings can be made equal by performing at most one swap on exactly one of them. Using no swap is allowed when the strings already match. Return `false` if no single exchange within either string can repair every differing position.

### Function Contract

**Inputs**

- `s1`: a lowercase English string of length $n$.
- `s2`: another lowercase English string with the same length, where $1 \le n \le 100$.

**Return value**

- Return `true` if zero or one swap within one string can make `s1` and `s2` equal; otherwise, return `false`.

### Examples

**Example 1**

- Input: `s1 = "bank", s2 = "kanb"`
- Output: `true`

Swapping the first and last characters of either string repairs the two mismatches.

**Example 2**

- Input: `s1 = "attack", s2 = "defend"`
- Output: `false`

One swap cannot repair all differing positions.

**Example 3**

- Input: `s1 = "kelb", s2 = "kelb"`
- Output: `true`

The strings already match, so no operation is required.
