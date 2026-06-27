# Find X-Sum of All K-Long Subarrays II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3321 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Sliding Window, Heap (Priority Queue) |
| Official Link | [find-x-sum-of-all-k-long-subarrays-ii](https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/) |

## Problem Description & Examples
### Goal
Given an array of integers, calculate the "X-Sum" for every contiguous subarray of length `k`. The X-Sum is defined as the sum of the `x` most frequent elements in the subarray. If two elements have the same frequency, the larger element is prioritized. If there are fewer than `x` distinct elements in the subarray, the X-Sum is simply the sum of all elements in the subarray.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `k`: An integer representing the length of the sliding window.
- `x`: An integer representing the number of top frequent elements to sum.

**Return value**

- A list of integers representing the X-Sum for each sliding window of size `k`.

### Examples
**Example 1**

- Input: `nums = [1,1,2,2,3,4,2,3], k = 6, x = 2`
- Output: `[6, 10, 12]`

**Example 2**

- Input: `nums = [3,8,7,8,7,5], k = 2, x = 2`
- Output: `[11, 15, 15, 15, 12]`

**Example 3**

- Input: `nums = [1,1,1,1], k = 2, x = 1`
- Output: `[2, 2, 2]`

---

## Underlying Base Algorithm(s)
The problem is solved using a sliding window approach combined with two balanced binary search trees (or two sorted sets) to maintain the top `x` frequent elements. We track the frequency of each number using a hash map. The two sets partition the elements into "top `x`" and "others," allowing us to efficiently update the X-Sum as the window slides by moving elements between sets and maintaining the sum of the top `x` group.

---

## Complexity Analysis
- **Time Complexity**: `O(n log k)`, where `n` is the length of `nums`. Each insertion and deletion in the sorted sets takes `O(log k)` time.
- **Space Complexity**: `O(n)`, required to store the frequency map and the elements within the sliding window sets.
