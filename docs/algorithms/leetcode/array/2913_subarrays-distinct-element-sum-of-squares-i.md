# Subarrays Distinct Element Sum of Squares I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2913 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Segment Tree |
| Official Link | [subarrays-distinct-element-sum-of-squares-i](https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/) |

## Problem Description & Examples
### Goal
Given an array of integers, calculate the sum of the squares of the count of distinct elements for every possible contiguous subarray. The final result should be the summation of these squared counts.

### Function Contract
**Inputs**

- `nums`: A list of integers where 1 <= nums.length <= 100 and 1 <= nums[i] <= 100.

**Return value**

- An integer representing the sum of the squares of the number of distinct elements across all contiguous subarrays.

### Examples
**Example 1**

- Input: `nums = [1, 2, 1]`
- Output: `15`
- Explanation: Subarrays are [1], [2], [1], [1, 2], [2, 1], [1, 2, 1]. Distinct counts are 1, 1, 1, 2, 2, 2. Squares are 1, 1, 1, 4, 4, 4. Sum = 15.

**Example 2**

- Input: `nums = [2, 2]`
- Output: `3`
- Explanation: Subarrays are [2], [2], [2, 2]. Distinct counts are 1, 1, 1. Squares are 1, 1, 1. Sum = 3.

**Example 3**

- Input: `nums = [1, 1, 2, 2]`
- Output: `20`

---

## Underlying Base Algorithm(s)
The problem is solved using a brute-force approach with nested loops to iterate through all possible subarrays. For each subarray, a hash set is utilized to track unique elements, allowing for an efficient count of distinct values.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`, where `n` is the length of the input array. We iterate through all `n(n+1)/2` subarrays, and for each, we perform set operations that take linear time relative to the subarray length.
- **Space Complexity**: `O(n)`, as the hash set stores at most `n` distinct elements at any given time.
