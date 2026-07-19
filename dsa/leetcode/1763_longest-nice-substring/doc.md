# Longest Nice Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1763 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String, Divide and Conquer, Bit Manipulation, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-nice-substring/) |

## Problem Description

### Goal

You are given a string `s` containing uppercase and lowercase English letters. A string is nice when every alphabetic letter that appears in it is represented in both cases: if lowercase `a` occurs, uppercase `A` must also occur, and conversely.

Find the longest contiguous substring of `s` that is nice. When several qualifying substrings have the same maximum length, return the one that begins earliest. If no nonempty nice substring exists, return the empty string.

### Function Contract

**Inputs**

- `s`: a string of uppercase and lowercase English letters with $1 \le n \le 100$, where $n=\lvert s\rvert$.

**Return value**

- Return the longest contiguous substring in which every appearing letter has both its lowercase and uppercase forms.
- Resolve equal maximum lengths by choosing the earliest starting position, and return `""` if none exists.

### Examples

**Example 1**

- Input: `s = "YazaAay"`
- Output: `"aAa"`
- Explanation: The returned substring contains both `a` and `A`; no longer substring satisfies the paired-case condition.

**Example 2**

- Input: `s = "Bb"`
- Output: `"Bb"`
- Explanation: Both cases of `b` occur, so the complete string is nice.

**Example 3**

- Input: `s = "c"`
- Output: `""`
- Explanation: The only appearing letter lacks its uppercase counterpart.
