# Number of Ways Where Square of Number Is Equal to Product of Two Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1577 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Math, Two Pointers |
| Official Link | [number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers](https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/) |

## Problem Description & Examples
### Goal
Count triplets where the square of one number from one array equals the product
of two numbers from the other array.

### Function Contract
**Inputs**

- `nums1`: the first integer array.
- `nums2`: the second integer array.

**Return value**

The total number of valid triplets across both directions.

### Examples
**Example 1**

- Input: `nums1 = [7, 4], nums2 = [5, 2, 8, 9]`
- Output: `1`

**Example 2**

- Input: `nums1 = [1, 1], nums2 = [1, 1, 1]`
- Output: `9`

**Example 3**

- Input: `nums1 = [7, 7, 8, 3], nums2 = [1, 2, 9, 7]`
- Output: `2`

---

## Underlying Base Algorithm(s)
Count products of all unordered pairs in one array, then for each value in the
other array add the frequency of `value * value`. Do this in both directions:
squares from `nums1` against pair products from `nums2`, and squares from
`nums2` against pair products from `nums1`.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2 + m^2)`.
- **Space Complexity**: `O(n^2 + m^2)` in the worst case for product counts.
