# Ransom Note

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 383 |
| Difficulty | Easy |
| Topics | Hash Table, String, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/ransom-note/) |

## Problem Description
### Goal
Given lowercase strings `ransom_note` and `magazine`, determine whether the note can be constructed by selecting character occurrences from the magazine. Character order in the magazine is irrelevant, but each occurrence can be used at most once.

Return `True` only when the magazine supplies at least the required multiplicity of every letter in the note. Having a letter present once is insufficient when the note needs it several times. Extra magazine characters may remain unused. A one-character note is constructible only when that character occurs in the magazine, while any frequency deficit makes the result `False`.

### Function Contract
**Inputs**

- `ransom_note`: a string of lowercase English letters to construct
- `magazine`: the lowercase English letters available for construction

**Return value**

- Return `True` when the magazine contains at least the required multiplicity of every character; otherwise return `False`.

### Examples
**Example 1**

- Input: `ransom_note = "a", magazine = "b"`
- Output: `False`

**Example 2**

- Input: `ransom_note = "aa", magazine = "ab"`
- Output: `False`

**Example 3**

- Input: `ransom_note = "aa", magazine = "aab"`
- Output: `True`
