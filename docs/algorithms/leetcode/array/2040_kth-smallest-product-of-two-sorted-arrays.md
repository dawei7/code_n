# Kth Smallest Product of Two Sorted Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2040 |
| Difficulty | Hard |
| Topics | Array, Binary Search |
| Official Link | [kth-smallest-product-of-two-sorted-arrays](https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/) |

## Problem Description & Examples
### Goal
Given two sorted arrays, consider every pair product. Find the `k`th smallest product.

### Function Contract
**Inputs**

- `nums1`, `nums2`: sorted integer arrays.
- `k`: one-based rank among all pair products.

**Return value**

Return the `k`th smallest product.

### Examples
**Example 1**

- Input: `nums1 = [2,5], nums2 = [3,4], k = 2`
- Output: `8`

**Example 2**

- Input: `nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6`
- Output: `0`

**Example 3**

- Input: `nums1 = [-2,-1,0,1,2], nums2 = [-3,-1,2,4,5], k = 3`
- Output: `-6`

---

## Underlying Base Algorithm(s)
Binary search the product value. For a candidate `x`, count how many pair products are `<= x` using the sorted order and per-value binary searches or two-pointer handling by sign. The smallest value with count at least `k` is the answer.

---

## Complexity Analysis
- **Time Complexity**: `O(n log m log R)` with per-row binary searches over the product range.
- **Space Complexity**: `O(1)`
