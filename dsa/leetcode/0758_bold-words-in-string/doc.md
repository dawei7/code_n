# Bold Words in String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 758 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Trie, String Matching |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/bold-words-in-string/) |

## Problem Description

### Goal

Given a string `s` and a list of words, find every occurrence of every listed word as a contiguous substring of `s`. Mark all character positions covered by at least one complete occurrence.

Return `s` with each maximal marked region enclosed by $<b>$ and $</b>$ tags. Overlapping occurrences and directly consecutive marked ranges share one tag pair, while uncovered characters remain unchanged. A listed word that does not occur contributes no tags.

### Function Contract

**Inputs**

- `words`: a list of non-empty lowercase dictionary words.
- `s`: the lowercase source string to annotate.

**Return value**

- The source string with maximal consecutive covered ranges enclosed in bold tags.

### Examples

**Example 1**

- Input: `words = ["ab", "bc"]`, `s = "aabcd"`
- Output: `"a<b>abc</b>d"`
- Explanation: The overlapping matches `"ab"` and `"bc"` merge into one bold range.

**Example 2**

- Input: `words = ["ab", "cb"]`, `s = "aabcd"`
- Output: `"a<b>ab</b>cd"`
- Explanation: Only `"ab"` occurs in the source.
