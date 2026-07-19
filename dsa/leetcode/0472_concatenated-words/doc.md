# Concatenated Words

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 472 |
| Difficulty | Hard |
| Topics | Array, String, Dynamic Programming, Depth-First Search, Trie, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/concatenated-words/) |

## Problem Description
### Goal
Given a list of unique nonempty words, identify each word that can be formed by concatenating at least two shorter words from the same dictionary. Component words may be reused when their text is needed more than once, and their order must reproduce the candidate exactly.

Return all concatenated words, with output order semantically unrestricted. A word cannot qualify by using itself as its only component, and every character must be covered without overlap or leftover suffixes. Every component must consume at least one character. Different valid segmentations still produce one output occurrence for the candidate word.

### Function Contract
**Inputs**

- `words`: a list of distinct strings

**Return value**

- All concatenated words. Output order is not semantically significant; the app reference preserves their length-sorted processing order.

### Examples
**Example 1**

- Input: `words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]`
- Output: `["dogcatsdog", "catsdogcats", "ratcatdogcat"]`

**Example 2**

- Input: `words = ["cat", "dog", "catdog"]`
- Output: `["catdog"]`

**Example 3**

- Input: `words = ["a", "aa", "aaa"]`
- Output: `["aa", "aaa"]`
