# Count Subarrays Where Max Element Appears at Least K Times

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2962 |
| Difficulty | Medium |
| Topics | Array, Sliding Window |
| Official Link | [count-subarrays-where-max-element-appears-at-least-k-times](https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/) |

## Problem Description & Examples
### Goal
Given an array of integers, determine the total number of contiguous subarrays that contain the maximum value of the entire array at least `k` times.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `k`: An integer representing the minimum frequency threshold for the maximum element.

**Return value**

- An integer representing the count of valid subarrays.

### Examples
**Example 1**

- Input: `nums = [1,3,2,3,3], k = 2`
- Output: `6`

**Example 2**

- Input: `nums = [1,4,2,1], k = 3`
- Output: `0`

**Example 3**

- Input: `nums = [6,6,6], k = 1`
- Output: `6`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Sliding Window** (or Two-Pointer) approach. First, identify the maximum element in the array. Then, maintain a window `[left, right]` and expand the `right` pointer. Whenever the count of the maximum element within the window reaches `k`, all subarrays starting from the current `left` and ending at `right` or any index beyond `right` (up to the end of the array) are valid. This allows for an efficient calculation without nested loops.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array. We traverse the array twice: once to find the maximum and once to process the sliding window.
- **Space Complexity**: `O(1)`, as we only use a few integer variables to track counts and pointers.
