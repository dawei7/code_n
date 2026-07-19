# Longest Word in Dictionary

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 720 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Trie, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-word-in-dictionary/) |

## Problem Description
### Goal
Given an array `words` representing an English dictionary, find a word that can be built one character at a time using other words in the dictionary. Building proceeds from left to right by appending one character, so every nonempty prefix of the chosen word must also occur in `words`.

Return the longest buildable word. If several answers have the same maximum length, return the lexicographically smallest one. If no word can begin from a one-letter dictionary entry, return the empty string.

### Function Contract
**Inputs**

- `words`: a nonempty array of distinct lowercase English words

**Return value**

- The longest word constructible one character at a time through dictionary prefixes, breaking ties lexicographically; return the empty string if no one-letter starting word exists

### Examples
**Example 1**

- Input: `words = ["w","wo","wor","worl","world"]`
- Output: `"world"`

**Example 2**

- Input: `words = ["a","banana","app","appl","ap","apply","apple"]`
- Output: `"apple"`

**Example 3**

- Input: `words = ["t","to","tea","ted","ten","i","in","inn"]`
- Output: `"inn"`
