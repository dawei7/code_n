# Maximize Active Section with Trade II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3501 |
| Difficulty | Hard |
| Topics | Array, String, Binary Search, Segment Tree |
| Official Link | [maximize-active-section-with-trade-ii](https://leetcode.com/problems/maximize-active-section-with-trade-ii/) |

## Problem Description & Examples
### Goal
Given an array of integers representing activity levels and a maximum allowed trade-off value, determine the length of the longest contiguous subarray where the difference between the maximum and minimum elements does not exceed the specified trade-off limit.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the activity levels.
- `k`: An integer representing the maximum allowed difference between the maximum and minimum values in the subarray.

**Return value**

- An integer representing the length of the longest valid contiguous subarray.

### Examples
**Example 1**

- Input: `nums = [8, 2, 4, 7], k = 4`
- Output: `2`
- Explanation: The subarray `[8, 4]` is invalid (diff 4), but `[2, 4]` or `[4, 7]` are valid. The longest valid subarray is `[2, 4]` or `[4, 7]` or `[8]` etc. Actually, `[2, 4]` has length 2.

**Example 2**

- Input: `nums = [10, 1, 2, 4, 7, 2], k = 5`
- Output: `4`
- Explanation: The subarray `[1, 2, 4, 2]` has max 4 and min 1, diff 3 <= 5. Length is 4.

**Example 3**

- Input: `nums = [4, 2, 2, 2, 4, 4, 2, 2], k = 0`
- Output: `3`
- Explanation: The subarray `[2, 2, 2]` has max 2 and min 2, diff 0 <= 0. Length is 3.

---

## Underlying Base Algorithm(s)
The problem is solved using the **Sliding Window** technique combined with a **Monotonic Deque** (or two deques) to maintain the minimum and maximum values of the current window in $O(1)$ amortized time. Alternatively, a Segment Tree could be used, but the sliding window approach is optimal for contiguous subarrays.

---

## Complexity Analysis
- **Time Complexity**: $O(n)$, where $n$ is the length of the input array, as each element is added and removed from the deques at most once.
- **Space Complexity**: $O(n)$ in the worst case to store the deques.
