# Word Ladder II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 126 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, String, Backtracking, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/word-ladder-ii/) |

## Problem Description
### Goal
Given two words of equal length and a `wordList` containing unique allowed words, transform `beginWord` into `endWord` by changing exactly one character at a time. Every word produced after the starting word, including the destination, must occur in `wordList`, and each intermediate form must have the same length.

Return all transformation sequences that use the minimum possible number of words, with both endpoints included in every sequence. Longer valid sequences must be omitted, while distinct shortest routes through different intermediate words must all be retained. Outer sequence order is irrelevant. If the destination is unavailable or cannot be reached through valid one-letter changes, return an empty list.

### Function Contract
**Inputs**

- `beginWord`: the first word in every sequence
- `endWord`: the required final word
- `wordList`: allowed transformed words, all with the same length

**Return value**

All shortest valid word sequences. Outer sequence order does not matter; word order inside each sequence does.

### Examples
**Example 1**

- Input: `beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]`
- Output: `[["hit","hot","dot","dog","cog"], ["hit","hot","lot","log","cog"]]`

**Example 2**

- Input: the same words without `"cog"`
- Output: `[]`

**Example 3**

- Input: `beginWord = "a", endWord = "c", wordList = ["a","b","c"]`
- Output: `[["a","c"]]`
