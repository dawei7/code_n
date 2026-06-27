# Sliding Subarray Beauty

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2653 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Sliding Window |
| Official Link | [sliding-subarray-beauty](https://leetcode.com/problems/sliding-subarray-beauty/) |

## Problem Description & Examples
### Goal
Given an integer array, identify the "beauty" value of every contiguous subarray of length `k`. The beauty of a subarray is defined as the `x`-th smallest number in that subarray, provided that this number is negative; otherwise, the beauty is 0.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `k`: An integer representing the size of the sliding window.
- `x`: An integer representing the rank of the smallest number to retrieve.

**Return value**

- A list of integers representing the beauty value for each sliding window of size `k`.

### Examples
**Example 1**

- Input: `nums = [1,-2,-3,-4,5], k = 2, x = 2`
- Output: `[-3,-3,-4]`

**Example 2**

- Input: `nums = [-1,-2,-3,-4,5], k = 2, x = 2`
- Output: `[-2,-3,-4]`

**Example 3**

- Input: `nums = [-3,1,2,-3,0,-3], k = 2, x = 1`
- Output: `[-3,0,-3,-3,-3]`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Sliding Window** combined with a **Frequency Array** (or Fenwick Tree/Binary Indexed Tree). Since the range of values in `nums` is constrained between -50 and 50, we can maintain a frequency map of the current window's elements. For each window, we iterate through the frequency map to find the `x`-th smallest negative number, which takes constant time O(50).

---

## Complexity Analysis
- **Time Complexity**: O(n * 50), where `n` is the length of the input array. Since the range of values is fixed (101 possible values), the inner loop over the frequency map is effectively O(1).
- **Space Complexity**: O(1), as the frequency map size is fixed at 101 regardless of the input size `n`.
