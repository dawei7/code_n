# Find Maximum Non-decreasing Array Length

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2945 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Dynamic Programming, Stack, Queue, Monotonic Stack, Prefix Sum, Monotonic Queue |
| Official Link | [find-maximum-non-decreasing-array-length](https://leetcode.com/problems/find-maximum-non-decreasing-array-length/) |

## Problem Description & Examples
### Goal
Given an array of integers, you can perform an operation where you merge adjacent elements into a single element equal to their sum. The objective is to find the maximum number of elements in the resulting array such that the elements are in non-decreasing order.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the initial array.

**Return value**

- An integer representing the maximum length of a non-decreasing array achievable through the specified merge operations.

### Examples
**Example 1**

- Input: `nums = [5, 2, 2]`
- Output: `1`
- Explanation: Merging all elements results in `[9]`, which is non-decreasing.

**Example 2**

- Input: `nums = [1, 2, 3, 4]`
- Output: `4`
- Explanation: The array is already non-decreasing.

**Example 3**

- Input: `nums = [4, 3, 2, 6]`
- Output: `3`
- Explanation: Merge 4 and 3 to get `[7, 2, 6]` (not non-decreasing). Merge 3 and 2 to get `[4, 5, 6]`, which is non-decreasing.

---

## Underlying Base Algorithm(s)
The problem is solved using Dynamic Programming optimized with a Monotonic Queue (or a monotonic stack/binary search approach). We define `dp[i]` as the maximum number of elements in a non-decreasing array formed by the prefix `nums[0...i-1]`, and `last[i]` as the minimum possible value of the last element in such an array. By maintaining the prefix sums, we can efficiently determine if a merge is valid and use a monotonic queue to keep track of optimal transitions, reducing the complexity from $O(n^2)$ to $O(n)$.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as each element is processed a constant number of times using the monotonic queue.
- **Space Complexity**: `O(n)` to store the DP arrays and the queue.
