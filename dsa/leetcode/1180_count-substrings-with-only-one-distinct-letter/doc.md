# Count Substrings with Only One Distinct Letter

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1180 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/) |

## Problem Description

### Goal

You are given a non-empty lowercase English string `s`. Count its non-empty substrings that contain only one distinct letter. A substring is a contiguous sequence, and occurrences at different index ranges count separately even when their text is identical.

Every single-character substring qualifies, while a longer substring qualifies exactly when all of its positions hold the same letter. Return the total number of qualifying substrings across every possible start and end position in `s`.

### Function Contract

**Inputs**

- `s`: A lowercase English string with $1 \leq \lvert s\rvert \leq 1000$.
- Let $n=\lvert s\rvert$.

**Return value**

- The number of non-empty contiguous substrings whose characters are all equal.

### Examples

**Example 1**

- Input: `s = "aaaba"`
- Output: `8`

The text `"aaa"` occurs once, `"aa"` occurs twice, `"a"` occurs four times, and `"b"` occurs once, for a total of eight occurrences.

**Example 2**

- Input: `s = "aaaaaaaaaa"`
- Output: `55`

**Example 3**

- Input: `s = "abc"`
- Output: `3`
