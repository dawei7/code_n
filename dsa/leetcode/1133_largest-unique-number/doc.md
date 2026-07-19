# Largest Unique Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1133 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/largest-unique-number/) |

## Problem Description

### Goal

You are given an integer array `nums`. An integer is unique in this array when it occurs exactly once; an integer that appears two or more times is not unique, regardless of where its copies occur.

Return the largest integer among all unique values in `nums`. The largest value in the array is not necessarily the answer if it is repeated. If no integer occurs exactly once, return `-1`.

### Function Contract

**Inputs**

- `nums`: an integer array of length $n$, where $1 \le n \le 2000$ and every value lies in $[0,1000]$.

Let $V=1001$ be the size of the allowed value domain.

**Return value**

The greatest value whose frequency in `nums` is exactly one, or `-1` if no such value exists.

### Examples

**Example 1**

- Input: `nums = [5,7,3,9,4,9,8,3,1]`
- Output: `8`
- Explanation: `9` is repeated, while `8` is the largest value appearing once.

**Example 2**

- Input: `nums = [9,9,8,8]`
- Output: `-1`
