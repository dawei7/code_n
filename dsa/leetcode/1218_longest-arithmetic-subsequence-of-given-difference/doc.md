# Longest Arithmetic Subsequence of Given Difference

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1218 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/) |

## Problem Description

### Goal

Given an integer array `arr` and an integer `difference`, return the length of the longest subsequence of `arr` that forms an arithmetic sequence whose adjacent values have difference exactly `difference`.

A subsequence is formed by deleting any number of elements without changing the relative order of the elements that remain. The selected values need not occupy consecutive positions in `arr`, but every selected value after the first must equal the preceding selected value plus `difference`.

### Function Contract

**Inputs**

- `arr`: An integer array of length $n$, where $1\le n\le10^5$ and $-10^4\le\texttt{arr[i]}\le10^4$.
- `difference`: The required difference between adjacent subsequence values, where $-10^4\le\texttt{difference}\le10^4$.

**Return value**

- The maximum length of an arithmetic subsequence having the given `difference`.

### Examples

**Example 1**

- Input: `arr = [1,2,3,4]`, `difference = 1`
- Output: `4`

The entire array already has the required adjacent difference.

**Example 2**

- Input: `arr = [1,3,5,7]`, `difference = 1`
- Output: `1`

No two values in their existing order differ by `1`, so any single value is optimal.

**Example 3**

- Input: `arr = [1,5,7,8,5,3,4,2,1]`, `difference = -2`
- Output: `4`

One longest valid subsequence is `[7,5,3,1]`.
