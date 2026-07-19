# Maximum Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 53 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Divide and Conquer, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-subarray/) |

## Problem Description
### Goal
You are given a nonempty integer array `nums`. Choose one contiguous interval and add all values inside it, then find the greatest sum obtainable over every possible nonempty interval.

Return that maximum sum, not the interval itself. The chosen values must occupy consecutive positions, so favorable elements cannot skip an intervening loss. An empty subarray with sum zero is not permitted; consequently, when every value is negative, the answer is the largest single element rather than zero.

### Function Contract
**Inputs**

- `nums`: a nonempty `List[int]`

**Return value**

The maximum contiguous-subarray sum as an integer.

### Examples
**Example 1**

- Input: `nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`
- Output: `6`

**Example 2**

- Input: `nums = [1]`
- Output: `1`

**Example 3**

- Input: `nums = [-8, -3, -5]`
- Output: `-3`
