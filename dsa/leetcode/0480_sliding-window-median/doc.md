# Sliding Window Median

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 480 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Sliding Window, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/sliding-window-median/) |

## Problem Description
### Goal
Given an integer array and a valid window length `k`, examine each contiguous block of exactly `k` values as the window moves one position right from the start to the end. Duplicate values remain separate window occurrences.

Return one floating-point median per window in left-to-right order. For odd `k`, the median is the middle value after ordering the window; for even `k`, it is the arithmetic mean of the two middle values. Remove the departing occurrence and add the arriving occurrence for each shift. The result has `len(nums) - k + 1` entries and must be computed without sorting every window from scratch.

### Function Contract
**Inputs**

- `nums`: the input integers
- `k`: the window length

**Return value**

- One floating-point median for each of the `len(nums) - k + 1` windows

### Examples
**Example 1**

- Input: `nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3`
- Output: `[1, -1, -1, 3, 5, 6]`

**Example 2**

- Input: `nums = [1, 2, 3, 4], k = 2`
- Output: `[1.5, 2.5, 3.5]`

**Example 3**

- Input: `nums = [5], k = 1`
- Output: `[5]`
