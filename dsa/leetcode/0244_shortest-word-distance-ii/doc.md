# Shortest Word Distance II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 244 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Two Pointers, String, Design |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-word-distance-ii/) |

## Problem Description
### Goal
Construct a `WordDistance` service for a fixed list of words that may contain repeated entries. After construction, multiple queries provide two distinct words known to exist in that original list, without changing the list between calls.

For each `shortest(word1, word2)` query, return the minimum absolute difference between an occurrence index of the first word and an occurrence index of the second. Process queries independently and preserve construction-time index information so repeated requests do not rescan unrelated words unnecessarily. The app adapter returns query answers in order; the native interface exposes the same behavior through persistent method calls.

### Function Contract
**Inputs**

- `wordsDict`: the fixed list of words to index
- `queries`: a list of `[word1, word2]` pairs; each pair contains distinct words present in the list

**Return value**

A list containing the minimum index distance for each query in order.

### Examples
**Example 1**

- Input: `wordsDict = ["practice","makes","perfect","coding","makes"], queries = [["coding","practice"],["makes","coding"]]`
- Output: `[3,1]`

**Example 2**

- Input: `wordsDict = ["a","b","a","c"], queries = [["a","c"],["a","b"]]`
- Output: `[1,1]`

**Example 3**

- Input: `wordsDict = ["x","y"], queries = [["x","y"]]`
- Output: `[1]`
