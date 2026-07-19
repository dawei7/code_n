# Number of Subarrays with Bounded Maximum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 795 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/) |

## Problem Description

### Goal

Given an integer array `nums` and bounds `left` and `right`, consider every nonempty contiguous subarray and find its maximum element.

Return the number of subarrays whose maximum lies in the inclusive interval `[left, right]`. A candidate must contain at least one value greater than or equal to `left` and no value greater than `right`. Subarrays are counted by index range, so equal value sequences at different positions contribute separately.

### Function Contract

**Inputs**

- `nums`: a nonempty list of positive integers.
- `left`: the lower allowed maximum.
- `right`: the upper allowed maximum, with `left <= right`.

**Return value**

- The number of contiguous subarrays having `left <= maximum <= right`.

### Examples

**Example 1**

- Input: `nums = [2,1,4,3], left = 2, right = 3`
- Output: `3`
- Explanation: `[2]`, `[2,1]`, and `[3]` have valid maxima.

**Example 2**

- Input: `nums = [2,9,2,5,6], left = 2, right = 8`
- Output: `7`
- Explanation: The `9` splits the array; seven subarrays in the remaining segments contain a value in the allowed interval.

**Example 3**

- Input: `nums = [1,2,3], left = 1, right = 3`
- Output: `6`
- Explanation: Every nonempty subarray is valid.
