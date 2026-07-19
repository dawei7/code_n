# Kth Smallest Product of Two Sorted Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2040 |
| Difficulty | Hard |
| Topics | Array, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/) |

## Problem Description

### Goal

Two integer arrays `nums1` and `nums2` are sorted in non-decreasing order.
Form one product for every index pair by multiplying an element from the first
array by an element from the second. Equal values and equal products retain
their full multiplicity because different index pairs are distinct choices.

Order all of these pair products from smallest to largest. Given the 1-based
rank `k`, return the product occupying that position. Input values may be
negative, zero, or positive, so product order cannot be obtained by advancing
one uniformly directed pair of pointers.

### Function Contract

Let $M$ and $N$ be the two array lengths, let
$A=\min(M,N)$, $B=\max(M,N)$, and let $R=10^{10}$ be the maximum absolute
product.

**Inputs**

- `nums1`, `nums2`: non-decreasing integer arrays with
  $1 \le M,N \le 5\cdot10^4$ and values from $-10^5$ through $10^5$.
- `k`: a 1-based rank satisfying $1 \le k \le MN$.

**Return value**

- The `k`th smallest value among all $MN$ indexed pair products.

### Examples

**Example 1**

- Input: `nums1 = [2, 5], nums2 = [3, 4], k = 2`
- Output: `8`
- Explanation: The first two products are `6` and `8`.

**Example 2**

- Input: `nums1 = [-4, -2, 0, 3], nums2 = [2, 4], k = 6`
- Output: `0`
- Explanation: Four products are negative, followed by the two zero products.

**Example 3**

- Input: `nums1 = [-2, -1, 0, 1, 2], nums2 = [-3, -1, 2, 4, 5], k = 3`
- Output: `-6`
