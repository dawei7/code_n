# Minimum Cost Good Caption

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3441 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-cost-good-caption/) |

## Problem Description

### Goal

A caption is good when every maximal group of equal characters has length at least three. Thus strings such as `"aaabbb"` and `"aaaaccc"` are good, while `"aabbb"` and `"ccccd"` are not.

In one operation, choose a character and move it one step earlier or later in the lowercase English alphabet, provided that step stays between `a` and `z`. Apply any number of operations to transform the given caption into a good caption with minimum total cost. When several minimum-cost captions exist, return the lexicographically smallest one. Return `""` if no good caption of the same length can exist.

### Function Contract

**Inputs**

- `caption`: A lowercase English string of length $n$, where $1\le n\le5\cdot10^4$.

**Return value**

Return the lexicographically smallest good caption among those requiring the minimum number of single-letter alphabet steps, or `""` when transformation is impossible.

### Examples

**Example 1**

- Input: `caption = "cdcd"`
- Output: `"cccc"`

**Example 2**

- Input: `caption = "aca"`
- Output: `"aaa"`

**Example 3**

- Input: `caption = "bc"`
- Output: `""`
