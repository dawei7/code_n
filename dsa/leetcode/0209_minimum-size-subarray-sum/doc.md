# Minimum Size Subarray Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 209 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-size-subarray-sum/) |

## Problem Description
### Goal
Given a positive integer `target` and a list of positive integers `nums`, choose a nonempty contiguous subarray whose values sum to at least `target`. The interval must use consecutive positions and cannot skip elements or wrap around the array.

Return the minimum length among all qualifying intervals. A one-element interval is valid when its value already reaches the target, and positive values ensure extending an interval never decreases its sum. If even the full array cannot reach `target`, return `0` rather than an interval length. The function returns only the length, not the selected elements or their indices.

### Function Contract
**Inputs**

- `target`: a positive required sum
- `nums`: a list of positive integers

**Return value**

The minimum qualifying length, or zero when no subarray qualifies.

### Examples
**Example 1**

- Input: `target = 7, nums = [2,3,1,2,4,3]`
- Output: `2`

**Example 2**

- Input: `target = 4, nums = [1,4,4]`
- Output: `1`

**Example 3**

- Input: `target = 20, nums = [1,2,3]`
- Output: `0`
