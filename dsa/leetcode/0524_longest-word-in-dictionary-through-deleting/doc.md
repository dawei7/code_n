# Longest Word in Dictionary through Deleting

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 524 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, String, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/) |

## Problem Description
### Goal
Given a string `s` and a dictionary of candidate words, a candidate can be formed by deleting characters from `s` only when its letters appear as a subsequence in the same relative order. Deletions may skip any positions but cannot reorder or substitute characters.

Return the longest dictionary word obtainable this way. If several qualifying words share the maximum length, return the lexicographically smallest one; if none qualifies, return `""`. The function returns the dictionary word itself rather than deleted indices, and a candidate equal to `s` is valid without any deletion.

### Function Contract
**Inputs**

- `s`: the source string
- `dictionary`: an array of candidate words

**Return value**

- The longest candidate that is a subsequence of `s`, using lexicographic order to break ties, or `""` when no candidate qualifies

### Examples
**Example 1**

- Input: `s = "abpcplea", dictionary = ["ale", "apple", "monkey", "plea"]`
- Output: `"apple"`

**Example 2**

- Input: `s = "abpcplea", dictionary = ["a", "b", "c"]`
- Output: `"a"`

**Example 3**

- Input: `s = "bab", dictionary = ["ba", "ab", "a", "b"]`
- Output: `"ab"`
