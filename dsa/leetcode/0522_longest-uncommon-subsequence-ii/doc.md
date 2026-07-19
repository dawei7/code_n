# Longest Uncommon Subsequence II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 522 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Two Pointers, String, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-uncommon-subsequence-ii/) |

## Problem Description
### Goal
Given an array of strings, a subsequence is formed by deleting characters while preserving the remaining order. An uncommon subsequence may be derived from one input string but must not be a subsequence of any other string in the array.

Return the maximum length of any uncommon subsequence, or `-1` when no candidate satisfies that condition. Equal input strings are separate competitors, so their full text cannot be uncommon. A candidate may be the complete source string, and comparison against another string concerns subsequence containment rather than simple equality, substring membership, or frequency alone.

### Function Contract
**Inputs**

- `strs`: an array of lowercase English strings

**Return value**

- The longest uncommon-subsequence length, or `-1` if none exists

### Examples
**Example 1**

- Input: `strs = ["aba", "cdc", "eae"]`
- Output: `3`

**Example 2**

- Input: `strs = ["aaa", "aaa", "aa"]`
- Output: `-1`

**Example 3**

- Input: `strs = ["aabbcc", "aabbcc", "cb", "abc"]`
- Output: `2`
