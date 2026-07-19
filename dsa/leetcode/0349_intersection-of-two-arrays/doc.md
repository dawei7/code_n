# Intersection of Two Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 349 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Two Pointers, Binary Search, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/intersection-of-two-arrays/) |

## Problem Description
### Goal
Given two integer arrays, identify the values that occur at least once in both arrays. Original positions and occurrence counts beyond the first presence do not affect membership in this intersection.

Each element in the result must be unique, and the result may be returned in any order. Duplicate occurrences in either input must not create duplicate output entries, while negative values and zero follow ordinary integer equality. If the arrays share no value, return an empty list. The function returns set-style shared values rather than index pairs or the multiset intersection.

### Function Contract
**Inputs**

- `nums1`: the first integer array
- `nums2`: the second integer array

**Return value**

- A list containing the unique intersection of the two arrays in any order.

### Examples
**Example 1**

- Input: `nums1 = [1, 2, 2, 1], nums2 = [2, 2]`
- Output: `[2]`

**Example 2**

- Input: `nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]`
- Output: `[4, 9]`

**Example 3**

- Input: `nums1 = [1, 2, 3], nums2 = [4, 5, 6]`
- Output: `[]`
