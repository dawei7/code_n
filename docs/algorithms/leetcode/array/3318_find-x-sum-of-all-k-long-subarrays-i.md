# Find X-Sum of All K-Long Subarrays I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3318 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Sliding Window, Heap (Priority Queue) |
| Official Link | [find-x-sum-of-all-k-long-subarrays-i](https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/) |

## Problem Description & Examples
### Goal
Given an array of integers, calculate the "X-sum" for every contiguous subarray of length `k`. The X-sum is defined as the sum of the `x` most frequent elements in the subarray. If two elements have the same frequency, the larger element is prioritized. If there are fewer than `x` distinct elements in the subarray, the X-sum is simply the sum of all elements in the subarray.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `k`: An integer representing the length of the sliding window.
- `x`: An integer representing the number of top-frequency elements to sum.

**Return value**

- A list of integers representing the X-sum for each sliding window of size `k`.

### Examples
**Example 1**

- Input: `nums = [1, 1, 2, 2, 3, 4, 2, 3], k = 6, x = 2`
- Output: `[6, 10, 12]`

**Example 2**

- Input: `nums = [3, 8, 7, 8, 7, 5], k = 2, x = 2`
- Output: `[11, 15, 15, 15, 12]`

**Example 3**

- Input: `nums = [1, 1, 1, 1], k = 2, x = 1`
- Output: `[2, 2, 2]`

---

## Underlying Base Algorithm(s)
The problem utilizes a **Sliding Window** approach combined with a **Frequency Map** (Hash Table). For each window, we extract the frequencies of elements, sort them based on the criteria (frequency first, then value), and compute the sum of the top `x` elements.

---

## Complexity Analysis
- **Time Complexity**: `O(n * k log k)`, where `n` is the length of `nums`. For each of the `n - k + 1` windows, we perform frequency counting and sorting of at most `k` distinct elements.
- **Space Complexity**: `O(n)`, required to store the frequency map and the resulting list of X-sums.
