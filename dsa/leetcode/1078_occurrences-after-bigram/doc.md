# Occurrences After Bigram

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1078 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/occurrences-after-bigram/) |

## Problem Description

### Goal

Two given strings, `first` and `second`, define a bigram. Within `text`, consider every consecutive three-word occurrence of the form `first second third`: `second` must come immediately after `first`, and `third` must come immediately after `second`.

Return an array containing the word `third` from every such occurrence, preserving the occurrences' order in `text`. The text contains lowercase English words separated by single spaces, with no leading or trailing space; `first` and `second` also contain only lowercase English letters.

### Function Contract

**Inputs**

- `text`: a sentence of $N$ characters and $W$ single-space-separated words, with $1 \le N \le 1000$.
- `first`: the first bigram word, with length from 1 through 10.
- `second`: the second bigram word, with length from 1 through 10.

**Return value**

- A list of every word immediately following a consecutive `first second` pair, in sentence order.

### Examples

**Example 1**

- Input: `text = "alice is a good girl she is a good student"`, `first = "a"`, `second = "good"`
- Output: `["girl", "student"]`

**Example 2**

- Input: `text = "we will we will rock you"`, `first = "we"`, `second = "will"`
- Output: `["we", "rock"]`
