# Find the Integer Added to Array I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3131 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [find-the-integer-added-to-array-i](https://leetcode.com/problems/find-the-integer-added-to-array-i/) |

## Problem Description & Examples
### Goal
Given two arrays of equal length, where the second array is formed by adding a constant integer `x` to every element of the first array, determine the value of `x`.

### Function Contract
**Inputs**

- `nums1`: A list of integers.
- `nums2`: A list of integers, which is a permutation of `nums1` with each element incremented by `x`.

**Return value**

- An integer representing the constant value `x` added to each element of `nums1`.

### Examples
**Example 1**

- Input: `nums1 = [2, 6, 4], nums2 = [9, 7, 5]`
- Output: `3`

**Example 2**

- Input: `nums1 = [10], nums2 = [5]`
- Output: `-5`

**Example 3**

- Input: `nums1 = [1, 1, 1, 1], nums2 = [1, 1, 1, 1]`
- Output: `0`

---

## Underlying Base Algorithm(s)
The problem relies on the property of linear shifts: if every element in a set is increased by a constant `x`, the difference between the minimum (or maximum) values of the two sets will also be exactly `x`. Thus, `x = min(nums2) - min(nums1)`.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the arrays, as we need to traverse the arrays to find the minimum values.
- **Space Complexity**: `O(1)`, as we only store the minimum values regardless of input size.
