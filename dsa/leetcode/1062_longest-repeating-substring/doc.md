# Longest Repeating Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1062 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Binary Search, Dynamic Programming, Rolling Hash, Suffix Array, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/longest-repeating-substring/) |

## Problem Description

### Goal

Given a lowercase English string `s`, find the greatest length of a non-empty substring that occurs at least twice in the string. The two occurrences are allowed to overlap, so they need distinct starting positions but do not need disjoint index ranges.

Return that greatest length. If no non-empty substring appears more than once, return `0`. Only contiguous substrings count; equal subsequences formed by skipping characters do not satisfy the requirement.

### Function Contract

**Inputs**

- `s`: a lowercase English string of length $N$, where $1 \le N \le 1500$.

**Return value**

- The maximum length of a substring having at least two occurrences, or `0` if none exists.

### Examples

**Example 1**

- Input: `s = "abcd"`
- Output: `0`
- Explanation: Every non-empty substring is unique.

**Example 2**

- Input: `s = "abbaba"`
- Output: `2`
- Explanation: Substrings such as `"ab"` occur more than once, while no length-three substring repeats.

**Example 3**

- Input: `s = "aabcaabdaab"`
- Output: `3`
- Explanation: `"aab"` appears three times.
