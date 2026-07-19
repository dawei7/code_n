# Shortest Word Distance

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 243 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-word-distance/) |

## Problem Description
### Goal
Given a list of words and two distinct target strings known to occur in it, choose one occurrence of `word1` and one occurrence of `word2`. Their distance is the absolute difference between their zero-based positions in the list.

Return the minimum distance over all valid pairs of target occurrences. Each word may appear several times, so an early pair is not necessarily closest and every relevant occurrence can affect the answer. Because the target strings are distinct, one position cannot represent both targets. Return only the positive distance, not the indices or the words themselves.

### Function Contract
**Inputs**

- `wordsDict`: a list of words containing both targets
- `word1`: the first target word
- `word2`: the distinct second target word

**Return value**

The minimum absolute difference between an index containing `word1` and an index containing `word2`.

### Examples
**Example 1**

- Input: `wordsDict = ["practice","makes","perfect","coding","makes"], word1 = "coding", word2 = "practice"`
- Output: `3`

**Example 2**

- Input: `wordsDict = ["practice","makes","perfect","coding","makes"], word1 = "makes", word2 = "coding"`
- Output: `1`

**Example 3**

- Input: `wordsDict = ["a","b"], word1 = "a", word2 = "b"`
- Output: `1`
