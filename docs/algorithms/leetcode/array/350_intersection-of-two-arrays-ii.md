# Intersection of Two Arrays II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 350 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Two Pointers, Binary Search, Sorting |
| Official Link | [intersection-of-two-arrays-ii](https://leetcode.com/problems/intersection-of-two-arrays-ii/) |

## Problem Description & Examples
### Goal
Given two integer arrays, identify the elements that appear in both arrays. The result must include each element as many times as it appears in both arrays, and the order of the output elements does not matter.

### Function Contract
**Inputs**

- `nums1`: A list of integers.
- `nums2`: A list of integers.

**Return value**

- A list of integers representing the intersection of the two input arrays, where each element is repeated according to its minimum frequency in both arrays.

### Examples
**Example 1**

- Input: `nums1 = [1, 2, 2, 1], nums2 = [2, 2]`
- Output: `[2, 2]`

**Example 2**

- Input: `nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]`
- Output: `[4, 9]`

**Example 3**

- Input: `nums1 = [1, 2], nums2 = [1, 1]`
- Output: `[1]`

---

## Underlying Base Algorithm(s)
The optimal approach utilizes a Hash Map (Frequency Counter) to store the occurrences of elements in the first array. We then iterate through the second array, checking if the current element exists in the map with a count greater than zero. If it does, we add it to the result and decrement its count in the map.

---

## Complexity Analysis
- **Time Complexity**: `O(n + m)`, where `n` and `m` are the lengths of the two input arrays. We traverse each array exactly once.
- **Space Complexity**: `O(min(n, m))`, as we store the frequency counts of the smaller array in a hash map.
