# Longest Well-Performing Interval

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1124 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Stack, Monotonic Stack, Prefix Sum |
| Official Link | [longest-well-performing-interval](https://leetcode.com/problems/longest-well-performing-interval/) |

## Problem Description & Examples
### Goal
Given daily work hours, find the longest contiguous interval where the number of tiring days is greater than the number of non-tiring days. A tiring day has more than `8` hours.

### Function Contract
**Inputs**

- `hours`: list of daily hour counts.

**Return value**

The maximum length of a well-performing interval.

### Examples
**Example 1**

- Input: `hours = [9,9,6,0,6,6,9]`
- Output: `3`

**Example 2**

- Input: `hours = [6,6,6]`
- Output: `0`

**Example 3**

- Input: `hours = [9,6,9,6,9]`
- Output: `5`

---

## Underlying Base Algorithm(s)
Prefix sum with earliest-index lookup.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`
