# One Edit Distance

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 161 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/one-edit-distance/) |

## Problem Description
### Goal
Given two strings `s` and `t`, decide whether they are exactly one edit distance apart. A single edit may insert one character, delete one character, or replace one existing character with a different character; all unaffected characters must retain their relative order.

Return `True` only when the edit distance is exactly one, not merely at most one. Identical strings therefore return `False`, as do strings whose lengths differ by more than one or whose mismatches require multiple operations. Empty strings follow the same rule: an empty string and a one-character string are one edit apart, while two empty strings are not.

### Function Contract
**Inputs**

- `s`: first string
- `t`: second string

**Return value**

`True` only when exactly one permitted edit transforms one string into the other; identical strings return `False`.

### Examples
**Example 1**

- Input: `s = "ab", t = "acb"`
- Output: `True`

**Example 2**

- Input: `s = "", t = ""`
- Output: `False`

**Example 3**

- Input: `s = "a", t = "A"`
- Output: `True`
