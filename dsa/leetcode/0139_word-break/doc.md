# Word Break

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 139 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Dynamic Programming, Trie, Memoization |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/word-break/) |

## Problem Description
### Goal
Given a string and a dictionary of unique nonempty words, determine whether boundaries can divide the entire string into a sequence of dictionary entries. Every character must be used exactly once in its original order, and no unmatched prefix or suffix may remain.

Return `True` when at least one complete segmentation exists and `False` otherwise. A dictionary entry may be reused multiple times, and different word lengths or overlapping candidate prefixes may create several possible boundary choices. Only existence matters: the function does not need to return a chosen segmentation or count how many valid segmentations the string has.

### Function Contract
**Inputs**

- `s`: the string to segment
- `word_dict`: available nonempty words

**Return value**

`True` when a complete dictionary segmentation exists; otherwise `False`.

### Examples
**Example 1**

- Input: `s = "leetcode", word_dict = ["leet", "code"]`
- Output: `True`

**Example 2**

- Input: `s = "applepenapple", word_dict = ["apple", "pen"]`
- Output: `True`

**Example 3**

- Input: `s = "catsandog", word_dict = ["cats", "dog", "sand", "and", "cat"]`
- Output: `False`
