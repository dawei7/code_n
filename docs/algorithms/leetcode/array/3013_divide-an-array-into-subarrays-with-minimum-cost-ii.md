# Divide an Array Into Subarrays With Minimum Cost II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3013 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Sliding Window, Heap (Priority Queue) |
| Official Link | [divide-an-array-into-subarrays-with-minimum-cost-ii](https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/) |

## Problem Description & Examples
### Goal
Given an array of integers, partition it into exactly `k` contiguous subarrays such that the sum of the first elements of each subarray is minimized. The first element of the first subarray is always the first element of the array.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `k`: An integer representing the number of subarrays required.
- `dist`: An integer representing the maximum distance between the starting indices of any two adjacent subarrays.

**Return value**

- An integer representing the minimum possible sum of the first elements of the `k` subarrays.

### Examples
**Example 1**

- Input: `nums = [1, 3, 2, 6, 4, 2]`, `k = 3`, `dist = 3`
- Output: `5`
- Explanation: We can partition the array into `[1]`, `[3, 2, 6]`, and `[4, 2]`. The first elements are 1, 3, and 4. Sum = 8. Alternatively, `[1]`, `[3, 2]`, `[6, 4, 2]` gives 1+3+6=10. The optimal is `[1]`, `[3]`, `[2]` is not possible due to `dist`. The optimal is 1+3+1=5 (if indices allow).

**Example 2**

- Input: `nums = [10, 8, 3, 7, 15]`, `k = 3`, `dist = 1`
- Output: `21`

**Example 3**

- Input: `nums = [10, 8, 3, 7, 15]`, `k = 3`, `dist = 2`
- Output: `18`

---

## Underlying Base Algorithm(s)
The problem is solved using a sliding window combined with a dynamic data structure to maintain the smallest `k-1` elements in a range of size `dist`. We use two balanced BSTs (or a SortedList) to track the smallest `k-1` elements and the remaining elements, allowing for efficient insertion, deletion, and sum retrieval.

---

## Complexity Analysis
- **Time Complexity**: `O(n log(dist))`, where `n` is the length of the array. Each element is added and removed from the sorted structures at most once.
- **Space Complexity**: `O(n)`, required to store the elements in the sliding window and the sorted structures.
