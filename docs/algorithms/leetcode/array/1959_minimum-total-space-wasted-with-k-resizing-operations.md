# Minimum Total Space Wasted With K Resizing Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1959 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Prefix Sum |
| Official Link | [minimum-total-space-wasted-with-k-resizing-operations](https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/) |

## Problem Description & Examples
### Goal
Store the sequence in an array whose capacity may be resized at most `k` times. Each segment between resizes uses one fixed capacity, and waste is unused capacity over time. Minimize total waste.

### Function Contract
**Inputs**

- `nums`: required array sizes over time.
- `k`: maximum number of resize operations.

**Return value**

Return the minimum possible wasted space.

### Examples
**Example 1**

- Input: `nums = [10,20], k = 0`
- Output: `10`

**Example 2**

- Input: `nums = [10,20,30], k = 1`
- Output: `10`

**Example 3**

- Input: `nums = [10,20,15,30,20], k = 2`
- Output: `15`

---

## Underlying Base Algorithm(s)
A fixed-capacity segment from `i` to `j` wastes `max(nums[i:j+1]) * length - sum(nums[i:j+1])`. Precompute segment costs, then run DP over positions and number of segments, where at most `k` resizes means at most `k + 1` segments.

---

## Complexity Analysis
- **Time Complexity**: `O(k * n^2)`
- **Space Complexity**: `O(n^2 + k * n)`
