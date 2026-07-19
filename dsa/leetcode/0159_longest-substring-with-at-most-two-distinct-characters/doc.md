# Longest Substring with At Most Two Distinct Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 159 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/) |

## Problem Description
### Goal
Given a string, consider its contiguous substrings and the set of character values present in each one. A substring is valid when that set contains at most two distinct characters, regardless of how many times either character repeats or how their occurrences alternate.

Return the maximum length of any valid substring. The selected characters do not have to be adjacent to each other exclusively, but the substring itself cannot skip positions or join separate intervals. A substring containing only one distinct character is allowed, the entire string is valid when it uses no more than two characters, and an empty input returns `0`.

### Function Contract
**Inputs**

- `s`: a string

**Return value**

The length of its longest substring whose character set has size at most two.

### Examples
**Example 1**

- Input: `s = "eceba"`
- Output: `3`

**Example 2**

- Input: `s = "ccaabbb"`
- Output: `5`

**Example 3**

- Input: `s = "a"`
- Output: `1`
