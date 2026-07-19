# Word Break II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 140 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Dynamic Programming, Backtracking, Trie, Memoization |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/word-break-ii/) |

## Problem Description
### Goal
Given a string and a dictionary of unique nonempty words, insert spaces so that every resulting token is a dictionary entry. A sentence must consume the entire string from left to right without deleting, rearranging, or leaving unmatched characters, and dictionary words may be reused.

Return all distinct valid sentences, preserving the original characters inside each sentence and separating adjacent words with one space. Different choices of boundaries must all be included, while partial segmentations are excluded. The sentences may appear in any order. If no complete segmentation exists, return an empty list rather than the original unsegmented string.

### Function Contract
**Inputs**

- `s`: the string to segment
- `word_dict`: available nonempty words

**Return value**

All valid fully segmented sentences in any order.

### Examples
**Example 1**

- Input: `s = "catsanddog", word_dict = ["cat","cats","and","sand","dog"]`
- Output: `["cats and dog", "cat sand dog"]`

**Example 2**

- Input: `s = "pineapplepenapple", word_dict = ["apple","pen","applepen","pine","pineapple"]`
- Output: three valid sentences

**Example 3**

- Input: `s = "catsandog", word_dict = ["cats","dog","sand","and","cat"]`
- Output: `[]`
