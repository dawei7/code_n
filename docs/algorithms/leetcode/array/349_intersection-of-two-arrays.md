# Intersection of Two Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 349 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Two Pointers, Binary Search, Sorting |
| Official Link | [intersection-of-two-arrays](https://leetcode.com/problems/intersection-of-two-arrays/) |

## Problem Description & Examples
### Goal
Given two integer arrays, identify the unique elements that appear in both arrays. The resulting collection should contain each common element exactly once, regardless of how many times it appears in the input arrays. The order of the output does not matter.

### Function Contract
**Inputs**

- `nums1`: A list of integers.
- `nums2`: A list of integers.

**Return value**

- A list of integers representing the unique intersection of the two input arrays.

### Examples
**Example 1**

- Input: `nums1 = [1, 2, 2, 1], nums2 = [2, 2]`
- Output: `[2]`

**Example 2**

- Input: `nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]`
- Output: `[9, 4]`

**Example 3**

- Input: `nums1 = [1, 2, 3], nums2 = [4, 5, 6]`
- Output: `[]`

---

## Underlying Base Algorithm(s)
The most efficient approach utilizes a Hash Set to achieve linear time complexity. By converting one array into a set, we enable O(1) average-time lookups. We then iterate through the second array, checking for existence in the set and adding matches to a result set to ensure uniqueness.

---

## Complexity Analysis
- **Time Complexity**: O(n + m), where n and m are the lengths of the two input arrays. We traverse each array exactly once.
- **Space Complexity**: O(min(n, m)), as we store the unique elements of the smaller array in a hash set.
