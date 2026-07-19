# Valid Anagram

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 242 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-anagram/) |

## Problem Description
### Goal
Given two strings `s` and `t` made from lowercase English letters, determine whether `t` is an anagram of `s`. An anagram may reorder characters arbitrarily but must use exactly the characters supplied by the original string.

Return `True` only when both strings have the same length and every letter occurs with the same multiplicity in each one. Matching sets of letters are insufficient when their counts differ, and no character may be added, deleted, or substituted. A one-character string is an anagram only of the same character, while a length mismatch immediately makes the answer `False`.

### Function Contract
**Inputs**

- `s`: a lowercase English string
- `t`: another lowercase English string

**Return value**

`True` when `t` is an anagram of `s`; otherwise `False`.

### Examples
**Example 1**

- Input: `s = "anagram", t = "nagaram"`
- Output: `True`

**Example 2**

- Input: `s = "rat", t = "car"`
- Output: `False`

**Example 3**

- Input: `s = "", t = ""`
- Output: `True`
