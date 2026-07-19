# Substrings of Size Three with Distinct Characters

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/) |
| Frontend ID | 1876 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String, Sliding Window, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A substring is a contiguous portion of a string. Call a substring good when none of its characters repeat. Given a lowercase English string `s`, count the good substrings whose length is exactly three.

Every starting position defines a separate occurrence. Consequently, if the same three-character text appears at several positions, each occurrence is counted. Windows may overlap, and a string shorter than three contributes no qualifying substring because it contains no window of the required size.

### Function Contract

**Inputs**

- `s`: a lowercase English string with $1 \le \lvert s\rvert \le 100$.
- Let $N = \lvert s\rvert$.

**Return value**

- Return the number of indices $i$ for which `s[i:i+3]` exists and its three characters are pairwise distinct.

### Examples

**Example 1**

- Input: `s = "xyzzaz"`
- Output: `1`

Among `"xyz"`, `"yzz"`, `"zza"`, and `"zaz"`, only `"xyz"` has three distinct characters.

**Example 2**

- Input: `s = "aababcabc"`
- Output: `4`

The good occurrences are `"abc"`, `"bca"`, `"cab"`, and the later `"abc"`.

**Example 3**

- Input: `s = "abca"`
- Output: `2`

Both overlapping windows, `"abc"` and `"bca"`, are good.
