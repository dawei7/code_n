# Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1438 |
| Difficulty | Medium |
| Topics | Array, Queue, Sliding Window, Heap (Priority Queue), Ordered Set, Monotonic Queue |
| Official Link | [longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) |

## Problem Description & Examples
### Goal
Find the longest contiguous subarray where the difference between the largest and smallest values is at most `limit`.

### Function Contract
**Inputs**

- `nums`: a list of integers.
- `limit`: the maximum allowed absolute difference inside the window.

**Return value**

The maximum length of a valid contiguous subarray.

### Examples
**Example 1**

- Input: `nums = [8,2,4,7], limit = 4`
- Output: `2`

**Example 2**

- Input: `nums = [10,1,2,4,7,2], limit = 5`
- Output: `4`

**Example 3**

- Input: `nums = [4,2,2,2,4,4,2,2], limit = 0`
- Output: `3`

---

## Underlying Base Algorithm(s)
Sliding window with two monotonic deques. One deque keeps candidate maximums and the other keeps candidate minimums; shrink the left side until their difference is within the limit.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` for the deques in the worst case.
