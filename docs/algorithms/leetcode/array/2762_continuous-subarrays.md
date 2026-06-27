# Continuous Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2762 |
| Difficulty | Medium |
| Topics | Array, Queue, Sliding Window, Heap (Priority Queue), Ordered Set, Monotonic Queue |
| Official Link | [continuous-subarrays](https://leetcode.com/problems/continuous-subarrays/) |

## Problem Description & Examples
### Goal
Given an integer array, identify the total count of contiguous subarrays where the absolute difference between any two elements within that subarray is at most 2.

### Function Contract
**Inputs**

- `nums`: A list of integers where 1 <= nums.length <= 10^5 and 1 <= nums[i] <= 10^9.

**Return value**

- An integer representing the total number of valid continuous subarrays.

### Examples
**Example 1**

- Input: `nums = [5, 4, 2, 4]`
- Output: `8`

**Example 2**

- Input: `nums = [1, 2, 3]`
- Output: `6`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Sliding Window** approach combined with two **Monotonic Deques**. The deques maintain the indices of the maximum and minimum elements within the current window `[left, right]`. As we expand the window by moving `right`, we check if the condition `max_val - min_val <= 2` is violated. If it is, we increment `left` until the condition is restored. The number of valid subarrays ending at `right` is simply `right - left + 1`.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array. Each element is added and removed from the deques at most once.
- **Space Complexity**: `O(n)` in the worst case to store the indices in the deques, though practically `O(1)` since the window size is constrained by the value difference condition.
