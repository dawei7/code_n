# Permutation in String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 567 |
| Difficulty | Medium |
| Topics | Hash Table, Two Pointers, String, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/permutation-in-string/) |

## Problem Description
### Goal
Given two strings `s1` and `s2`, determine whether `s2` contains a permutation of `s1`. More precisely, look for a contiguous substring of `s2` whose characters can be rearranged to produce exactly `s1`; the order of those characters inside the substring does not have to match their order in `s1`.

Return `True` when at least one such substring exists and `False` otherwise. A valid substring must have length `len(s1)` and the same multiplicity of every lowercase English letter, so matching only the set of distinct characters is insufficient.

### Function Contract
**Inputs**

- `s1`: the lowercase string whose character multiset must be matched
- `s2`: the lowercase string to search

**Return value**

- `True` if some length-`len(s1)` substring of `s2` has exactly the same character frequencies; otherwise `False`

### Examples
**Example 1**

- Input: `s1 = "ab", s2 = "eidbaooo"`
- Output: `True`

**Example 2**

- Input: `s1 = "ab", s2 = "eidboaoo"`
- Output: `False`

**Example 3**

- Input: `s1 = "adc", s2 = "dcda"`
- Output: `True`
