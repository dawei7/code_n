# Number of Matching Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 792 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Binary Search, Dynamic Programming, Trie, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-matching-subsequences/) |

## Problem Description

### Goal

Given a source string `s` and an array of nonempty strings `words`, determine which words are subsequences of `s`. A subsequence is formed by deleting zero or more characters from `s` without changing the relative order of those that remain.

Return the number of matching entries in `words`. Each array position is counted separately, so repeated copies of the same word each contribute when that word is a subsequence. The matched characters do not need to be contiguous in `s`.

### Function Contract

**Inputs**

- `s`: a nonempty lowercase source string.
- `words`: a list of nonempty lowercase candidate strings.

**Return value**

- The number of candidates that can be formed by deleting zero or more characters from `s` without reordering the remaining characters.

### Examples

**Example 1**

- Input: `s = "abcde", words = ["a","bb","acd","ace"]`
- Output: `3`
- Explanation: `a`, `acd`, and `ace` are subsequences; `bb` is not.

**Example 2**

- Input: `s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]`
- Output: `2`
- Explanation: The first two words can be matched in order.

**Example 3**

- Input: `s = "aaaa", words = ["a","aa","aaa","aaaa","aaaaa"]`
- Output: `4`
- Explanation: Every candidate except the length-five word fits.
