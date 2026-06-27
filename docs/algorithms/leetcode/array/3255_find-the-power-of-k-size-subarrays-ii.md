# Find the Power of K-Size Subarrays II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3255 |
| Difficulty | Medium |
| Topics | Array, Sliding Window |
| Official Link | [find-the-power-of-k-size-subarrays-ii](https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/) |

## Problem Description & Examples
### Goal
Given an array of integers and an integer `k`, identify the "power" of every contiguous subarray of length `k`. A subarray is considered powerful if it is sorted in strictly increasing order with consecutive elements having a difference of exactly 1. If a subarray is powerful, its power is the maximum element in that subarray; otherwise, its power is -1.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input sequence.
- `k`: An integer representing the size of the sliding window.

**Return value**

- A list of integers where the $i$-th element is the power of the subarray starting at index $i$.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4, 3, 2, 5], k = 3`
- Output: `[3, 4, -1, -1, -1]`

**Example 2**

- Input: `nums = [2, 2, 2, 2, 2], k = 4`
- Output: `[-1, -1]`

**Example 3**

- Input: `nums = [3, 2, 3, 2, 3, 2], k = 2`
- Output: `[-1, 3, -1, 3, -1]`

---

## Underlying Base Algorithm(s)
The problem is solved using a linear scan with a sliding window approach. We maintain a count of consecutive elements that satisfy the condition `nums[i] == nums[i-1] + 1`. By tracking the length of the current "valid" sequence, we can determine if a window of size `k` is powerful in $O(1)$ time per element.

---

## Complexity Analysis
- **Time Complexity**: $O(n)$, where $n$ is the length of the input array, as we traverse the array exactly once.
- **Space Complexity**: $O(n - k + 1)$ to store the result array, or $O(1)$ auxiliary space if the result is not counted towards space complexity.
