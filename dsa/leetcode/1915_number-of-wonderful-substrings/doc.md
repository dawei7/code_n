# Number of Wonderful Substrings

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/number-of-wonderful-substrings/) |
| Frontend ID | 1915 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Bit Manipulation, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A string is wonderful when at most one distinct letter occurs an odd number of times. You are given `word`, whose characters are restricted to the first ten lowercase English letters from `a` through `j`.

Count the non-empty contiguous substrings of `word` that are wonderful. Substrings are identified by their positions, so equal text appearing at different locations contributes once for each occurrence.

### Function Contract

**Inputs**

- `word`: a string of length $N$ containing only letters from `a` through `j`.
- $1 \le N \le 10^5$.

**Return value**

- Return the number of non-empty substrings in which at most one letter has odd frequency.

### Examples

**Example 1**

- Input: `word = "aba"`
- Output: `4`

The three one-letter substrings and the complete string are wonderful.

**Example 2**

- Input: `word = "aabb"`
- Output: `9`

Every substring except `"ab"` at either middle boundary is wonderful.

**Example 3**

- Input: `word = "he"`
- Output: `2`

Each single character is wonderful, while `"he"` has two odd counts.
