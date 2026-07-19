# Max Consecutive Ones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 485 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [LeetCode](https://leetcode.com/problems/max-consecutive-ones/) |

## Problem Description
### Goal
Given a nonempty binary array `nums`, examine its maximal contiguous runs of `1` values. A run ends whenever a `0` occurs or the array boundary is reached, and separated runs cannot be joined by skipping the zeroes between them.

Return the maximum number of consecutive `1` values in any run. An array containing only zeroes returns `0`, while an all-one array returns its complete length. The result is a length rather than the run's starting index or values, and each position is considered in its original order.

### Function Contract
**Inputs**

- `nums`: a nonempty array whose elements are either `0` or `1`

**Return value**

- The number of elements in the longest consecutive block of ones

### Examples
**Example 1**

- Input: `nums = [1, 1, 0, 1, 1, 1]`
- Output: `3`

**Example 2**

- Input: `nums = [1, 0, 1, 1, 0, 1]`
- Output: `2`

**Example 3**

- Input: `nums = [0, 0, 0]`
- Output: `0`
