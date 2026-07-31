# Words Within Two Edits of Dictionary

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2452 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Words Within Two Edits of Dictionary](https://leetcode.com/problems/words-within-two-edits-of-dictionary/) |

## Problem Description

### Goal

You are given two string arrays, `queries` and `dictionary`. Every word in both arrays consists of lowercase English letters, and all words have the same length. One edit selects a character of a query word and replaces it with any other letter.

Return every query that can be made equal to at least one dictionary word using at most two edits. Zero edits are allowed, so an exact dictionary match qualifies. Preserve the order in which qualifying words occur in `queries`.

### Function Contract

**Inputs**

- `queries`: A list of $Q$ lowercase words to test, where $1 \le Q \le 100$.
- `dictionary`: A list of $D$ lowercase reference words, where $1 \le D \le 100$.

All words have one shared length $n$, where $1 \le n \le 100$.

**Return value**

- The qualifying query words in their original order. A query qualifies when its Hamming distance from some dictionary word is at most 2.

### Examples

**Example 1**

- Input: `queries = ["word", "note", "ants", "wood"], dictionary = ["wood", "joke", "moat"]`
- Output: `["word", "note", "wood"]`
- Explanation: The three returned queries need one, two, and zero substitutions respectively; `"ants"` needs more than two against every dictionary word.

**Example 2**

- Input: `queries = ["yes"], dictionary = ["not"]`
- Output: `[]`
- Explanation: All three positions differ, so two edits cannot create a match.
