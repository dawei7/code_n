# Most Common Word

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 819 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/most-common-word/) |

## Problem Description

### Goal

You are given a paragraph containing ASCII letters, spaces, and common punctuation, together with a list of banned words. Words are maximal consecutive groups of letters: punctuation and whitespace separate them, and capitalization does not distinguish one occurrence from another.

Normalize the paragraph's words to lowercase, discard every occurrence whose normalized form is banned, and return the word that appears most often among those remaining. The input guarantees that one allowed word has a strictly greater frequency than every other allowed word, so the result is unambiguous and must be returned in lowercase.

### Function Contract

**Inputs**

- `paragraph`: ASCII letters separated by spaces and punctuation from `!?',;.`.
- `banned`: distinct lowercase words that must not be counted.

**Return value**

- The uniquely most frequent non-banned word, written in lowercase.

### Examples

**Example 1**

- Input: `paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]`
- Output: `"ball"`
- Explanation: After case folding and excluding `hit`, `ball` is the only word appearing twice.

**Example 2**

- Input: `paragraph = "a, a, a, a, b,b,b,c, c", banned = ["a"]`
- Output: `"b"`
- Explanation: Punctuation separates the words, and `b` occurs three times among the allowed words.

**Example 3**

- Input: `paragraph = "Bob. hIt, baLl", banned = ["bob","hit"]`
- Output: `"ball"`
- Explanation: Comparisons are case-insensitive, and the result is normalized to lowercase.
