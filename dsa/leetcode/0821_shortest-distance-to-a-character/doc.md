# Shortest Distance to a Character

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 821 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-distance-to-a-character/) |

## Problem Description

### Goal

Given a string `s` and a character `c` that occurs at least once in `s`, produce an integer array `answer` having the same length as the string.

For every zero-based index `i`, set `answer[i]` to the distance from `i` to the closest occurrence of `c`. The distance between indices `i` and `j` is the absolute difference $\left\lvert i - j \right\rvert$. When occurrences on both sides are equally close, the numerical distance is the same, so no occurrence index needs to be chosen or returned.

### Function Contract

**Inputs**

- `s`: a nonempty lowercase English string
- `c`: one lowercase English character guaranteed to occur in `s`

**Return value**

- A length-`len(s)` integer list whose position $i$ is $\min_{j:s_j=c} \lvert i-j \rvert$

### Examples

**Example 1**

- Input: `s = "loveleetcode", c = "e"`
- Output: `[3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]`

**Example 2**

- Input: `s = "aaab", c = "b"`
- Output: `[3, 2, 1, 0]`

**Example 3**

- Input: `s = "baaaab", c = "b"`
- Output: `[0, 1, 2, 2, 1, 0]`
