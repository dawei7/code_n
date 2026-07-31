# Count the Number of Beautiful Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2588 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Bit Manipulation, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/) |

## Problem Description

### Goal

You are given a 0-indexed array `nums` of non-negative integers. In one operation, choose two different indices `i` and `j`, then choose a non-negative bit position $k$ whose bit is set in both selected values. Subtract $2^k$ from both `nums[i]` and `nums[j]`.

A nonempty contiguous subarray is beautiful when some sequence of these operations can reduce every one of its elements to zero. The sequence may be empty, so a subarray already consisting entirely of zeros is beautiful.

Return the total number of beautiful subarrays. Each occurrence is identified by its pair of array boundaries, even when two subarrays contain equal values.

### Function Contract

**Inputs**

- `nums`: A list of $n$ non-negative integers, where $1 \leq n \leq 10^5$ and $0 \leq \texttt{nums[i]} \leq 10^6$.

**Return value**

- The number of nonempty contiguous subarrays that can be reduced completely to zero by the allowed operation.

### Examples

**Example 1**

- Input: `nums = [4,3,1,2,4]`
- Output: `2`

The subarray `[3,1,2]` and the complete array are beautiful.

**Example 2**

- Input: `nums = [1,10,4]`
- Output: `0`

No nonempty subarray satisfies the required bit-pairing condition.
