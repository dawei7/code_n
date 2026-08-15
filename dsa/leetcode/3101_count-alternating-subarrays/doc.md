# Count Alternating Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3101 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [count-alternating-subarrays](https://leetcode.com/problems/count-alternating-subarrays/) |

## Problem Description

### Goal

You are given a binary array `nums`. A subarray is *alternating* when every pair of adjacent elements inside it has different values; equivalently, no two neighboring elements in that contiguous range are equal.

Count and return all alternating subarrays of `nums`. Every one-element subarray is alternating because it contains no adjacent pair to violate the condition.

Subarrays with the same values at different positions are counted separately because each choice of contiguous boundaries is a distinct subarray.

### Function Contract

**Inputs**

- `nums`: A binary array of length $n$, where $1 \le n \le 10^5$ and every value is either `0` or `1`.

**Return value**

- The number of contiguous subarrays whose adjacent values alternate.

### Examples

#### Example 1

- **Input:** `nums = [0, 1, 1, 1]`
- **Output:** `5`
- **Explanation:** The four one-element subarrays and the range `[0, 1]` are alternating.

#### Example 2

- **Input:** `nums = [1, 0, 1, 0]`
- **Output:** `10`
- **Explanation:** Every subarray is alternating, so all $4 \cdot 5 / 2 = 10$ contiguous ranges are counted.
