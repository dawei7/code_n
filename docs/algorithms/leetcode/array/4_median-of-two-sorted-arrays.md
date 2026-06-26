# Median of Two Sorted Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 4 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Divide and Conquer |
| Official Link | [median-of-two-sorted-arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) |

## Problem Description & Examples
### Goal
Given two individually sorted integer arrays, return the median value of all elements as if the arrays had been merged. The solution should avoid building the merged array and instead search for the split point between the left and right halves.

### Function Contract
**Inputs**

- `nums1`: List[int] sorted in nondecreasing order
- `nums2`: List[int] sorted in nondecreasing order

**Return value**

float - the median of the combined multiset

### Examples
**Example 1**

- Input: `nums1 = [1, 3], nums2 = [2]`
- Output: `2.0`

**Example 2**

- Input: `nums1 = [1, 2], nums2 = [3, 4]`
- Output: `2.5`

**Example 3**

- Input: `nums1 = [], nums2 = [7]`
- Output: `7.0`

---

## Underlying Base Algorithm(s)
Binary search over a partition of the smaller sorted array.

---

## Complexity Analysis
- **Time Complexity**: `O(log(min(m, n)))`
- **Space Complexity**: `O(1)`
