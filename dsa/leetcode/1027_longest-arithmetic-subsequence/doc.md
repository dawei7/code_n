# Longest Arithmetic Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1027 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/longest-arithmetic-subsequence/) |

## Problem Description

### Goal

Given an integer array `nums`, return the length of its longest arithmetic subsequence.

A subsequence is formed by deleting zero or more elements without changing the relative order of those that remain in the original input array. A sequence `seq` is arithmetic when every adjacent calculation `seq[i + 1] - seq[i]` has the same fixed value for all valid `i`.

### Function Contract

**Inputs**

- `nums`: an array of $N$ integers, where $2 \le N \le 1000$ and $0 \le \texttt{nums[i]} \le 500$.

**Return value**

- The maximum number of elements in an arithmetic subsequence of `nums`.

### Examples

**Example 1**

- Input: `nums = [3,6,9,12]`
- Output: `4`
- Explanation: The entire array is arithmetic with common difference $3$.

**Example 2**

- Input: `nums = [9,4,7,2,10]`
- Output: `3`
- Explanation: The subsequence `[4,7,10]` has common difference $3$.

**Example 3**

- Input: `nums = [20,1,15,3,10,5,8]`
- Output: `4`
- Explanation: The subsequence `[20,15,10,5]` has common difference $-5$.
