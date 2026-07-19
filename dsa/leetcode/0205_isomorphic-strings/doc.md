# Isomorphic Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 205 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/isomorphic-strings/) |

## Problem Description
### Goal
Given two strings `s` and `t` of equal length, decide whether the characters of `s` can be replaced consistently to produce `t`. Every occurrence of one source character must map to the same target character while preserving character positions and order.

The mapping must also be one-to-one: two different source characters cannot both map to the same target character, although a character may map to itself. Return `True` exactly when such a complete correspondence exists. Matching character counts alone is insufficient when their occurrence patterns differ, and the strings themselves must not be modified during the comparison.

### Function Contract
**Inputs**

- `s`: the source string
- `t`: a string of the same length

**Return value**

`True` exactly when each source character maps to one target character and no two source characters share a target.

### Examples
**Example 1**

- Input: `s = "egg", t = "add"`
- Output: `True`

**Example 2**

- Input: `s = "foo", t = "bar"`
- Output: `False`

**Example 3**

- Input: `s = "paper", t = "title"`
- Output: `True`
