# Longest Even Odd Subarray With Threshold

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2760 |
| Difficulty | Easy |
| Topics | Array, Sliding Window |
| Official Link | [longest-even-odd-subarray-with-threshold](https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/) |

## Problem Description & Examples
### Goal
Given an integer array and a threshold value, identify the length of the longest contiguous subarray that satisfies three conditions: every element is at most the threshold, the first element is even, and adjacent elements alternate between even and odd parity.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `threshold`: An integer representing the upper bound for elements in the subarray.

**Return value**

- An integer representing the length of the longest valid subarray found. If no such subarray exists, return 0.

### Examples
**Example 1**

- Input: `nums = [3, 2, 5, 4], threshold = 5`
- Output: `3`

**Example 2**

- Input: `nums = [1, 2], threshold = 2`
- Output: `1`

**Example 3**

- Input: `nums = [2, 3, 4, 5], threshold = 4`
- Output: `3`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Linear Scan (Single Pass)** approach. We iterate through the array while maintaining a running count of the current valid subarray length. We reset the counter whenever an element violates the threshold or the parity alternation rule, ensuring we only start counting when an even number is encountered.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we traverse the list exactly once.
- **Space Complexity**: `O(1)`, as we only use a few integer variables to track the current and maximum lengths.
