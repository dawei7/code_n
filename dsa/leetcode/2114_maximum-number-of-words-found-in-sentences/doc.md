# Maximum Number of Words Found in Sentences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2114 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/) |

## Problem Description
### Goal

A sentence consists of one or more words separated by single spaces. It has no
space before its first word or after its last word.

Given an array `sentences` in which every string follows that format, determine
the greatest number of words appearing in any one sentence. More than one
sentence may attain the maximum; only the word count is required.

### Function Contract
**Inputs**

- `sentences`: A nonempty list of lowercase English sentences. Every pair of
  consecutive words has exactly one separating space, and no sentence has a
  leading or trailing space.

Let $n = \lvert\texttt{sentences}\rvert$, and let $S$ be the total number of
characters across all sentences:

$$
S = \sum_{s \in \texttt{sentences}} \lvert s \rvert.
$$

**Return value**

Return an integer equal to the maximum number of words in any string in
`sentences`.

### Examples
**Example 1**

- Input: `sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]`
- Output: `6`

The three sentences contain five, four, and six words, respectively.

**Example 2**

- Input: `sentences = ["please wait", "continue to fight", "continue to win"]`
- Output: `3`

The second and third sentences tie for the maximum.

**Example 3**

- Input: `sentences = ["solitary"]`
- Output: `1`

A sentence without a space still contains one word.
