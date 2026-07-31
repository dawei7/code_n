# Number of Zero-Filled Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2348 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-zero-filled-subarrays/) |

## Problem Description

### Goal

Given an integer array `nums`, count its nonempty contiguous subarrays whose
every element is `0`. Subarrays are distinguished by their start and end
positions, so equal sequences occurring at different positions count
separately.

Return the total across all lengths and all zero runs. Nonzero values separate
the array into independent runs: a zero-filled subarray cannot cross one of
them anywhere.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $1 \le n \le 10^5$ and each
  value lies in $[-10^9,10^9]$.

**Return value**

The number of nonempty contiguous subarrays containing only zeros.

### Examples

**Example 1**

- Input: `nums = [1,3,0,0,2,0,0,4]`
- Output: `6`
- Explanation: Four one-zero subarrays and two two-zero subarrays occur.

**Example 2**

- Input: `nums = [0,0,0,2,0,0]`
- Output: `9`
- Explanation: Runs of lengths 3 and 2 contribute 6 and 3.

**Example 3**

- Input: `nums = [2,10,2019]`
- Output: `0`
- Explanation: The array contains no zero.
