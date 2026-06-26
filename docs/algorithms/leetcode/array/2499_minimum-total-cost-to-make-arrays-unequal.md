# Minimum Total Cost to Make Arrays Unequal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2499 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Greedy, Counting |
| Official Link | [minimum-total-cost-to-make-arrays-unequal](https://leetcode.com/problems/minimum-total-cost-to-need-arrays-unequal/) |

## Problem Description & Examples
### Goal
Given two integer arrays of equal length, calculate the minimum cost to swap elements within the first array such that for all indices `i`, `nums1[i]` is not equal to `nums2[i]`. A swap between index `i` and `j` incurs a cost of `i + j`. If it is impossible to satisfy the condition, return -1.

### Function Contract
**Inputs**

- `nums1`: A list of integers representing the first array.
- `nums2`: A list of integers representing the second array.

**Return value**

- An integer representing the minimum total cost to satisfy the condition, or -1 if no such configuration exists.

### Examples
**Example 1**

- Input: `nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 3, 4, 5]`
- Output: `10`

**Example 2**

- Input: `nums1 = [2, 2, 2, 2], nums2 = [1, 3, 4, 5]`
- Output: `0`

**Example 3**

- Input: `nums1 = [1, 2, 2, 2], nums2 = [1, 2, 2, 2]`
- Output: `-1`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy approach with Frequency Counting**. First, identify all indices `i` where `nums1[i] == nums2[i]`. These indices must be resolved. We prioritize swapping these indices with other indices `j` where `nums1[j] != nums2[j]` and `nums1[j] != nums1[i]` and `nums2[j] != nums1[i]`. If we still have unresolved indices, we must swap them with each other. The constraint is that the most frequent element among the problematic indices cannot exceed half the total number of problematic indices.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the arrays, as we iterate through the arrays a constant number of times to count frequencies and calculate costs.
- **Space Complexity**: `O(n)` to store the frequency map of the problematic indices.
