# Longest Alternating Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2765 |
| Difficulty | Easy |
| Topics | Array, Enumeration |
| Official Link | [longest-alternating-subarray](https://leetcode.com/problems/longest-alternating-subarray/) |

## Problem Description & Examples
### Goal
Given an array of integers, identify the length of the longest contiguous subarray where the difference between consecutive elements alternates between 1 and -1. Specifically, for a subarray `nums[i...j]` to be valid, `nums[k+1] - nums[k]` must be `1` if `k-i` is even, and `-1` if `k-i` is odd. If no such subarray of length at least 2 exists, return -1.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the length of the longest alternating subarray, or -1 if no valid subarray of length 2 or greater is found.

### Examples
**Example 1**

- Input: `nums = [3, 4, 5, 4]`
- Output: `2` (The longest is `[4, 5]` or `[5, 4]`)

**Example 2**

- Input: `nums = [2, 2, 2]`
- Output: `-1`

**Example 3**

- Input: `nums = [1, 2, 1, 2]`
- Output: `4`

---

## Underlying Base Algorithm(s)
The problem is solved using a linear scan (sliding window/two-pointer approach). We maintain a current length counter that resets or increments based on the expected alternating difference. By iterating through the array once, we track the state of the expected difference (1 or -1) and update the global maximum length whenever a valid sequence is extended.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we perform a single pass through the data.
- **Space Complexity**: `O(1)`, as we only use a few integer variables to track the current state and the maximum length found.
