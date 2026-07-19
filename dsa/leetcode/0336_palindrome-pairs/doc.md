# Palindrome Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 336 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Trie, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/palindrome-pairs/) |

## Problem Description
### Goal
Given a list of unique lowercase strings, find ordered pairs of distinct indices `[i, j]` such that concatenating `words[i]` followed by `words[j]` produces a palindrome. Reversing the pair changes the concatenation and is a separate candidate.

Return every valid ordered pair in any order, with no duplicate index pair and never pairing an index with itself. Both directions should appear when both concatenations are palindromic. The empty string may pair with any nonempty word that is already a palindrome. Evaluate the entire concatenated text; matching only a prefix or suffix is insufficient.

### Function Contract
**Inputs**

- `words`: unique lowercase strings, possibly including the empty string

**Return value**

A list of all ordered index pairs forming palindromic concatenations, in any outer-list order.

### Examples
**Example 1**

- Input: `words = ["abcd","dcba","lls","s","sssll"]`
- Output: `[[0,1],[1,0],[3,2],[2,4]]`

**Example 2**

- Input: `words = ["bat","tab","cat"]`
- Output: `[[0,1],[1,0]]`

**Example 3**

- Input: `words = ["a",""]`
- Output: `[[0,1],[1,0]]`
