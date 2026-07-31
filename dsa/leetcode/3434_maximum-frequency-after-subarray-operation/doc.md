# Maximum Frequency After Subarray Operation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3434 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Dynamic Programming, Greedy, Enumeration, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-frequency-after-subarray-operation/) |

## Problem Description

### Goal

Given an integer array `nums` and a target value `k`, perform exactly one operation. Choose a non-empty contiguous subarray `nums[i..j]`, choose any integer `x`, and add that same `x` to every element of the selected subarray.

Elements outside the selected interval remain unchanged. The addition may be positive, negative, or zero. Determine the greatest possible number of elements equal to `k` after the operation.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $1\le n\le10^5$ and $1\le\texttt{nums[i]}\le50$.
- `k`: The target integer, where $1\le k\le50$.

**Return value**

Return the maximum attainable frequency of `k` after one subarray addition.

### Examples

**Example 1**

- Input: `nums = [1,2,3,4,5,6], k = 1`
- Output: `2`

**Example 2**

- Input: `nums = [10,2,3,4,5,5,4,3,2,2], k = 10`
- Output: `4`
