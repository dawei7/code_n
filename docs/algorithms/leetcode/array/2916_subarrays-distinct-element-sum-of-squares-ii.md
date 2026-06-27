# Subarrays Distinct Element Sum of Squares II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2916 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Binary Indexed Tree, Segment Tree |
| Official Link | [subarrays-distinct-element-sum-of-squares-ii](https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/) |

## Problem Description & Examples
### Goal
Calculate the sum of the squares of the count of distinct elements for every possible contiguous subarray of a given integer array. Since the result can be very large, return it modulo 10^9 + 7.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input array.

**Return value**

- An integer representing the sum of the squares of the number of distinct elements in all subarrays, modulo 10^9 + 7.

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

- Input: `nums = [1, 2, 3]`
- Output: `14`

---

## Underlying Base Algorithm(s)
The problem is solved using a Segment Tree with Lazy Propagation. We iterate through the array, maintaining the contribution of each subarray ending at the current index `i`. If an element `x` was last seen at index `prev`, adding `x` at index `i` increases the distinct count by 1 for all subarrays starting in the range `(prev, i]`. Using the identity $(x+1)^2 = x^2 + 2x + 1$, we can update the sum of squares efficiently by maintaining the sum of distinct counts and the sum of squares of distinct counts in a segment tree.

## Complexity Analysis
- **Time Complexity**: `O(n log n)`, where `n` is the length of the array, due to the segment tree operations performed for each element.
- **Space Complexity**: `O(n)`, required for the segment tree and the hash map storing the last seen indices.
