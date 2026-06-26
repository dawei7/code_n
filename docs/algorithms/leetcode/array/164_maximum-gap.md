# Maximum Gap

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 164 |
| Difficulty | Medium |
| Topics | Array, Sorting, Bucket Sort, Radix Sort |
| Official Link | [maximum-gap](https://leetcode.com/problems/maximum-gap/) |

## Problem Description & Examples
### Goal
Given an unsorted array, find the largest difference between consecutive values
after sorting the array.

### Function Contract
**Inputs**

- `nums`: an integer array.

**Return value**

The maximum adjacent sorted gap, or `0` when fewer than two values exist.

### Examples
**Example 1**

- Input: `nums = [3, 6, 9, 1]`
- Output: `3`

**Example 2**

- Input: `nums = [10]`
- Output: `0`

**Example 3**

- Input: `nums = [1, 100, 50]`
- Output: `50`

---

## Underlying Base Algorithm(s)
The direct approach sorts and scans adjacent differences. The linear-time
canonical method uses buckets: with `n` values between min and max, the maximum
gap must occur between buckets, so store only each bucket's minimum and maximum
and scan non-empty buckets in order.

---

## Complexity Analysis
- **Time Complexity**: `O(n)` with bucket placement, or `O(n log n)` by sorting.
- **Space Complexity**: `O(n)` for buckets.
