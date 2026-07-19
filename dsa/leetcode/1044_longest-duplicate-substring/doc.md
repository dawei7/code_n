# Longest Duplicate Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1044 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Binary Search, Sliding Window, Rolling Hash, Suffix Array, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/longest-duplicate-substring/) |

## Problem Description

### Goal

Given a string `s`, consider every duplicated substring. A substring is a contiguous sequence of characters, and it is duplicated when the same sequence occurs at two or more distinct starting positions in `s`. The occurrences do not need to be disjoint, so they are allowed to overlap and may share characters from the original string.

Among all such repeated sequences, return any one whose length is as large as possible. Multiple answers of that maximum length are equally valid. If no nonempty contiguous substring occurs at least twice, return the empty string `""`.

### Function Contract

**Inputs**

- `s`: a string of length $N$, where $2 \le N \le 3\cdot10^4$, consisting only of lowercase English letters.

**Return value**

- Any longest contiguous substring with at least two occurrences in `s`, or `""` when no duplicated substring exists.

### Examples

**Example 1**

- Input: `s = "banana"`
- Output: `"ana"`
- Explanation: `"ana"` occurs beginning at indices `1` and `3`; those occurrences overlap.

**Example 2**

- Input: `s = "abcd"`
- Output: `""`
- Explanation: No nonempty substring occurs twice.
